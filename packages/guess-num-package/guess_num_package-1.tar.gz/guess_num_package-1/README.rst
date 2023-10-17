PyAnsys Technical Practical
###########################

This repository was generated from the `interview-practical
<https://github.com/pyansys/interview-practical>`_ template and contains a
simple exercise to evaluate candidates based on their ability to solve a
practical problem.

PyAnsys Overview
----------------
The PyAnsys project exposes Ansys technologies via libraries in the Python ecosystem. Each library provides clear, concise, and maintainable APIs. Useful Pythonic functions, classes, and plugins allow users to interact with targeted products and services in a high-level, object-orientated approach.

Development Standards
---------------------
Visit ``CONTRIBUTING.md`` for additional information on how to develop according to Ansys's PyAnsys standards. All development documentation can be found at `PyAnsys Developer’s Guide <https://dev.docs.pyansys.com/>`_.

Expected Outcome
----------------
This repository has several CI/CD (Continuous Integration/Continuous Deployment) failures.

Submit a pull request that fixes the following issues:

- [ ] Unit testing failures
- [ ] Raise code coverage above 95%
- [ ] Fix style check CI check
- [ ] Fix documentation failure CI check
- [ ] Rewrite this ``README.rst`` with installation and usage directions. Assume it can be installed from PyPI.


Evaluation Criteria
-------------------
You will be evaluated on:

- [ ] Ability to write unit tests that improve coverage.
- [ ] Documentation within the ``README.rst``
- [ ] Documentation and description of the pull request
- [ ] Ability to debug.
- [ ] Coding practice (e.g. multiple commits, local vs. remote testing)

Notes on Testing
~~~~~~~~~~~~~~~~
In the "Evaluation Criteria" section, the term "local vs. remote testing" refers to the difference between running tests on a developer's local machine versus running them on a remote server or continuous integration (CI) environment.

- **Local testing**: This involves running tests on your own computer, usually within your development environment. Local testing allows you to quickly identify and fix issues before pushing your changes to the repository. It is essential for ensuring your code changes do not introduce new bugs and that your code complies with the project's guidelines and standards. It is highly recommended that you perform local testing before submitting a pull request.

- **Remote testing**: This refers to running tests on a remote server, typically as part of a continuous integration (CI) pipeline. When you submit a pull request, the project's CI system will automatically execute tests on the proposed changes in a controlled environment. Remote testing helps to ensure that your changes are compatible with the project's codebase and that your contribution maintains the desired level of quality.

When evaluating your submission, we will consider your approach to testing. Candidates who demonstrate a thorough understanding of both local and remote testing and utilize these techniques effectively will be highly regarded. We encourage you to run tests locally before submitting a pull request and ensure that your changes pass all tests in the CI environment. This practice will not only improve the quality of your submission but also demonstrate your commitment to maintaining the high standards set by the PyAnsys project.

Installation
----------------
The ``importlib-metadata`` package requires Python 3.7.0 through Python 3.7.17

Local development using Git requires cloning: ``git clone https://github.com/ansys/python-interview-practial-Cjohns54.git``

Install Dependencies with correct versioning. Reference ``pyproject.toml``.

Getting Started
----------------
Usage: bin_search.py
~~~~~~~~

The bin_search.py module provides classes and functions to perform binary searches. Here's how you can use it:

.. code:: python

    import logging
    import ansys.interview.practical as pract

    # Configure logging (optional)
    LOG = logging.getLogger(__name__)
    LOG.setLevel("INFO")

    # Create a NumberRange instance
    number_range = pract.NumberRange(7, 1, 50)

    # Create a Searcher instance
    searcher = pract.Searcher(number_range)

    # Perform a binary search
    guess, num_guesses = searcher.search()

    # Output the results
    print("Guessed number:", guess)
    print("Number of guesses:", num_guesses)

In this example:

We import the necessary modules and configure logging (optional).

We create a NumberRange instance, specifying the target number and the range it can be in.

We create a Searcher instance, passing the NumberRange object for searching.

We call the search method on the Searcher instance to perform a binary search. It returns the guessed number and the number of guesses.

Finally, we output the guessed number and the number of guesses.

Usage: test_bin_tree.py
~~~~~~~~

Install Pytest: ``pip install pytest``

Run the tests: ``pytest test_bin_search.py``

Make sure you have the necessary dependencies installed and that your code is correctly structured to run the tests successfully.

License
-------
Licensed under the MIT license. Regardless, please don't fork or republish this repository. We'd rather not recreate the example.
