# from syntax.ez_parser import Parser
from lexical.lexer import Lexer
from utilities.symbol_table_v2 import symbol_table

test = "Number num = 10; for (Number num1; num1 < 10; num1++) { String a = 'b'; if (True) { return a } }"
while_loop = "Number num = 1; while (num <= 10) { num++; }"
bedmas = "Number num1 = 10; Number num2 = 5; num1 = num1 + num2; if (num1 > 14) { num2 = 10 / 2 + 1; } elif { num2 = 2*3+4; }"
for_loop = "Number number = 0; for (Number i=0; i <10; i++) { number = number + i }"

l = Lexer()
l.build()
l.input(for_loop)
given_token = l.token()

while given_token != None:
    given_token = l.token()

print(symbol_table)