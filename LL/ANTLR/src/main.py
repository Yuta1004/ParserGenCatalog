# Code from : https://medium.com/@kv391/antlr4-grammar-a-quick-tutorial-e1f0fb6ca4ff

from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

expr = input("Enter an expression: ")
input_stream = InputStream(expr)
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
tree = parser.expr()

print("Accept(or no-error-text):", tree.getText())
