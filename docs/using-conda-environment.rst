=========================
8 Using Conda Environment
=========================

Note: this page is moved from my **ml-101** repo directly.

This doc is for Ubuntu/Linux only, for now.

One could install conda at `anaconda.com <https://www.anaconda.com/>`_. 
Once finished installation, you can edit .bashrc file in your home 
directory, and comment out "source" line that added by the Anaconda 
installer so that you won't mess up anaconda python and OS python. 
See below section to check how to activate conda.

Similar with python virtual environment, conda has its own 
environment. 
The detailed documentation could be found `conda.io <https://conda.io/docs/
user-guide/tasks/manage-environments.html>`_.

For this project, I created an environment called **coding-learning-env**. 
You can create the same environment by using the "conda-env.yml" file.

8.0 How to create a conda env
=============================

The first thing first to learn is to create a conda environment. 
Creating a conda env is as easy as:
::

    conda create --name my-conda-env

where the "my-conda-env" is the name of your environment. 
You can also specify the version of python you choose to use in that 
environment:
::

    conda create -n my-conda-env python=3.6

In this case, we create the env by following command:
::

    conda create -n coding-learning-env python=3.6


8.1 How to activate conda
=========================

1. Use command in terminal as follow: 
   :code:`source anaconda3/bin/activate`
   
   Please notice that you do not need to activate conda if the activation is 
   already writen in your .bashrc file.


8.2 How to activate conda environment
=====================================

1. Activate conda
2. Use command in terminal as follow: 
   :code:`source activate coding-learning-env`


8.3 How to create the same environment
======================================

When there is a yml file existed in the repo, and you want to create the 
same environment with same pacakges, you can follow steps below:

1. Activate conda
2. Git clone the repo to local, then cd to that repo directory.
3. Use command in terminal as follow: 
   :code:`conda env create -f conda-env.yml`


8.4 How to exit current environment
===================================

1. Use command in terminal as follow: :code:`source deactivate`

   Plus, this works for both leaving conda and conda environment.


8.5 How to export the conda environment to yml file
===================================================

1. Activate the conda environment you want to export first.
2. Use command in terminal as follow: 
   :code:`conda env export > nameEnvironment.yml`, 
   where nameEnvironment is the yml file name. 

   In this project case, we use :code:`conda env export > conda-env.yml`

   Plus, this is how you can update the conda environment.
3. To obtain no-builds list, one could use
   :code:`conda env export --no-builds > conda-no-builds-env.yml`
  
   The no-builds list is for cross-platform.


8.6 How to see the conda environment list
=========================================

1. Activate conda
2. Use command in terminal as follow: :code:`conda env list`

