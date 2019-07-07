=========
3 Doxygen
=========

3.1 Normal Use of Doxygen Steps
===============================

1. Install Doxygen ( Personal opinion, do not use GUI version ).
2. Go to your repo directory.
3. Open terminal here, type in :code:`doxygen -g` to generate a 
   Doxygen config file.
4. Open the config file with editor, and go through some important tags, 
   like "PROJECT_NAME", "INPUT", "USE_MDFILE_AS_MAINPAGE", etc.
5. Modify the comment in your code so that it could be seen by doxygen.
6. Use :code:`doxygen Doxygen` to run the building process.
