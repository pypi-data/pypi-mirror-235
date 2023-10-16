import logging
import re
import typing

TYPE_RX = r"(?P<prefix>\s+type:)(?P<type>[\w\*.<>|]+)"

BASE_NAME_DICT = {
    "QtObject": "QtQml.QtObject",
    "Item": "QtQuick.Item",
}


def post_process_type(rx, text, type):
    match = rx.search(text)
    if match:
        type = match.group("type")
        text = text[:match.start("prefix")] + text[match.end("type"):]
    return text, type

def is_cxx_comment(text):
    if not isinstance(text, str):
        text = str(text)
    return text.startswith("//")


class QmlBaseComponent():
    def __init__(self, name, version = None, should_separate_blocks = True):
        self.name = name
        self.base_name = ""
        self.elements = []
        self.should_separate_blocks = should_separate_blocks

        lst = name.split(".")
        self.class_name = lst[-1]
        self.namespaces = lst[:-1]

    def get_attributes(self):
        return [x for x in self.elements if isinstance(x, QmlAttribute)]

    def get_properties(self):
        return [x for x in self.elements if isinstance(x, QmlProperty)]

    def get_functions(self):
        return [x for x in self.elements if isinstance(x, QmlFunction)]

    def get_signals(self):
        return [x for x in self.elements if isinstance(x, QmlSignal)]

    def add_element(self, element):
        self.elements.append(element)

    def starts_with_cxx_comment(self):
        if not hasattr(self, "doc_is_inline") or not hasattr(self, "doc"):
            return False
        if self.doc_is_inline:
            return False
        return self.doc.startswith("//")

    def __str__(self):
        lst = []
        self._export_content(lst)
        return "\n".join(lst)

    def _export_element(self, element, lst):
        doc = str(element)
        if doc:
            lst.append(doc)

    def _export_elements(self, input_list, lst, filter=None):
        for element in input_list:
            if filter and not filter(element):
                continue
            self._export_element(element, lst)

    def _export_element_w_access(self, element, lst, is_public,
            last_was_public, last_was_cxx_comment):
        if is_public != last_was_public:
            if is_public:
                lst.append("public:")
            else:
                lst.append("private:")
        elif last_was_cxx_comment and is_cxx_comment(element) and self.should_separate_blocks:
            lst.append("")
        self._export_element(element, lst)

    def _start_class(self, lst):
        class_decl = "class " + self.class_name
        if self.base_name:
            for alias, replacement in self.alias.items():
                self.base_name = re.sub(alias, replacement, self.base_name)
            self.base_name = BASE_NAME_DICT.get(self.base_name, self.base_name)

            class_decl += " : public " + self.base_name

        class_decl += " {"
        lst.append(class_decl)

    def _end_class(self, lst):
        lst.append("};")


