=====
1 CPP
=====

1.1 GCC and Make
================

To learn C++, one could look around GCC (GNU C Compiler) first.

The tutorial could be seen `here <https://www3.ntu.edu.sg/home/ehchua/
programming/cpp/gcc_make.html>`_.

1. g++ command is used to compile source file. One could use commands 
   in termianl as follow to generate executable file:
   ::

        g++ -o hello hello.cpp
        chmod a+x hello
        ./hello

where:

- "-o" specifies the executable filename.
- "chmod a+x" gives the file execute permission.
- "./hello" runs the executable.
- also, if you use "g++ hello.cpp", you will get a "a.out" as an execuable.
