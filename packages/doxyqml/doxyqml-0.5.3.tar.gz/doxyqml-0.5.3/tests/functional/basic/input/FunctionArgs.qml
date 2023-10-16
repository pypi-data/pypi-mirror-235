/*
 * Header bla
 */
import QtQuick 1.1

/**
 * A very simple item
 */
Item {
    /**
     * The 'foo' property
     */
    property int foo

    signal clicked(int x, int y)

    signal activated

    /**
     * Do something with arg1 and arg2
     * @param type:string arg1 first argument
     * @param type:int arg2 second argument
     */
    function doSomething(arg1, arg2) {
        console.log("arg1=" + arg1);
    }

    /**
     * A badly documented function. Missing one argument and documenting a
     * non-existing document
     * @param type:string foo first argument
     * @param type:int baz this argument does not exist
     */
    function badlyDocumented(foo, bar) {
    }

    property string escaped: "a string \n \" \t with escaped chars"
    property string block: "a string with some block {({ ] } chars"

    /**
     * Compute the arg^2
     * @return type:int the result
     */
    function square(arg) {
        return arg * arg;
    }

    /**
     * Function with int default parameter
     * @param type:int arg A parameter with a defaultvalue
     * @return type:int the result
     */
    function intDefaultParameter(arg = 0) {
        return arg;
    }

    /**
     * Function with string default parameter
     * @param type:string arg A parameter with a default value
     * @return type:string the result
     */
    function stringDefaultParameter(arg = "hello") {
        return arg;
    }

    /**
     * Function with property as default parameter
     * @param type:int arg A parameter with a default value
     * @return type:int the result
     */
    function propDefaultParameter(arg = foo) {
        return arg;
    }

    /**
     * Function that takes a pointer type parameter
     * @param type:QObject* arg A pointer to an object derived from a QObject type
     */
    function handleAnObject(arg) {
      arg.aMethod()
    }

    /// One-line comment
    function refresh() {
    }

    /// Function that takes an empty object as default value for a parameter
    function objectDefaultParam(arg = {}) {
        return arg
    }

    /// Function that has arguments and a spread argument
    function argumentsWithSpread(arg1, arg2 = {}, ...args) {
      return arg1;
    }

    /// Function that has only spread arguments
    function onlySpread(...args) {
    }

    /// Function that takes an empty array as default value for a parameter
    function arrayDefaultParam(arg = []) {
        return arg
    }

    /// Default values can now be expressions
    function complicatedDefaultValue(area = 10.0 * 20.0) {}

    /// Function with arguments
    function typedFunction(a: int, arg: var, item: Item) {}

    /// Private function
    function __privateFunction() {}

    Item {
    }

    Item {}

    property /* foo */ int /* bar */ weirdProperty /* baz */ : /* foo */ 12
}