class QmlClass(QmlBaseComponent):
    SINGLETON_COMMENT = "/** @remark This component is a singleton */"
    VERSION_COMMENT = "/** @version %s */"
    IMPORT_STATEMENT_COMMENT = "/** {} <br><b>Import Statement</b> \\n @code import {} @endcode */"

    def __init__(self, name, version=None, modulename=None, should_separate_blocks = True):
        QmlBaseComponent.__init__(self, name, version, should_separate_blocks)
        self.header_comments = []
        self.footer_comments = []
        self.imports = []
        self.alias = {}
        self.modulename = modulename
        self.version = version

    def add_pragma(self, decl):
        args = decl.split(' ', 2)[1].strip()

        if args.lower() == "singleton":
            self.header_comments.append(QmlClass.SINGLETON_COMMENT)

    def add_import(self, decl):
        modules = decl.split()
        module = modules[1]
        if module[0] == '"':
            # Ignore directory or javascript imports for now
            return
        if "as" in modules:
            self.alias[modules[modules.index("as")+1]] = modules[1]
        self.imports.append(module)

    def add_header_comment(self, obj):
        self.header_comments.append(obj)

    def add_footer_comment(self, obj):
        self.footer_comments.append(obj)

    def _export_header(self, lst):
        for module in self.imports:
            lst.append("using namespace %s;" % module.replace('.', '::'))
        if self.namespaces:
            lst.append("namespace %s {" % '::'.join(self.namespaces))

        lst.extend([str(x) for x in self.header_comments])

        if self.modulename:
            # we want to insert a newline if there has been any comments (usually a description of the class)
            newline = ""

            # is there any comments before this one?
            any_comments = len(self.header_comments) > 0

            # and if there is any comments, is the last one a SPDX message? they don't render, so don't insert a
            # useless newline
            is_spdx_last = any_comments and ("SPDX" not in self.header_comments[len(self.header_comments) - 1])

            if any_comments and is_spdx_last:
                newline = "\\n"

            lst.append(QmlClass.IMPORT_STATEMENT_COMMENT.format(newline, self.modulename))
        if self.version:
            lst.append(QmlClass.VERSION_COMMENT % self.version)


    def _export_footer(self, lst):
        lst.extend([str(x) for x in self.footer_comments])

        if self.namespaces:
            lst.append("}")

    def _export_content(self, lst):
        self._export_header(lst)

        # Public members.
        self._start_class(lst)

        last_element_was_public = False
        last_element_was_cxx_comment = False
        for element in self.elements:
            if str(element) == "" or isinstance(element, str):
                self._export_element_w_access(element, lst,
                        last_element_was_public, last_element_was_public,
                        last_element_was_cxx_comment)
                last_element_was_cxx_comment = is_cxx_comment(element)
            elif element.is_public_element():
                self._export_element_w_access(element, lst, True,
                        last_element_was_public, last_element_was_cxx_comment)
                last_element_was_public = True
                last_element_was_cxx_comment = False
            else:
                self._export_element_w_access(element, lst, False,
                        last_element_was_public, last_element_was_cxx_comment)
                last_element_was_public = False
                last_element_was_cxx_comment = False

        self._end_class(lst)
        self._export_footer(lst)

    def is_public_element(self):
        return True


class QmlComponent(QmlBaseComponent):
    """A component inside a QmlClass"""

    def __init__(self, name):
        QmlBaseComponent.__init__(self, name)
        self.comment = None

    def _export_content(self, lst):
        component_id = self.get_component_id()
        if component_id:
            if self.comment:
                lst.append(self.comment)

            lst.append("%s %s;" % (self.class_name, component_id))

        # Export child components with the top-level component. This avoids
        # very deep nesting in the generated documentation.
        self._export_elements(self.elements, lst, filter=lambda x:
                              isinstance(x, QmlComponent))

    def get_component_id(self):
        # Returns the id of the component, if it has one
        for attr in self.get_attributes():
            if attr.name == "id":
                return attr.value
        return None

    def is_public_element(self):
        return False


class QmlArgument(object):
    def __init__(self, name):
        self.type = ""
        self.name = name
        self.default_value = None
        self.spread = False

    def __str__(self):
        if self.spread:
            return '.../*{}*/'.format(self.name)
        elif self.type == "":
            return self.name + self.default_value_string()
        else:
            return self.type + " " + self.name + self.default_value_string()

    def default_value_string(self):
        if self.default_value is None:
            return ''
        else:
            return ' = {}'.format(self.default_value)

    def is_public_element(self):
        return True


class QmlAttribute(object):
    def __init__(self):
        self.name = ""
        self.value = ""
        self.type = "var"
        self.doc = ""

    def __str__(self):
        if self.name != "id":
            lst = []
            if len(self.doc) > 0:
                lst.append(self.doc)
            lst.append(self.type + " " + self.name + ";")
            return "\n".join(lst)
        else:
            return ""

    def is_public_element(self):
        return False


