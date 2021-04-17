from typing import List, Dict, Set

class SymbolTable:    
    class Node:
        class Record:
            # Record initialization
            def __init__(self, symbol: str, symbol_type: str, node):
                self.symbol:        str     = symbol
                self.symbol_type:   str     = symbol_type
                self.node:          str     = node

        # Node initialization
        def __init__(self, scope: str, parent=None):
            self.scope:     str                     = scope
            # records -> [symbol, Record]
            self.records:   Dict[str, self.Record]  = {}
            # children -> [scope, Node]
            self.children:  Dict[str, self.Node]    = {}
            self.parent:    self.Node               = parent

        # Node methods
        def add_record(self, symbol: str, symbol_type: str=None):
            self.records[symbol] = self.Record(symbol, symbol_type, self)

        def _add_child(self, scope: str, child):
            self.children[scope] = child

        def _add_parent(self, parent):
            self.parent = parent

        def modify_record(self, symbol: str, symbol_type: str=None, scope: str=None):
            record = self.records[symbol]
            record.symbol = symbol
            if symbol_type != None: record.symbol_type = symbol_type
            if scope != None: record.scope = scope

    # SymbolTable methods
    def __init__(self):
        self.root:  Node                    = self.Node('global')
        self.scopes: Dict[str, self.Node]   = {}
        self.scopes['global']               = self.root

    def create_node(self, scope: str, parent=None):
        node = self.Node(scope, parent)
        if parent != None:
            parent._add_child(scope, node)
            node._add_parent(parent)
        self.scopes[scope] = node
        return node

    def get_node_by_scope(self, scope: str) -> Node:
        return self.scopes[scope]
    
    def clear(self):
        for scope in self.scopes.items():
            scope_name = scope[1]
            node = scope[1]
            node.records = {}
            node.children = {}

            if scope_name != 'global':
                del scope

    def print_node(self, out: str, current: Node):
        out += '  Node: {}\n'.format(current.scope)
        if current.parent != None:
            out += '  Parent: {}\n'.format(current.parent.scope)
        out += ' {}\n'.format('-' * 47)
        
        # iterate through all records in the current node
        out += '| Symbol\t\tType\t\tScope\t|\n'
        out += '| ------\t\t----\t\t-----\t|\n'
        for pair in current.records.items():
            record = pair[1]

            tabs = 3
            if len(record.symbol) > 5:
                tabs = 2

            out += '| {}{}{}\t\t{}\t|\n'.format(
                record.symbol,
                '\t' * tabs,
                record.symbol_type,
                record.node.scope
            )
        out += ' {}\n\n\n'.format('-' * 47)
        
        return out

    def __str__(self):
        # Perform BFS to print table
        seen: Set = set()
        to_visit = [self.root]
        seen.add(self.root)
        out = ''

        while len(to_visit) != 0:
            current = to_visit.pop(0)
            out = self.print_node(out, current)

            for child in current.children.items():
                if child[1] not in seen:
                    to_visit.append(child[1])
                    seen.add(child[1])

        return out


# Create Symbol Table
symbol_table = SymbolTable()

# TESTING
# # Get the root global node in the table
# global_node = s.get_node_by_scope('global')

# global_node.add_record('number', None)
# for_1_node = s.create_node('for_1', global_node)
# if_1_node = s.create_node('if_1', global_node)

# for_1_node.add_record('i', None)
# if_1_node.add_record('i', None)
# if_1_node.add_record('n', 'Number')

# if_2_node = s.create_node('if_2', for_1_node)
# if_2_node.add_record('s', 'String')

# print(s)