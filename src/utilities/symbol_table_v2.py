from typing import List, Dict, Set
import pdb

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
        def __init__(self, scope: str, parent=None):
            # records -> [symbol, Record]
            self.scope:     str                     = scope
            self.records:   Dict[str, self.Record]  = {}
            # children -> [scope, Node]
            self.children:  Dict[str, self.Node]    = {}
            self.parent:    self.Node               = parent

        # Node methods
        def add_record(self, symbol: str, symbol_type: str=None, scope: str=None):
            self.records[symbol] = self.Record(symbol, symbol_type, scope)

        def add_child(self, scope: str, child):
            self.children[scope] = child

        def add_parent(self, parent):
            self.parent = parent

        def modify_record(self, symbol: str, symbol_type: str=None, scope: str=None):
            record = self.records[symbol]
            record.symbol = symbol
            if symbol_type != None: record.symbol_type = symbol_type
            if scope != None: record.scope = scope

    # SymbolTable methods
    def __init__(self):
        self.root:  Node        = self.Node('global')
        self.scopes: Dict       = {}
        self.scopes['global']   = self.root

    def create_node(self, scope: str, parent=None):
        node = self.Node(scope, parent)
        if parent != None:
            parent.add_child(scope, node)
            node.add_parent(parent)
        self.scopes[scope] = node
        return node

    def get_node_by_scope(self, scope: str):
        return self.scopes[scope]

    def print_node(self, out: str, current: Node):
        out += ' {}\n'.format('-' * 47)
        out += '| Parent Node: {}\t\t\t\t|\n'.format(current.parent.scope)
        out += ' {}\n'.format('-' * 47)
        
        # iterate through all records in the current node
        for pair in current.records.items():
            record = pair[1]

            tabs = 3
            if len(record.symbol) > 5:
                tabs = 2

            out += '| Symbol\t\tType\t\tScope\t|\n'
            out += '| ------\t\t----\t\t-----\t|\n'
            out += '| {}{}{}\t\t{}\t|\n'.format(
                record.symbol,
                '\t' * tabs,
                record.symbol_type,
                record.scope
            )
            out += ' {}\n'.format('-' * 47)
        
        return out

    def __str__(self):
        # Perform BFS to print table
        seen: Set = set()
        to_visit = [self.root]

        out = '\n'

        while len(to_visit) != 0:
            current = to_visit.pop(0)
            # pdb.set_trace()
            if not current.scope in seen:
                # pdb.set_trace()
                out += self.print_node(out, current)
                seen.add(current.scope)
            
            for child in current.children.items():
                # pdb.set_trace()
                to_visit.append(child[1])

        return out


# Create Symbol Table
s = SymbolTable()
# Get the root global node in the table
global_node = s.get_node_by_scope('global')

global_node.add_record('number', None, 'global')
for_1_node = s.create_node('for_i', global_node)
if_1_node = s.create_node('if_1', global_node)

for_1_node.add_record('i', None, 'for_1')
if_1_node.add_record('i', None, 'if_1')

print(s)