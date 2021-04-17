# from syntax.ez_parser import Parser
from lexical.lexer import Lexer
from semantic.ez_parser import Parser
from intermediate.codegen import CodeGen
from utilities.symbol_table_v2 import symbol_table

while_loop = 'Number num = 1; while (num <= 10) { num++; }'
bedmas = 'Number num1 = 10; Number num2 = 5; num1 = num1 + num2; if (num1 > 14) { num2 = 10 / 2 + 1; } else { num2 = 2*3+4; }'
for_loop = 'Number number = 0; for (Number i = 0; i < 10; i++) { number = number + i; }'
tests = [(while_loop, 'WHILE LOOP'), (bedmas, 'BEDMAS'), (for_loop, 'FOR LOOP')]

for test in tests:
    source = test[0]
    source_name = test[1]

    print('{}\n\n--- Source Code: ---'.format(test[1]))
    print('{}\n'.format(source))

    # Parse source and return Abstract Syntax Tree (AST)
    p = Parser()
    p.build()
    ast = p.parse(source)

    # Generate Three Address Code (TAC)
    c = CodeGen()
    c.build()
    tac = c.generate(ast)

    print('--- Three Address Code: ---')
    print(tac)

    print('--- Symbol Table ---\n')
    print(symbol_table)
    symbol_table.clear()