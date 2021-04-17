import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'lexical')))
from lexer import Lexer
sys.path.append(os.path.abspath(os.path.join('..', 'semantic')))
from ez_parser import Parser
sys.path.append(os.path.abspath(os.path.join('..', 'intermediate')))
from codegen import CodeGen
sys.path.append(os.path.abspath(os.path.join('..', 'assembly')))
from assemblygen import AssemblyGen


def save_results(result, outFile):
    f = open('./results/{}.txt'.format(outFile), 'w')
    f.write(str(result))
    f.close()

def run_test(source, test_number):
    # Build lexer
    l = Lexer()
    l.build()
    l.input(source)
    given_tokens = ''
    current_token = l.token()
    # Loop through tokens
    while current_token is not None:
        given_tokens += str(current_token) + '\n'
        current_token = l.token()
    # Save the results for viewing, even though we will discard them
    save_results(given_tokens, 'test_{}_lexical'.format(test_number))
    # Build parser
    p = Parser()
    p.build()
    # Write stderr to file, it stores our lexemes as they are translated
    # by the syntax parser
    sys.stderr = open('./results/test_{}_syntax.txt'.format(test_number), 'w')
    # Generate semantic tree
    given_tree = p.parse(source, debug=True)
    save_results(given_tree, 'test_{}_semantic'.format(test_number))
    # Init codegen
    c = CodeGen()
    c.build()
    # Generate intermediate code
    given_code = c.generate(given_tree)
    save_results(given_code, 'test_{}_intermediate'.format(test_number))
    # Init assemblygen
    a = AssemblyGen()
    # Generate assembly code
    given_assembly = a.generate(given_code)
    save_results(given_assembly, 'test_{}_assembly'.format(test_number))

# Test case 1
test1_f = open('./test_cases/testcase1.ez', 'r')
test1_source = test1_f.read()
test1_f.close()
run_test(test1_source, 1)

# Test case 2
test2_f = open('./test_cases/testcase2.ez', 'r')
test2_source = test2_f.read()
test2_f.close()
run_test(test2_source, 2)

# Test case 3
test3_f = open('./test_cases/testcase3.ez', 'r')
test3_source = test3_f.read()
test3_f.close()
run_test(test3_source, 3)