class QmlProperty(object):
    type_rx = re.compile(TYPE_RX)

    DEFAULT_PROPERTY_COMMENT = "/** @remark This is the default property */"
    READONLY_PROPERTY_COMMENT = "/** @remark This property is read-only */"

    def __init__(self):
        self.type = ""
        self.is_default = False
        self.is_readonly = False
        self.name = ""
        self.doc = ""
        self.doc_is_inline = False

    def __str__(self):
        self.post_process_doc()
        lst = []
        if not self.doc_is_inline:
            lst.append(self.doc + "\n")
        if self.is_default:
            lst.append(self.DEFAULT_PROPERTY_COMMENT + "\n")
        elif self.is_readonly:
            lst.append(self.READONLY_PROPERTY_COMMENT + "\n")
        lst.append("Q_PROPERTY(%s %s READ dummyGetter_%s_ignore)"
            % (self.type, self.name, self.name))
        if self.doc_is_inline:
            lst.append(" " + self.doc)
        return "".join(lst)

    def post_process_doc(self):
        self.doc, self.type = post_process_type(self.type_rx, self.doc, self.type)

    def is_public_element(self):
        # Doxygen always adds Q_PROPERTY items as public members.
        return True


class QmlFunction(object):
    doc_arg_rx = re.compile(r"[@\\]param" + TYPE_RX + r"\s+(?P<name>\w+)")
    return_rx = re.compile(r"[@\\]returns?" + TYPE_RX)

    def __init__(self):
        self.type = "void"
        self.name = ""
        self.doc = ""
        self.doc_is_inline = False
        self.args = []

    def __str__(self):
        self.post_process_doc()
        arg_string = ", ".join([str(x) for x in self.args])
        lst = []
        if not self.doc_is_inline:
            lst.append(self.doc + "\n")
        lst.append("%s %s(%s);" % (self.type, self.name, arg_string))
        if self.doc_is_inline:
            lst.append(" " + self.doc)
        return "".join(lst)

    def post_process_doc(self):
        def repl(match):
            # For each argument with a specified type, update arg.type and return a typeless @param line
            type = match.group("type")
            name = match.group("name")
            for arg in self.args:
                if arg.name == name:
                    arg.type = type
                    break
            else:
                logging.warning("In function %s(): Unknown argument %s" % (self.name, name))
            return "@param %s" % name

        self.doc = self.doc_arg_rx.sub(repl, self.doc)
        self.doc, self.type = post_process_type(self.return_rx, self.doc, self.type)

    def is_public_element(self):
        return True


class QmlEnum(object):
    def __init__(self):
        self.name = ""
        self.doc = ""
        self.doc_is_inline = False
        self.enumerators = []

    def __str__(self):
        lst = []

        if self.doc and not self.doc_is_inline:
            lst.append(self.doc + "\n")
        lst.append("enum class %s {" % (self.name))
        if self.doc and self.doc_is_inline:
            lst.append(" " + self.doc)
        lst.append("\n")

        for e in self.enumerators:
            lst.append(str(e) + "\n")

        lst.append("};")
        return "".join(lst)

    def is_public_element(self):
        return True


class QmlEnumerator(object):
    def __init__(self, name):
        self.name = name
        self.initializer = ""
        self.is_last = False
        self.doc = ""
        self.doc_is_inline = False

    def __str__(self):
        lst = []
        if self.doc and not self.doc_is_inline:
            lst.append(self.doc + "\n")
        lst.append("%s" % (self.name))
        if self.initializer:
            lst.append(" = %s" % (self.initializer))
        if not self.is_last:
            lst.append(",")
        if self.doc and self.doc_is_inline:
            lst.append(" " + self.doc)
        return "".join(lst)

    def is_public_element(self):
        return True


class QmlSignal(object):
    def __init__(self):
        self.name = ""
        self.doc = ""
        self.doc_is_inline = False
        self.args = []

    def __str__(self):
        arg_string = ", ".join([str(x) for x in self.args])
        lst = []
        if not self.doc_is_inline:
            lst.append(self.doc + "\n")
        lst.append("Q_SIGNALS: void %s(%s); " % (self.name, arg_string))
        if self.doc_is_inline:
            lst.append(self.doc + "\n")
        # Appending "public:" here makes it possible to declare a signal without
        # turning all functions defined after into signals.
        # It could be replaced with the use of Q_SIGNAL, but my version of
        # Doxygen (1.8.4) does not support it
        lst.append("public:")
        return "".join(lst)

    def is_public_element(self):
        # Doxygen always adds Q_SIGNALS items as public members.
        return True
