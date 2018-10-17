from graphviz import Diagraph

dot = Diagraph()

dot.attr('node', shape='box', style=rounded)
dot.node('start', 'Start')
dot.node('end', 'End')

dot.attr('node', shape='doublecircle')
dot.node('A', 'Coffee is great')
dot.node('B', 'I concur')

dot.edge(['start','A'], ['A','B'], ['B','end'])

dot.view()