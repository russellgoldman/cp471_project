import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'utilities')))
from ez_parser import Parser



def main():
    global incrementT
    global incrementL
    incrementT = 0
    incrementL = 0
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
            # Build the output
            incrementL += 1
            firstLabel = incrementL
            incrementL += 1
            secondLabel = incrementL
            return 'if {} goto L{}\ngoto L{}\nL{}: {} \nL{}: '.format(l, firstLabel, secondLabel, firstLabel, m, secondLabel)
        else:
            # Build the output
            incrementL += 1
            firstLabel = incrementL
            incrementL += 1
            secondLabel = incrementL
            incrementL += 1
            thirdLabel = incrementL
            return 'if {} goto L{}\ngoto L{}\nL{}: {} \ngoto L{} \nL{}: {} \nL{}:'.format(l, firstLabel, secondLabel, firstLabel, m, thirdLabel,secondLabel,r,thirdLabel)
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

        # Build the output
        incrementL += 1
        firstLabel = incrementL
        incrementL += 1
        secondLabel = incrementL
        return 'if {} goto L{}\ngoto L{}\nL{}: {} \nL{}: '.format(l, firstLabel, secondLabel, firstLabel, r, secondLabel)
    elif given_tree[0] == 'forExpression':
        l = traverse(given_tree[1])
        r = traverse(given_tree[2])
        return (l,r)
    elif given_tree[0] == 'forStatement':
        l = traverse(given_tree[1])
        r = traverse(given_tree[2])

        # Build the output. Messy, but necessary
        incrementL += 1
        firstLabel = incrementL
        incrementL += 1
        secondLabel = incrementL
        incrementL += 1
        thirdLabel = incrementL
        return '{} \nL{}: if {} goto L{}\ngoto L{}\nL{}: {} \n  {} \ngoto L{}\nL{}:'.format(l[0], firstLabel, l[1][0], secondLabel, thirdLabel, secondLabel, r, l[1][1], firstLabel, thirdLabel)
    elif given_tree[0] == 'statementBodyExpression':
        l = traverse(given_tree[1])
        r = traverse(given_tree[2])
        return '{}\n{}'.format(l,r)

if __name__ == '__main__':
    main()