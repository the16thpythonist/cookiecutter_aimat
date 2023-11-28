.. image:: https://github.com/the16thpythonist/cookiecutter_aimat/blob/master/aimat_logo.png
    :align: middle
    :width: 50%

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

    pip3 install cookiecutter

You can then use the cookiecutter command line interface to locally instantiate this template by using the URL of the 
github repository.

.. code-block:: console

    cookiecutter https://github.com/the16thpythonist/cookiecutter_aimat

**Configuration.** executing the above command will present you with a series of input prompts in which you are able to 
enter data to customize the code generated for your project.

.. 
    https://tableconvert.com/restructuredtext-generator

The following table provides an overview of the various prompts and brief descriptions of their purpose.

 ================== ========================== 
  prompt             description               
 ================== ========================== 
  ``project_slug``   The name of your project  

==========
📨 Contact
==========

If you have any other questions specifically regarding this template, feel free to contact: 
`jonas.teufel@kit.edu <jonas.teufel@kit.edu>`_

=======================
📚 Additional Resources
=======================

In this section we provide a number of additional resources you can read on your own.

🖥️ Python Programming
=====================

- Learn Python the Hard Way

.. _AIMAT: https://aimat.iti.kit.edu/
.. _cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _unittesting: https://medium.com/interleap/intro-to-unit-tests-f2b7750c2d3c