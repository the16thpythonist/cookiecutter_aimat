.. image:: /aimat_logo.png
    :alt: The AIMAT group logo
    :width: 50%
    :align: center

=============================
👩‍🔬 AIMAT Project Cookiecutter
=============================

*Welcome!*

So you have decided to do a thesis project with with the AIMAT_ group. This README file will walk you through the 
process of creating a basic structure of the code that you'll be using to conduct the computational experiments for 
your project. 

This structure will be created by the cookiecutter_ 🍪 template that is implemented in this repository. cookiecutter_ 
is a project intended to simplify the setup of python projects in general by providing an interface to instantiate 
and customize project templates found on the web.

    Please note that this template is just a *recommendation*. If you want to built the code structure completely 
    then you are free to do so as well. However, this template exists to make it easier for you! At first it may 
    seem daunting because there are so many files, but you'll see that most of them are just necessary boilerplate
    and you'll be able to ignore most of them.

===========
🔥 Features
===========

Before we get right into how to instantiate this template for your own project, 
here are the most notable features that this template provides for you.

- **best practices for re-use.** Most importantly, this template will set up your project according to a series of 
  coding best practices that will make it easier for the code to remain useful to the group even after you finish
  your project!
- **ready for documentation.** The template will already create a large portion of your own project's ``README.rst`` file 
  which will be the starting point of your project documentation.
- **ready for release.** The template sets up the necessary folder structure and configuration files which are required 
  to publish the code to the python package index to make it installable via ``pip`` for example.
- **ready for unit testing.** The template includes some useful utilities in case you want to get started with 
  unittesting_ your code.

==================
🚀 Getting Started
==================

To get started with your project setup, first make sure that you have python and pip installed on your system.

.. code-block:: console

    python3 --version

Then install cookiecutter_ like this:

.. code-block:: console

    sudo apt install cookiecutter

You can then use the cookiecutter command line interface to locally instantiate this template by using the URL of the 
github repository.

.. code-block:: console

    cookiecutter https://github.com/the16thpythonist/cookiecutter_aimat

**Configuration.** executing the above command will present you with a series of input prompts in which you are able to 
enter data to customize the code generated for your project.

The following table provides an overview of the various prompts and brief descriptions of their purpose.

==================================  =====================================================================================================
prompt                              description               
==================================  ===================================================================================================== 
``project_slug``                    The name of your project. For one thing, this will be the name of the project folder that will be 
                                    created through this template. It will also be the name of your github repository.
                                    Choose this name wisely, as it will be hard to change later on. For that purpose see the notes 
                                    on naming conventions further down below. 
``author_name``                     Your first and last name. This will serve as contact information for the potential relase of
                                    the package.
``author_email``                    Your email address. This will be part of your contact information for the package.
``version``                         The version with which your project will be initialized. For this it is recommended to keep the 
                                    default value of ``0.1.0``. You'll be able to increment the version as you start developing the 
                                    project.
``license``                         In this step, the prompt will ask you to decide between a few of the most common options for 
                                    software licenses. You can read up on `software licences`_ to find out what suits your project best.
                                    However, the MIT license (default) is often a good choice.
==================================  =====================================================================================================

==============
🐾 First Steps
==============

After the above instantiation of the repository was completed sucessfully, it will have created a new folder with the name 
given as ``project_slug``.

As a first step, it makes sense to carefully read the ``DEVELOP.rst`` file. It contains explanations about the general project 
structure, further references to online material and other useful information!

==============================
🖊️ Notes on Naming Conventions
==============================

One important step in the development of your project is to create a name for your code package. Here, it makes sense to spend some 
time to come up with good name. Especially, if you are planning to release your code for other people to use, it is important to 
choose a name which other people can understand easily.

**use snake case.** To stay consistent with the common python naming convention, create a name in *snake case* which means 
only consisting of *lower case characters* and using *underscores* as whitespaces.

.. code-block:: bash

    LanguageModelsAre-GREAT                         # Bad
    language_models_are_great                       # Better

**be descriptive.** Make sure that the name is descriptive of your project and that it can also be understood by others.

.. code-block:: bash

    my_thesis_project                               # Bad
    crystal_gnn_benchmarks                          # Better

**be concise.** On the other hand you also don't want your project name to be a whole sentence because you'll end up writing 
that name a lot in the import statments. However, be careful not to lean too much into abbreviations lest the name becomes hard 
to understand for others.

.. code-block:: bash

    benchmark_framework_for_gnns_and_crystals       # Bad
    crystal_gnn_benchmarks                          # Better
    crstl_gnn_bench                                 # Also OK
    cgnnb                                           # Bad

==========
📨 Contact
==========

If you have any other questions specifically regarding this template, feel free to contact: 
`jonas.teufel@kit.edu <jonas.teufel@kit.edu>`_

.. _AIMAT: https://aimat.iti.kit.edu/
.. _cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _unittesting: https://medium.com/interleap/intro-to-unit-tests-f2b7750c2d3c
.. _`software licenses`: https://choosealicense.com/licenses/