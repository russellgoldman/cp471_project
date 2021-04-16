from typing import List, Dict

class SymbolTable:    
    class Node:
        class Record:
            # Record initialization
            def __init__(self, symbol: str, symbol_type: str, scope: str):
                self.symbol:        str     = symbol
                self.symbol_type:   str     = symbol_type
                self.scope:         str     = scope
            
            # def print_str(self):
            #     out = ''
            #     out += 'symbol: {}\n'.format(self.symbol)
            #     out += 'symbol_type: {}\n'.format(self.symbol_type)
            #     out += 'scope: {}\n'.format(self.scope)
            #     print(out)

        # Node initialization
        def __init__(self, parent=None):
            # records -> [symbol, Record]
            self.records:   Dict[str, self.Record]  = {}
            # children -> [scope, Node]
            self.children:  Dict[str, self.Node]    = {}
            self.parent:    self.Node               = parent

        # Node methods
        def add_record(self, symbol: str, symbol_type: str = None, scope: str = None):
            self.records[symbol] = self.Record(symbol, symbol_type, scope)

        def add_child(self, scope: str, child):
            self.children[scope] = child

        def add_parent(self, parent):
            self.parent = parent

        def modify_record(self, symbol: str, symbol_type: str = None, scope: str = None):
            record = self.records[symbol]
            record.symbol = symbol
            if symbol_type != None: record.symbol_type = symbol_type
            if scope != None: record.scope = scope

    # SymbolTable methods
    def __init__(self):
        self.root:  Node        = self.Node()
        self.scopes: Dict       = {}
        self.scopes['global']   = self.root

    def get_scope_node(self, scope: str):
        return self.scopes[scope]

    # def __str__(self):
    #     current = root
    #     current.


# Create Symbol Table
s = SymbolTable()
# Get the root global node in the table
global_node = s.get_scope_node('global')

global_node.add_record('number', None, 'global')
for_1_node = s.Node(global_node)
if_1_node = s.Node(global_node)

for_1_node.add_record('i', None, 'for_1')
if_1_node.add_record('i', None, 'if_1')