===========================
Information for Development
===========================

The structure that was automatically created for your structure will seem daunting at first, but 
this file will walk you through the most imporant parts and aspects of this structure step-by-step.

====================
📁 Project Structure
====================

Here is an overview of the project structure.

- ``DEVELOP.rst`` - You are here. This file provides additional information for the development of 
  your project.
- ``README.rst`` - This will serve as other peoples entry point to your project. The ``rst`` file 
  extension of this file indicates the usage of reStructuredText_, which is a specific markup language 
  to produce text files that can be rendered with richer formatting. Such a README_ file will actually 
  be recognized and rendered when someone opens a project's github page.
- ``pyproject.toml`` - This file contains the configuration about the package in general. In this file 
  you'll have to, for example, list all the third party packages that your own code depends on with their 
  specific version so that the same environment can be recreated on other's systems as well.
- ``{{ cookiecutter.project_slug }}/`` - This will be the folder that should contain all your **actual code**
    - ``utils.py`` - Module containing utility functions that can't be associated with a more fitting module name.
    - ``testing.py`` - Module containing utility functions for unittesting purposes.
    - ``VERSION`` - A plain text file which contains only the version string of the project.
- ``tests/`` - Contains all the code for unittesting.

==================================
🚀 Setting Up with Poetry and Venv
==================================

This section will explain how to initially set up the development environement for your project. For this 
purpose two alternatives will be presented: Either setting up with ``poetry`` or ``pip``. Poetry_ is a python 
package manager that was rather recently introduced as an alternative to pip and conda. For various technical 
and usability reasons poetry is nowadays the recommended choice for python package management.

However, regardless of which option you decide on, it makes sense to discuss the importance of python *virtual
environments* first, as they will be used in either method.

Why Virtual Environments in Python?
-----------------------------------

To explain what a virtual environment is and why it is important it makes sense to first explain the python global 
environment. When installing python on your system it operates on a single global environment by default. Whenever 
a package is installed using 

.. code-block:: console

    pip3 install some_package

for example, all the code from this package is installed into a certain folder on your system 

(Recommended) Setting up with poetry
====================================

As the first step you'll have to install the Poetry_ python package globally on your system.

.. code-block:: console

    pip3 install poetry

After the installation is complete, you'll be able to use the ``poetry`` terminal commands. To set up your project 
first navigate into your projects top level directory (the one containing the ``pyproject.toml``) file and then execute 
the poetry 

.. code-block:: console

    cd {{ cookiecutter.project_slug }}



(Alternative) Setting up with pip
=================================

Setting up the virtual environment
----------------------------------

As previously discussed it is very recommended to set up a separate virtual environment for each project you are 
working on to avoid version conflicts.

This can be done manually by using the ``venv`` python package. Simply move into the top level folder of your project 
and create the virtual env folder like this:

.. code-block:: console

    python3 -m venv venv

This will create a new folder called ``venv``. You can now *activate* this environment with this command:

.. code-block:: console

    source venv/bin/activate

This will modifiy your current terminal session in such a way that whenever you write commands like ``python3`` or ``pip3`` 
from that point onwards it will not use the global environment installed on your system but rather the local instance 
of the python environment contained in the ``venv`` folder.

Installing your existing code
-----------------------------

After you have set up and activated your virtual environment, you can use the python related commands as before - the only 
difference being that they now use the local versions of the virtual environment.

That means, for example, that you can now start to add your development dependencies such as pytorch for example.

.. code-block:: console 

    pip3 install torch

One important step however is to locally install your own project code, such that all the internal imports will be working 
correctly. This is done by switching into the top-level folder of your project (the one that contains the ``pyproject.toml`` file)
and executing the following command:

.. code-block:: console

    pip3 install -e .

In this case the ``-e`` flag is of special importance, which indicates to install the local code in *editable* mode. 
without this flag you'd have to reinstall the package every time the code is changed.

Configuring your IDE
====================

The previous explanations cover the use case in which one wants to manually execute the scripts from the command line. However, 
this is increasingly not how software development is conducted nowadays anymore. Instead, you'll likely want to use 
an *integrated development environment* (IDE) application.

When using an IDE, it is important to configure it to use the correct python executable of the virtual environment that you 
have just created - rather than the global one.

=========================
📦 Using Absolute Imports
=========================

Another important aspect to discuss - and one that is often a source of a lot of confusion - is best practices related to 
the python import system. This section will discuss the do's and don'ts of importing your own modules in the given 
project structure.

Avoid Relative Imports
======================

To motivate the use of absolute imports, this section will address some problems with the commonly used alternative - *relative imports*.

When one starts working with python one usually works with one or two isolated scripts and one doesn't give much thought to 
how the import system works. So at the beginning, a small project will most likely look something like this:

.. code-block:: text 

    project/
    ├─ utils.py
    ├─ models.py
    ├─ main.py

.. code-block:: python

    # models.py
    from models import Model
    from utils import train_model

    model = Model()
    train_model(model)

Now consider the following structure of a more mature project instead:

.. code-block:: text

    project/
    ├─ models/
    │  ├─ gnn.py
    │  ├─ dnn.py
    │  ├─ ...
    ├─ utils/
    │  ├─ training.py
    │  ├─ testing.py
    ├─ main.py

In this case it would be possible to import ``training.py`` from within ``main.py`` but you'd run into problems when 
trying to import ``training.py`` from ``gnn.py`` for example.

Another general problem with relative imports is that they can cause naming collisions with existing 
third-party libraries. Imagine you have your own module called ``utils.py`` and somewhere 

Use Absolute Imports Instead
============================

For the previously presented reasons, it is recommended to use absolute importing right away. Absolute importing is also a hard 
requirement if you intend to release your project to the python package repository.

For absolute importing you simply have to have to add the name of your project/package to the front of each import statement 
and then write out the full "path" towards the desired module you want to import. For the project structure above, the 
mentioned imports could simply be achieved like this:

.. code-block:: python

    # gnn.py
    from project.utils.training import train_model


In a more concrete example for your own project it would work something like this:

.. code-block:: python

    # concrete examples of absolute imports
    import {{ cookiecutter.project_slug }}.visualization.molecules as vis
    from {{ cookecutter.project_slug }}.models.gnn import GcnModel

=====================
🕰️ Package Versioning
=====================

One thing that is important to keep in mind

======================
🌐 Working with Github
======================

It is recommended to maintain a github repository.

Create Local Git Repository
===========================

Connect with Github
===================

(Optional) Avoid Two-Factor Authentication
==========================================

=======================
📚 Additional Resources
=======================

This section compiles a number of useful resources that might be helpful during development


.. _reStructuredText: https://www.writethedocs.org/guide/writing/reStructuredText/
.. _README: https://www.makeareadme.com/
.. _Poetry: https://python-poetry.org/