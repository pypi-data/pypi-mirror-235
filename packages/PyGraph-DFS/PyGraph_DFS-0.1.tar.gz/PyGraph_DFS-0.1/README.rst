PyGraph_DFS Package
===================

Overview
--------

PyGraph_DFS is a Python package that provides a straightforward and efficient way to perform Depth-First Search (DFS) on a graph. It is a versatile tool that can be used in various scenarios where graph traversal and exploration are necessary.

Installation
------------

You can install PyGraph_DFS using pip:

.. code-block:: shell

   pip install PyGraph_DFS

Usage
-----

After installing the package, you can use it in your Python scripts as follows:

.. code-block:: python

   from PyGraph_DFS import GraphDFS

   # Create a graph instance
   my_graph = GraphDFS()

   # Add edges to the graph
   my_graph.add_edge("A", "B")
   my_graph.add_edge("B", "C")
   my_graph.add_edge("B", "D")
   my_graph.add_edge("D", "E")

   # Perform Depth-First Search (DFS)
   visited_nodes = my_graph.dfs("A")

   # Print the visited nodes
   print(visited_nodes)

Example Output
--------------

The above code will produce the following output:

.. code-block:: python

   ['A', 'B', 'C', 'D', 'E']


License
-------

This project is licensed under the MIT License. See the `LICENSE <LICENSE>`_.
