from antlr4 import *

from CLexer import CLexer
from CListener import CListener
from CParser import CParser


class FunctionListener(CListener):
    def enterFunctionDefinition(self, ctx: CParser.FunctionDefinitionContext):
        # Get the function name
        function_name = ctx.declarator().directDeclarator().directDeclarator().getText()

        # Get the return type
        return_type = ctx.declarationSpecifiers().getText()

        print(f"Function Name: {function_name}, Return Type: {return_type}")


def main():
    # load the input C file
    input_stream = FileStream("myfile.c")

    # create a lexer and parser
    lexer = CLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)

    # create the parse tree
    tree = parser.compilationUnit()

    # create the listener and walker
    listener = FunctionListener()
    walker = ParseTreeWalker()

    # walk the tree
    walker.walk(listener, tree)


if __name__ == '__main__':
    main()
