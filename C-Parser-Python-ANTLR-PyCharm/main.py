from antlr4 import *

from CLexer import CLexer
from CListener import CListener
from CParser import CParser


class FunctionListener(CListener):
    def enterFunctionDefinition(self, ctx: CParser.FunctionDefinitionContext):
        print("Found a function: " + ctx.getText())


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
