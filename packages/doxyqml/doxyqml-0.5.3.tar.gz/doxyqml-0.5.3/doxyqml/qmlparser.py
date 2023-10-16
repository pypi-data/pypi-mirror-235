import doxyqml.lexer as lexer

from doxyqml.qmlclass import QmlComponent, QmlArgument, QmlEnum, QmlEnumerator, QmlProperty, QmlFunction, QmlSignal, QmlAttribute


class QmlParserError(Exception):
    def __init__(self, msg, token):
        Exception.__init__(self, msg)
        self.token = token


class QmlParserUnexpectedTokenError(QmlParserError):
    def __init__(self, token):
        QmlParserError.__init__(self, "Unexpected token: {}".format(str(token)), token)


def parse_class_definition(reader, cls, parse_sub_classes = True):
    token = reader.consume_wo_comments()
    if token.type != lexer.BLOCK_START:
        raise QmlParserError("Expected '{' after base class name", token)
    last_comment_token = None
    while not reader.at_end():
        token = reader.consume()
        if is_comment_token(token):
            if last_comment_token:
                cls.add_element(last_comment_token.value)
            last_comment_token = token
        elif token.type == lexer.KEYWORD:
            parse_class_content(reader, cls, token, last_comment_token)
            last_comment_token = None
        elif token.type == lexer.COMPONENT and parse_sub_classes:
            parse_class_component(reader, cls, token, last_comment_token)
            last_comment_token = None
        elif token.type == lexer.ATTRIBUTE:
            parse_class_attribute(reader, cls, token, last_comment_token)
            last_comment_token = None
        elif token.type == lexer.BLOCK_START:
            skip_block(reader)
        elif token.type == lexer.BLOCK_END:
            break
    if last_comment_token:
        cls.add_element(last_comment_token.value)


def parse_class_content(reader, cls, token, doc_token):
    keyword = token.value
    if keyword.endswith("property"):
        obj = parse_property(reader, keyword)
    elif keyword == "function":
        obj = parse_function(reader)
    elif keyword == "signal":
        obj = parse_signal(reader)
    elif keyword == "enum":
        obj = parse_enum(reader)
    else:
        raise QmlParserError("Unknown keyword '%s'" % keyword, token)
    if doc_token is not None:
        obj.doc = doc_token.value
        obj.doc_is_inline = (doc_token.type == lexer.ICOMMENT)
    if obj.name.startswith('_'):
        return
    cls.add_element(obj)


def parse_class_component(reader, cls, token, doc_token):
    obj = QmlComponent(token.value)
    parse_class_definition(reader, obj)

    if doc_token is not None:
        obj.comment = doc_token.value

    cls.add_element(obj)


def parse_class_attribute(reader, cls, token, doc_token) -> QmlAttribute:
    obj = QmlAttribute()
    obj.name = token.value

    # Should be colon
    token = reader.consume_expecting(lexer.CHAR)
    token = reader.consume()
    if token.type == lexer.BLOCK_START or token.type == lexer.ARRAY_START:
        skip_block(reader)
    else:
        obj.value = token.value

    if doc_token is not None:
        obj.doc = doc_token.value

    cls.add_element(obj)


def parse_property(reader, property_token_value) -> QmlProperty:
    prop = QmlProperty()
    prop.is_default = property_token_value.startswith("default")
    prop.is_readonly = property_token_value.startswith("readonly")

    token = reader.consume_expecting(lexer.ELEMENT)
    prop.type = token.value

    token = reader.consume_expecting(lexer.ELEMENT)
    prop.name = token.value
    return prop


def parse_function(reader) -> QmlFunction:
    obj = QmlFunction()
    token = reader.consume_expecting(lexer.ELEMENT)
    obj.name = token.value

    reader.consume_expecting(lexer.CHAR, "(")
    obj.args = parse_arguments(reader)
    return obj


def parse_enum(reader) -> QmlEnum:
    obj = QmlEnum()
    token = reader.consume_expecting(lexer.ELEMENT)
    obj.name = token.value

    reader.consume_expecting(lexer.BLOCK_START)
    prev_comment_token = None
    prev_enumerator = None

    while not reader.at_end():
        token = reader.consume()
        if is_comment_token(token):
            if token.type == lexer.ICOMMENT:
                if prev_enumerator == None:
                    # this is still for the enum itself
                    obj.doc = token.value
                    obj.doc_is_inline = True
                else:
                    # for last enum
                    prev_enumerator.doc = token.value
                    prev_enumerator.doc_is_inline = True
            else:
                prev_comment_token = token
        elif token.type == lexer.BLOCK_END:
            break
        elif token.type == lexer.ELEMENT:
            if prev_enumerator:
                obj.enumerators.append(prev_enumerator)
            prev_enumerator, block_end = parse_enumerator(reader, token.value)
            if prev_comment_token:
                 prev_enumerator.doc = prev_comment_token.value
            prev_comment_token = None
            if block_end:
                break
            continue
        elif token.type == lexer.CHAR and token.value == ",":
            continue
        else:
            raise QmlParserUnexpectedTokenError(token)

    if prev_enumerator:
        prev_enumerator.is_last = True
        obj.enumerators.append(prev_enumerator)
    return obj


