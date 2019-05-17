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
See `here <https://pypi.org/project/graphviz/>`_ to see how to use it.

You can use anaconda to run the script.
Please notice that the graphviz is installed under pip, not conda.