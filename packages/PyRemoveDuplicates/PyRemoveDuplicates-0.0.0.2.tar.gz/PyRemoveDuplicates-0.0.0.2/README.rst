PyRemoveDuplicates
===================

**PyRemoveDuplicates** is a Python package that simplifies the process of removing duplicate elements from a list or array. It offers a straightforward and efficient solution for scenarios where data deduplication is required.

Installation
------------

You can install **PyRemoveDuplicates** using pip, the Python package manager. Open your terminal or command prompt and run the following command:

.. code:: bash

    pip install PyRemoveDuplicates


After installing the package, you can use it in your Python scripts as follows:

.. code:: python

    from PyRemoveDuplicates import Unique

    # Create a list with duplicate elements
    my_list = [1, 2, 2, 3, 4, 4, 5]

    # Use the remove_duplicates function to remove duplicates
    unique_list = Unique(my_list)

    # Print the unique list
    print(unique_list)

License
-------

This project is licensed under the `MIT License <LICENSE>`__.