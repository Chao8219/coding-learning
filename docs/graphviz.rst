==========
7 Graphviz
==========

.. image:: https://img.shields.io/badge/python-3.6-blue.svg

The graphviz is a powerful tool to plot diagrams from source code. 
You can use different engines to generate diagrams as pics or pdf in 
graphviz.

The installation is simple and strightforward: 
go to `download <https://graphviz.gitlab.io/download/>`_, find your 
OS and do as they said.

7.1 DOT Language
================

DOT language is simple. 
You could go `help-doc <http://melp.nl/2013/08/
flow-charts-in-code-enter-graphviz-and-the-dot-language/>`_ to find a 
easy-handy example to plot flowchart.

As is written in the example, you can use any editor to write down 
the code, and generate the format you want by command in terminal: 
::

    dot -Tpng -o example.png example.gv

7.2 Python
==========

You can also use python to generate dot file. 
See `pypi graphviz <https://pypi.org/project/graphviz/>`_ for more help.

7.2.1 Using Graphviz on Windows
-------------------------------

This is a special note for using Graphviz on Windows.
For me, using graphviz on Ubuntu is relatively easy since all I did was 
to install graphviz package inside the conda env. 
It becomes a little bit different while I am using Win 10 for this repo.
So here are some tips for myself in case I need to do this again.

1. :code:`conda install python-graphviz`

2. :code:`pip install graphviz`

3. "Control Panel" -> "System and Security" -> "System" ->
   "Advanced System Setting" -> "Environment Variables" -> 
   Edit "Path" under "System variables" -> add new path 
   "C:\Users\the_path_to_Anaconda3\envs\my_env\Library\bin
   \graphviz"

After adding path up, please re-open terminals. This is very important.

7.2.2 Creating Flowchart by Python Script
-----------------------------------------

One could write a simple example in python as follow:
::

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

Once the script is created, one could simply run: 
:code:`python your_flowchart.py`, then the pdf file will be generated.