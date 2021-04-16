import unittest
import sys, os
import re


def main():

    source_f = open('../intermediate/codegen/out3.txt', 'r')
    source = source_f.read()
    source_f.close()

    print(codegen(source))

def codegen(source):
    registerCount = 0
    currentRegister = 0 
    assembly = ""
    lineNumber = 0
    label = []
    variable = []
    source = source.split('\n')
    for line in source:      
        split = line.split()
        for word in split:
            if re.search(r'([A-Za-z]|_)([A-Za-z]|[0-9]|_)*', word):#len(word) > 1:
                if  word[0] == "L"  and ":" not in word :
                    label.append(word)
                elif word != 'goto' and word != 'if' and word not in variable and ":" not in word :
                    variable.append(word)
                    assembly += "LD r{}, {}\n".format(registerCount, word)
                    registerCount += 1
        #print(line)    
        if "if" in line:
            if ">" in line:
                assembly += "BGT r0, r1,"            #"BGT r0, r1,"  
            elif "<=" in line:
                assembly += "BLE r0, r1,"            #"BLE r0, r1," 
            elif "<" in line:
                assembly += "BGT r1, r0,"            #"BGT r1, r0,"
            elif ">=" in line:
                assembly += "BLE r1, r0,"            #"BLE r1, r0," 
            elif "==" in line:
                assembly += "BGT r0, r1,"            #"BGT r0, r1,"
                assembly += "BGT r1, r0,"            #"BGT r1, r0,"
            if "goto" in line:
                assembly += " L1\n"
        elif "=" in line:
            if "+" in line:
                assembly += "ADD r0, r0, r1\n"      #"ADD r0, r0, r1\n" 
            elif "-" in line:
                assembly += "SUB r0, r0, r1\n"      #"SUB r0, r0, r1\n"
            elif "*" in line:
                assembly += "DIV r0, r0, r1\n"      #"DIV r0, r0, r1\n"
            elif "/" in line:
                assembly += "MUL r0, r0, r1\n"      #"MUL r0, r0, r1\n"
            else:
                assembly += "ST a, r1\n"            #"ST a, r1\n" 
        elif "goto" in line:
            assembly += "JMP L1\n"                  #"JMP L1\n"
        lineNumber += 1
    #print(variable)
    #print(label)
    return assembly



if __name__ == '__main__':
    main()