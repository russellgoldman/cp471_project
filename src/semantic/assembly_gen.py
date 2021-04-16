import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'utilities')))
from ez_parser import Parser


def main():

    source_f = open('./codegen/out.txt', 'r')
    source = source_f.read()
    source_f.close()

    print(codegen(source))

def codegen(source):
    registerCount = 0
    assembly = ""
    lineNumber = 0
    label = []
    source = source.split('\n')
    for line in source:      
        #if ":" in line:
        print(line)    
        if "if" in line:
            if ">" in line:
                assembly += "BGT r0, r1,"
            elif "<=" in line:
                assembly += "BLE r0, r1,"
            elif "<" in line:
                assembly += "BGT r1, r0,"
            elif ">=" in line:
                assembly += "BLE r1, r0,"
            elif "==" in line:
                assembly += "BGT r0, r1,"
                assembly += "BGT r1, r0,"
            if "goto" in line:
                assembly += " L1\n"
        elif "=" in line:
            if "+" in line:
                assembly += "ADD r0, r0, r1\n"
            elif "-" in line:
                assembly += "SUB r0, r0, r1\n"
            elif "*" in line:
                assembly += "DIV r0, r0, r1\n"
            elif "/" in line:
                assembly += "MUL r0, r0, r1\n"
            else:
                assembly += "ST a, r1\n"
        elif "goto" in line:
            assembly += "JMP L1\n"



        lineNumber += 1

    return assembly



if __name__ == '__main__':
    main()