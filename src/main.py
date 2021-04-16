# from syntax.ez_parser import Parser
from lexical.lexer import Lexer
from utilities.symbol_table_v2 import symbol_table

source = "Number num = 10; for (Number num1; num1 < 10; num1++) { String a = 'b'; if (True) { return a } }"
l = Lexer()
l.build()
l.input(source)
given_token = l.token()

while given_token != None:
    given_token = l.token()

print(symbol_table)