import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'utilities')))
from ez_parser import Parser
from icecream import ic



def main():
    global incrementT
    global incrementL
    incrementT = 0
    incrementL = 0
    source_f = open('./given/testcase1.ez', 'r')
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
    global incrementT
    global incrementL
    if type(given_tree) is not tuple:
        return given_tree     
    elif given_tree[0] == 'statement':
        l = traverse(given_tree[1])
        r = traverse(given_tree[2])
        return '{}\n{}\n'.format(l,r)
    elif given_tree[0] == 'assignmentExpression':
        l = traverse(given_tree[2])
        r = traverse(given_tree[3])
        if type(r) is tuple:
            return('{}\n{} {} {}'.format(r[1], l, given_tree[1], r[0]))
            
        else:
            return '{} {} {}'.format(l,given_tree[1],r)
    elif given_tree[0] == 'ifStatement':
        l = traverse(given_tree[1])
        m = traverse(given_tree[2])
        r = traverse(given_tree[3])
        if not r:
            incrementL += 1
            part1 = 'if {} goto L{}\n'.format(l, incrementL)
            incrementL += 1
            part2 = 'goto L{}\n'.format(incrementL)
            incrementL += 1
            part3 = 'L{}: {} \n'.format(incrementL, m)
            incrementL += 1
            part4 = 'L{}: '.format(incrementL)
            return '{}{}{}{}'.format(part1,part2,part3,part4)
        else:
            incrementL += 1
            first = incrementL
            part1 = 'if {} goto L{}\n'.format(l, first)
            incrementL += 1
            second = incrementL
            part2 = 'goto L{}\nL{}: {} \n'.format(second, first, m)
            third = incrementL + 1
            part3 = 'goto L{} \nL{}: {} \nL{}:'.format(third,second,r,third)
            return '{}{}{}'.format(part1,part2,part3)
    elif given_tree[0] == 'relationExpression':
        l = traverse(given_tree[2])
        r = traverse(given_tree[3])
        return '{} {} {}'.format(l,given_tree[1],r)
    elif given_tree[0] == 'sumExpression':
        l = traverse(given_tree[2])
        r = traverse(given_tree[3])
        incrementT += 1
        t = 't{}'.format(incrementT)
        if type(l) is tuple:
            return (t, '{} = {}\n{} = {}'.format(l[0], l[1], t, '{} {} {}'.format(l[0],given_tree[1],r)))
            incrementT += 1
        return (t, '{} = {} {} {}'.format(t, l,given_tree[1],r))
    elif given_tree[0] == 'multiplyExpression':
        l = traverse(given_tree[2])
        r = traverse(given_tree[3])
        incrementT += 1
        t = 't{}'.format(incrementT)
        if type(l) is tuple:
            return (t, '{} = {}\n{} = {}'.format(l[0], l[1], t, '{} {} {}'.format(l[0],given_tree[1],r)))
            incrementT += 1
        return (t, '{} {} {}'.format(l,given_tree[1],r))
    elif given_tree[0] == 'iterationExpression':
        l = traverse(given_tree[2])
        r = traverse(given_tree[3])
        incrementT += 1
        t = 't{}'.format(incrementT)
        if type(l) is tuple:
            return (t, '{} = {}\n{} = {}'.format(l[0], l[1], t, '{} {} {}'.format(l[0],given_tree[1],r)))
            incrementT += 1
        return (t, '{} = {} {} {}'.format(t, l,given_tree[1],r))
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