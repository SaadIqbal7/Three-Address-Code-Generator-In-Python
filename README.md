# Three-Address Code Generator In Python

## Description
The project implements a three-address code generator which converts C code to three-address code. The project implements 3 phases of compiler:
- Lexical Analyzer
- Parser
- Three-Address Code Generator

The lexical analyzer tokenizes the inputs into lexemes. These lexemes are passed to the parsers to generate the parse tree. This parse tree is then used to generate the three-address code.

In order to execute the project, use command

```
python main.py <file name>
```

If you don’t provide the file name, the program will prompt you to input a file name.

## Limitations
The project does not implement a few tokens commonly found in C like, `for` `return` `continue` `printf`. Functions and function calls are also not implemented. Although the three-address code generator converts C code, the array representation is like in Java e.g. `float[50] array;`. Variable initialization at time of decleration is not allow, you first have to declare the variable, `int i;` then, initialize the variable, `i = 10;`. For arrays, first declare the array then use index notation to assign values to array, `array[0] = 10;`
