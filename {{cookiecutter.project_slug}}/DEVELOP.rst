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

This section will explain how to initially set up the development environment for your project using the 
``pip`` package manager and a virtual environment.

Why Virtual Environments in Python?
===================================

To explain what a virtual environment is and why it is important it makes sense to first explain the python global 
environment. When installing python on your system it operates on a single global environment by default. Whenever 
a package is installed using 

.. code-block:: console

    pip3 install some_package

for example, all the code from this package is installed into a certain folder on your system 

Setting up the virtual environment
==================================

As previously discussed it is very recommended to set up a separate virtual environment for each project you are 
working on to avoid version conflicts.

This can be done manually by using the ``venv`` python package. First make sure that the venv python package is 
installed like this:

.. code-block:: console

    sudo apt install python3-venv

Then, simply move into the top level folder of your project and create the virtual env folder like this:

.. code-block:: console

    python3 -m venv venv

This will create a new folder called ``venv``. You can now *activate* this environment with this command:

.. code-block:: console

    source venv/bin/activate

This will modifiy your current terminal session in such a way that whenever you write commands like ``python3`` or ``pip3`` 
from that point onwards it will not use the global environment installed on your system but rather the local instance 
of the python environment contained in the ``venv`` folder.

Installing your existing code
=============================

After you have set up and activated your virtual environment, you can use the python related commands as before - the only 
difference being that they now use the local versions of the virtual environment.

That means, for example, that you can now start to add your development dependencies such as pytorch for example.

.. code-block:: console 

    pip3 install torch

One important step however is to locally install your own project code, such that all the internal imports will be working 
correctly. This is done by switching into the top-level folder of your project (the one that contains the ``pyproject.toml`` file)
and executing the following command:

.. code-block:: console

    cd {{ cookiecutter.project_slug }}
    pip3 install -e .[dev]

This command warrants some further explanations:

- the dot ``.`` is the linux syntax for "current folder", which tells pip to install the local files.
- The ``-e`` flag puts the installation into *editable* mode. Instead of installing the package by making a copy, it uses 
  those exact files in the folder directly. This way you won't have to reinstall the package every time to reflect 
  changes in the code.
- the ``[dev]`` addition will install the optional development dependencies as well. These will be third party packages that 
  are required for development, such as ``pytest`` for unittesting, but don't make sense to include as a general dependency.

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

Based on this structure you would do the following imports for example:

.. code-block:: python

    # main.py
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
    from {{ cookiecutter.project_slug }}.models.gnn import GcnModel

=================================
📦 Releasing your Package to PyPi
=================================

At some point the code of your project perhaps evolves into some general functionality that some other people could 
potentially benefit from as well. If that is the case, it might make sense to publically release your package to the 
official python package repository PyPi_. By doing this other people will be able to install your package very 
conveniently via pip like this:

.. code-block:: console

    pip3 install {{ cookiecutter.project_slug }}

The following sections will explain how to achieve this.

Registering with PyPi
=====================

The first thing you'll have to do is to register a new account with PyPi_ online: https://pypi.org/account/register/

It is advised to note down your username and password as you'll need them later on.

Publishing with Poetry
======================

On your local system, you can use the ``poetry`` command line interface to publish your package. If you've followed the 
installation instructions above, Poetry_ should have already been installed to your virtual environment as a development 
dependency. However, you make sure that it is installed by running:

.. code-block:: console

    pip3 install poetry

**Build the code.** The first step you'll need to do prior to publishing is to actually build your code. This can be done 
by running the ``build`` command like this:

.. code-block:: console

    poetry build

**Publish the code.** Then you can publish the code using the ``publish`` command. This is where you'll need to provide the 
username and password for your PyPi_ account.

.. code-block:: console

    poetry build --username='{pypi_username}' --password='{pypi_password}'

=====================
🕰️ Package Versioning
=====================

One thing that will be important to keep track of - especially if you are planning to release your code - 
is the versioning of your code. To publish your code, it is required that you provide a unique version identifier.
Once published, it is also not possible to then modify that code again - the only way to modify the published code 
is to actually publish a new version.

Even if you don't intend to release the code, it might still make sense to keep track of the version for your 
own sake. The following sections will introduce the concept of `Semantic Versioning`_ explained.

What is Versioning?
===================

One of the most commong versioning schemes is called `Semantic Versioning`_. You can read up on it on the 

Start Developing Version Zero
=============================

The semantic versioning scheme presents a bit of a problem in cases...

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

**TO BE DONE**

.. _reStructuredText: https://www.writethedocs.org/guide/writing/reStructuredText/
.. _README: https://www.makeareadme.com/
.. _Poetry: https://python-poetry.org/
.. _PyPi: https://pypi.org/
.. _`Semantic Versioning`: https://semver.org/