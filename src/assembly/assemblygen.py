class AssemblyGen(object):
    def generate(self, source):
        currentRegister = 0 
        assembly = ""
        source = source.split('\n')
        for line in source:      
            split = line.split()
            if "if" in line:
                shift = 0
                if ":" in split[0]:
                    shift += 1
                    assembly += "{}\n".format(split[0])
                assembly += "LD r{}, {}\n".format(currentRegister,split[1+shift])
                if ">" in line:
                    assembly += "LD r{}, {}\n".format(currentRegister+1,split[3+shift])
                    assembly += "BGT r{}, r{}, {}\n".format(currentRegister,currentRegister+1,split[5+shift])           #"BGT r0, r1,"  
                elif "<=" in line:
                    assembly += "LD r{}, {}\n".format(currentRegister+1,split[3+shift])
                    assembly += "BLE r{}, r{}, {}\n".format(currentRegister,currentRegister+1,split[5+shift])            #"BLE r0, r1," 
                elif "<" in line:
                    assembly += "LD r{}, {}\n".format(currentRegister+1,split[3+shift])
                    assembly += "BGT r{}, r{}, {}\n".format(currentRegister+1,currentRegister,split[5+shift])           #"BGT r1, r0,"
                elif ">=" in line:
                    assembly += "LD r{}, {}\n".format(currentRegister+1,split[3+shift])
                    assembly += "BLE r{}, r{}, {}\n".format(currentRegister+1,currentRegister,split[5+shift])            #"BLE r1, r0," 
                elif "==" in line:
                    assembly += "LD r{}, {}\n".format(currentRegister+1,split[3+shift])
                    assembly += "BGT r{}, r{}, {}\n".format(currentRegister,currentRegister+1,split[5+shift])            #"BGT r0, r1,"
                    assembly += "BGT r{}, r{}, {}\n".format(currentRegister+1,currentRegister,split[5+shift])            #"BGT r1, r0,"    
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