def parse_enumerator(reader, name):
    obj = QmlEnumerator(name)

    block_end = False

    while not reader.at_end():
        token = reader.consume()
        if is_comment_token(token):
            if token.type == lexer.ICOMMENT:
                # we could catch the inline comment for the last item here
                obj.doc = token.value
                obj.doc_is_inline = True
        elif token.type == lexer.BLOCK_END:
            block_end = True
            break
        elif token.type == lexer.CHAR:
            if token.value == ",":
                break
            elif token.value == "=":
                token = reader.consume_expecting(lexer.ELEMENT)
                obj.initializer = token.value
                continue
        else:
            raise QmlParserUnexpectedTokenError(token)

    return obj, block_end


def parse_signal(reader):
    obj = QmlSignal()
    token = reader.consume_expecting(lexer.ELEMENT)
    obj.name = token.value

    idx = reader.idx
    token = reader.consume_wo_comments()
    if token.type == lexer.CHAR and token.value == "(":
        obj.args = parse_arguments(reader, typed=True)
    else:
        reader.idx = idx
    return obj


def parse_arguments(reader, typed=False):
    token = reader.consume_wo_comments()
    spread = False
    if token.type == lexer.CHAR and token.value == ")":
        return []
    elif token.type == lexer.ELLIPSES:
        token =  reader.consume_expecting(lexer.ELEMENT)
        spread = True
    elif token.type != lexer.ELEMENT:
        raise QmlParserUnexpectedTokenError(token)

    args = []
    while True:
        if typed:
            arg_type = token.value
            token = reader.consume_expecting(lexer.ELEMENT)
            arg = QmlArgument(token.value)
            arg.type = arg_type
        elif spread:
            arg = QmlArgument(token.value)
            arg.spread = True
            spread = False
        else:
            arg = QmlArgument(token.value)

        token = reader.consume_expecting(lexer.CHAR)

        if token.value == "=":
            default_value = ""
            while True:
                token = reader.consume_expecting(
                    [lexer.ELEMENT, lexer.CHAR, lexer.STRING, lexer.BLOCK_START, lexer.ARRAY_START]
                )
                if token.value in (")", ","):
                    break
                if token.value == "{":
                    token = reader.consume_expecting(lexer.BLOCK_END)
                    default_value += "{}"
                elif token.value == "[":
                    token = reader.consume_expecting(lexer.ARRAY_END)
                    default_value += "[]"
                else:
                    default_value += token.value
                # token = reader.consume_expecting(lexer.CHAR)
            arg.default_value = default_value
        args.append(arg)

        if token.value == ":":
            token = reader.consume_expecting(lexer.ELEMENT)
            arg.type = token.value
            token = reader.consume_expecting(lexer.CHAR)

        if token.value == ")":
            return args
        elif token.value != ",":
            raise QmlParserUnexpectedTokenError(token)

        token = reader.consume_expecting([lexer.ELEMENT, lexer.ELLIPSES])


        if token.type == lexer.ELLIPSES:
            token = reader.consume_expecting(lexer.ELEMENT)
            spread = True


def skip_block(reader):
    count = 1
    while True:
        token = reader.consume_wo_comments()
        if token.type == lexer.BLOCK_START:
            count += 1
        elif token.type == lexer.BLOCK_END:
            count -= 1
            if count == 0:
                return


def parse_header(reader, cls):
    while not reader.at_end():
        token = reader.consume()
        if is_comment_token(token):
            cls.add_header_comment(token.value)
        elif token.type == lexer.IMPORT:
            cls.add_import(token.value)
        elif token.type == lexer.PRAGMA:
            cls.add_pragma(token.value)
        elif token.type == lexer.COMPONENT:
            cls.base_name = token.value
            return
        else:
            raise QmlParserUnexpectedTokenError(token)


def parse_footer(reader, cls):
    while not reader.at_end():
        token = reader.consume()
        if is_comment_token(token):
            cls.add_footer_comment(token.value)
        else:
            raise QmlParserUnexpectedTokenError(token)


def is_comment_token(token):
    return token.type in (lexer.COMMENT, lexer.ICOMMENT)


class TokenReader(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0

    def consume(self):
        token = self.tokens[self.idx]
        self.idx += 1
        return token

    def consume_wo_comments(self):
        while True:
            token = self.consume()
            if not is_comment_token(token):
                return token

    def consume_expecting(self, expected_types, value=None):
        token = self.consume_wo_comments()
        if type(expected_types) is list:
            if token.type not in expected_types:
                raise QmlParserError(
                    "Expected token of type '%s', got '%s' instead" % (expected_types, token.type), token)
        elif token.type != expected_types:
            raise QmlParserError(
                "Expected token of type '%s', got '%s' instead" % (expected_types, token.type), token)
        if value is not None and token.value != value:
            raise QmlParserError("Expected token with value '%s', got '%s' instead" % (
                value, token.value), token)
        return token

    def at_end(self):
        return self.idx == len(self.tokens)


def parse(tokens, cls, parse_sub_classes = True):
    reader = TokenReader(tokens)
    parse_header(reader, cls)
    parse_class_definition(reader, cls, parse_sub_classes)
    parse_footer(reader, cls)
