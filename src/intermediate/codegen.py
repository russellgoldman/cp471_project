import unittest
import sys, os

class CodeGen(object):
    def build(self):
        self.incrementT = 0
        self.incrementL = 0

    def generate(self, given_tree):
        if type(given_tree) is not tuple:
            return given_tree     
        elif given_tree[0] == 'statement':
            l = self.generate(given_tree[1])
            r = self.generate(given_tree[2])
            return '{}\n{}\n'.format(l,r)
        elif given_tree[0] == 'assignmentExpression':
            l = self.generate(given_tree[2])
            r = self.generate(given_tree[3])
            if type(r) is tuple:
                return('{}\n{} {} {}'.format(r[1], l, given_tree[1], r[0]))
                
            else:
                return '{} {} {}'.format(l,given_tree[1],r)
        elif given_tree[0] == 'ifStatement':
            l = self.generate(given_tree[1])
            m = self.generate(given_tree[2])
            r = self.generate(given_tree[3])
            if not r:
                # Build the output
                self.incrementL += 1
                firstLabel = self.incrementL
                self.incrementL += 1
                secondLabel = self.incrementL
                return 'if {} goto L{}\ngoto L{}\nL{}: {} \nL{}: '.format(l, firstLabel, secondLabel, firstLabel, m, secondLabel)
            else:
                # Build the output
                self.incrementL += 1
                firstLabel = self.incrementL
                self.incrementL += 1
                secondLabel = self.incrementL
                self.incrementL += 1
                thirdLabel = self.incrementL
                return 'if {} goto L{}\ngoto L{}\nL{}: {} \ngoto L{} \nL{}: {} \nL{}:'.format(l, firstLabel, secondLabel, firstLabel, m, thirdLabel,secondLabel,r,thirdLabel)
        elif given_tree[0] == 'relationExpression':
            l = self.generate(given_tree[2])
            r = self.generate(given_tree[3])
            return '{} {} {}'.format(l,given_tree[1],r)
        elif given_tree[0] == 'sumExpression':
            l = self.generate(given_tree[2])
            r = self.generate(given_tree[3])
            self.incrementT += 1
            t = 't{}'.format(self.incrementT)
            if type(l) is tuple:
                return (t, '{} = {}\n{} = {}'.format(l[0], l[1], t, '{} {} {}'.format(l[0],given_tree[1],r)))
                self.incrementT += 1
            return (t, '{} = {} {} {}'.format(t, l,given_tree[1],r))
        elif given_tree[0] == 'multiplyExpression':
            l = self.generate(given_tree[2])
            r = self.generate(given_tree[3])
            self.incrementT += 1
            t = 't{}'.format(self.incrementT)
            if type(l) is tuple:
                return (t, '{} = {}\n{} = {}'.format(l[0], l[1], t, '{} {} {}'.format(l[0],given_tree[1],r)))
                self.incrementT += 1
            return (t, '{} {} {}'.format(l,given_tree[1],r))
        elif given_tree[0] == 'iterationExpression':
            l = self.generate(given_tree[2])
            r = self.generate(given_tree[3])
            self.incrementT += 1
            t = 't{}'.format(self.incrementT)
            if type(l) is tuple:
                return (t, '{} = {}\n{} = {}'.format(l[0], l[1], t, '{} {} {}'.format(l[0],given_tree[1],r)))
                self.incrementT += 1
            return (t, '{} = {} {} {}'.format(t, l,given_tree[1],r))
        elif given_tree[0] == 'whileStatement':
            l = self.generate(given_tree[1])
            r = self.generate(given_tree[2])

            # Build the output
            self.incrementL += 1
            firstLabel = self.incrementL
            self.incrementL += 1
            secondLabel = self.incrementL
            return 'if {} goto L{}\ngoto L{}\nL{}: {} \nL{}: '.format(l, firstLabel, secondLabel, firstLabel, r, secondLabel)
        elif given_tree[0] == 'forExpression':
            l = self.generate(given_tree[1])
            r = self.generate(given_tree[2])
            return (l,r)
        elif given_tree[0] == 'forStatement':
            l = self.generate(given_tree[1])
            r = self.generate(given_tree[2])

            # Build the output. Messy, but necessary
            self.incrementL += 1
            firstLabel = self.incrementL
            self.incrementL += 1
            secondLabel = self.incrementL
            self.incrementL += 1
            thirdLabel = self.incrementL
            return '{} \nL{}: if {} goto L{}\ngoto L{}\nL{}: {} \n  {} \ngoto L{}\nL{}:'.format(l[0], firstLabel, l[1][0], secondLabel, thirdLabel, secondLabel, r, l[1][1], firstLabel, thirdLabel)
        elif given_tree[0] == 'statementBodyExpression':
            l = self.generate(given_tree[1])
            r = self.generate(given_tree[2])
            return '{}\n{}'.format(l,r)