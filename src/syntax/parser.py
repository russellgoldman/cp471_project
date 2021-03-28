# Ref: https://ply.readthedocs.io/en/latest/ply.html
import ply.yacc as yacc
import grammar_rules

class Parser(object):
    # Build the parser using the grammar rules module
    def build(self, data, **kwargs):
        self.parser = yacc.yacc(module=grammar_rules, **kwargs)

        while True:
            try:
                s = input(data)
            except EOFError:
                break
            if not s:
                continue
            
            result = self.parse(s)
            print(result)
        

p = Parser()
p.build('Number num = 10;')
