from graphviz import Digraph

dot = Digraph()

dot.attr('node', shape='box', style='rounded')
dot.node('start', 'Start')
dot.node('end', 'End')

dot.attr('node', shape='doublecircle')
dot.node('A', 'Coffee is great')
dot.node('B', 'I concur')

dot.edge('start', 'A')
dot.edge('A', 'B')
dot.edge('B', 'end')

dot.view()
