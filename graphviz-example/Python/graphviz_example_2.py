from graphviz import Digraph
dot = Digraph('graphviz_example_2', filename='graphviz_example_2')
dot.attr(label='A Simple Example\nby Chao', splines='ortho')

# oval shape for start and end
dot.attr('node', shape='oval')
# first argument is label, second argument is text on the node
dot.node('start', 'New Adventure')
dot.node('end', 'The End')

# solid box for action
dot.attr('node', shape='box', style='solid')
dot.node('mug', 'A mug is placed\nin front of you.')
dot.node('iced coffee', 'Iced Coffee')
dot.node('hot coffee', 'Hot Coffee')

# dotted box for thoughts or other stuff
dot.attr('node', shape='box', style='dotted')
dot.node('nice choice', 'Nice choice')
dot.node('good taste', 'Good taste')

# diamond shape for decisions
dot.attr('node', shape='diamond', style='solid')
dot.node('inside', 'What do you want to drink?')

dot.edge('start', 'mug')
dot.edge('mug', 'inside')
dot.edge('inside', 'iced coffee')
dot.edge('inside', 'hot coffee')
dot.edge('iced coffee', 'nice choice')
dot.edge('hot coffee', 'good taste')
dot.edge('nice choice', 'end')
dot.edge('good taste', 'end')

dot.view()