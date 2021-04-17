import unittest
import sys, os
import re


def main():

    source_f = open('./given/testcase1.txt', 'r')
    source = source_f.read()
    source_f.close()

    print(codegen(source))

def codegen(source):
    registerCount = 0
    currentRegister = 0 
    assembly = ""
    lineNumber = 0
    labelCount = 1
    label = []
    variable = []
    dictionary = {}
    source = source.split('\n')
    for line in source:      
        split = line.split()
        for word in split:
            if re.search(r'([A-Za-z]|_)([A-Za-z]|[0-9]|_)*', word):#len(word) > 1:
                if  word[0] == "L"  and ":" not in word :
                    label.append(word)
                elif word != 'goto' and word != 'if' and word not in variable and ":" not in word :
                    variable.append(word)  
        if "if" in line:
            shift = 0
            if ":" in split[0]:
                shift += 1
                assembly += "{}\n".format(split[0])
            assembly += "LD r{}, {}\n".format(currentRegister,split[1+shift])
            if ">" in line:
                assembly += "BGT r0, r1,"            #"BGT r0, r1,"  
            elif "<=" in line:
                assembly += "LD r{}, {}\n".format(currentRegister+1,split[3+shift])
                assembly += "BLE r{}, r{}, {}\n".format(currentRegister,currentRegister+1,split[5+shift])            #"BLE r0, r1," 
            elif "<" in line:
                assembly += "BGT r1, r0,"            #"BGT r1, r0,"
            elif ">=" in line:
                assembly += "BLE r1, r0,"            #"BLE r1, r0," 
            elif "==" in line:
                assembly += "BGT r0, r1,"            #"BGT r0, r1,"
                assembly += "BGT r1, r0,"            #"BGT r1, r0,"    
            # if "goto" in line:
            #     assembly += " L1\n"
        elif "=" in line:
            shift = 0
            if ":" in split[0]:
                shift += 1
                assembly += "{}\n".format(split[0])
            assembly += "LD r{}, {}\n".format(currentRegister,split[2+shift])   
            if "+" in line:
                assembly += "LD r{}, {}\n".format(currentRegister+1,split[4+shift])
                assembly += "ADD r{}, r{}, r{}\n".format(currentRegister,currentRegister,currentRegister+1)      #"ADD r0, r0, r1\n" 
            elif "-" in line:
                assembly += "LD r{}, {}\n".format(currentRegister+1,split[4+shift])
                assembly += "SUB r{}, r{}, r{}\n".format(currentRegister,currentRegister,currentRegister+1)        #"SUB r0, r0, r1\n"
            elif "*" in line:
                assembly += "LD r{}, {}\n".format(currentRegister+1,split[4+shift])
                assembly += "MUL r{}, r{}, r{}\n".format(currentRegister,currentRegister,currentRegister+1)        #"DIV r0, r0, r1\n"
            elif "/" in line:
                assembly += "LD r{}, {}\n".format(currentRegister+1,split[4+shift])
                assembly += "DIV r{}, r{}, r{}\n".format(currentRegister,currentRegister,currentRegister+1)        #"MUL r0, r0, r1\n"                      
            assembly += "ST {}, r{}\n".format(split[0+shift],currentRegister)            #"ST a, r1\n"      
        elif "goto" in line:
            assembly += "JMP {}\n".format(split[1])                  #"JMP L1\n"
        elif ":" in line:
            assembly += "{}\n".format(split[0])

    return assembly



if __name__ == '__main__':
    main()