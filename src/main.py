from ez_parser import Parser

source = "Number num = 10;"
p = Parser()
p.build()
p.parse(source)
print(given_tree)