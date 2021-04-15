import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'utilities')))
from ez_parser import Parser



def main():
    source_f = open('./given/testcase3.ez', 'r')
    source = source_f.read()
    source_f.close()

    # build parser
    p = Parser()
    p.build()
    # generate parse tree
    given_tree = p.parse(source)
    #print(given_tree)
    print(traverse(given_tree))

def traverse(given_tree):
    if type(given_tree) is not tuple:
        return given_tree     
    elif given_tree[0] == 'statement':
        l = traverse(given_tree[1])
        r = traverse(given_tree[2])
        return '\n{}\n{}\n'.format(l,r)
    elif given_tree[0] == 'assignmentExpression':
        l = traverse(given_tree[2])
        r = traverse(given_tree[3])
        return '{} {} {}'.format(l,given_tree[1],r)
    elif given_tree[0] == 'ifStatement':
        l = traverse(given_tree[1])
        m = traverse(given_tree[2])
        r = traverse(given_tree[3])
        if not r:
            return 'if {} goto L2\ngoto L3\nL2: {} \nL3: '.format(l,m)
        else:
            return 'if {} goto L2\ngoto L3\nL2: {} \ngoto L4 \nL3: {} \nL4:'.format(l,m,r)
    elif given_tree[0] == 'relationExpression':
        l = traverse(given_tree[2])
        r = traverse(given_tree[3])
        return '{} {} {}'.format(l,given_tree[1],r)
    elif given_tree[0] == 'sumExpression':
        l = traverse(given_tree[2])
        r = traverse(given_tree[3])
        return '{} {} {}'.format(l,given_tree[1],r)
    elif given_tree[0] == 'iterationExpression':
        l = traverse(given_tree[2])
        r = traverse(given_tree[3])
        return '{} {} {}'.format(l,given_tree[1],r)
    elif given_tree[0] == 'whileStatement':
        l = traverse(given_tree[1])
        r = traverse(given_tree[2])
        return 'while {} goto L2\ngoto L3\nL2: {} \nL3: '.format(l,r)
    elif given_tree[0] == 'forExpression':
        l = traverse(given_tree[1])
        r = traverse(given_tree[2])
        return (l,r)
    elif given_tree[0] == 'forStatement':
        l = traverse(given_tree[1])
        r = traverse(given_tree[2])
        return '{} \nL1: if {} goto L2\ngoto L3\nL2: {} \n  {} \ngoto L1\nL3:'.format(l[0],l[1][0],r,l[1][1])
    elif given_tree[0] == 'statementBodyExpression':
        l = traverse(given_tree[1])
        r = traverse(given_tree[2])
        return '{}\n{}'.format(l,r)

if __name__ == '__main__':
    main()