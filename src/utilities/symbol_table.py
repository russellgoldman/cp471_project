from typing import Dict
    
class SymbolTable:
    class SymbolTableEntry:
        def __init__(self):
            # name and key are synonymous in this context
            self.symbol:    str             = None
            self.scope:     str             = None
            self.value:     str|int|float   = None

        def set_symbol(self, symbol):
            self.symbol = symbol
        
        def set_scope(self, scope):
            self.scope = scope
        
        def set_value(self, value):
            self.value = value


    table: Dict = {}

    def create_entry(self, name):
        if not self.contains(name):
            self.table[name] = self.SymbolTableEntry()
            return
        
        raise ValueError("The name {name} already exists, could not create entry".format(name=name))


    def get_entry(self, name):
        if self.contains(name):
            return self.table[name]
        
        raise ValueError("The name {name} does not exist, could not get entry".format(name=name))
        

    def set_symbol(self, name, symbol):
        if self.contains(name):
            self.table[name].set_symbol(symbol)
            return
        
        raise ValueError("The name {name} does not exist, could not alter symbol entry".format(name=name))


    def set_scope(self, name, scope):
        if self.contains(name):
            self.table[name].set_scope(scope)
            return
        
        raise ValueError("The name {name} does not exist, could not alter scope entry".format(name=name))


    def set_value(self, name, value):
        if self.contains(name):
            self.table[name].set_value(value)
            return

        raise ValueError("The name {name} does not exist, could not alter value entry".format(name=name))


    def contains(self, name):
        return self.table.get(name) != None


# Preliminary testing
s = SymbolTable()
try:
    s.get_entry('my_str')
except ValueError as e:
    print("Recovered from error: ", end="")
    print(e)

s.create_entry('my_str')
try:
    s.create_entry('my_str')
except ValueError as e:
    print("Recovered from error: ", end="")
    print(e)

s.set_symbol('my_str', 'str')
s.set_symbol('my_str', 'int')
print(s.get_entry('my_str').symbol)