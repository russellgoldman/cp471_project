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
name = 'my_str'
s = SymbolTable()
try:
    s.get_entry(name)
except ValueError as e:
    print("Recovered from error: ", end="")
    print(e)

s.create_entry(name)
try:
    s.create_entry(name)
except ValueError as e:
    print("Recovered from error: ", end="")
    print(e)

s.set_symbol(name, 'str')
s.set_symbol(name, 'int')
s.set_value(name, 3.01)
print(s.get_entry(name).symbol)
print(s.get_entry(name).value)


"""
Number number = 0;
for(Number i = 0; i < 10; i++) {
    number = number + i;

    if (i > 5) {
        Number n = 5
    }

    number = number + n         //  Semantic Analysis returns an error
                                    n is not defined
}


0:
Symbol      Type        Scope
number      Number      Global

|                                 |

1:
Symbol      Type        Scope           Symbol      Type        Scope
i           Number      For_1           n           Number      If_1


"""