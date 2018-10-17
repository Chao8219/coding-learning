# Coding Learning Repo

This repo is for testing and learning all kinds code and software I may need.

# Contents

1. [CPP](#cpp)
2. [Python](#python)
3. [Doxygen](#doxygen)
4. [Ubuntu Tips](#ubuntu-tips)
5. [General Tips](#general-tips)

# CPP

## GCC and Make

To learn C++, one could look around GCC (GNU C Compiler) first.

The tutorial could be seen [here](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html)

1. g++ command is used to compile source file. One could type in codes as follow to generate executable file:

```
g++ -o hello hello.cpp
chmod a+x hello
./hello
```

where:
- `-o` specifies the executable filename.
- `chmod a+x` gives the file execute permission.
- `./hello` runs the executable.
- also, if you use `g++ hello.cpp`, you will get a `a.out` as an execuable.

[back to top](#contents)

# Python

[back to top](#contents)

# Doxygen

## Normal Use of Doxygen Steps:

1. Install Doxygen ( Personal opinion, do not use GUI version ).
2. Go to your repo directory.
3. Open terminal here, type in `doxygen -g` to generate a Doxygen config file.
4. Open the config file with editor, and go through some important tags, like "PROJECT_NAME", "INPUT", "USE_MDFILE_AS_MAINPAGE", etc.
5. Modify the comment in your code so that it could be seen by doxygen.
6. Use `doxygen Doxygen` to run the building process.

[back to top](#contents)

# Ubuntu Tips

## Ubuntu 101
    
- Use `Ctrl+Alt+T` to open terminal.
- In terminal, use `Ctrl+Shift+T` to open a new tab.
- Use `Ctrl+D` to close terminal window.
- Use `cd` to change directory.
- Use `ls` to check list
- Use `gedit ~/.bashrc` to open the file that will automatically run the moment you open a new terminal.
    - Additionally, if you are using OS X, you can use `open -e [file name]` to open the file.

## Set Terminal Tab Name
    
Use `gedit ~/.bashrc` to open .bashrc file. Add script as follow:

```
function set-title(){
if [[ -z "$ORIG" ]]; then
ORIG=$PS1
fi
TITLE="\[\e]2;$*\a\]"
PS1=${ORIG}${TITLE}
}
```

Then you can use the function **set-title** to set title up.

## Use Git

1. Use `git init` to initialize config file.
2. To update submodule all at the same time, use `git submodule foreach git pull origin master`.


[back to top](#contents)

# General Tips

## Naming Rules

1. For name of repos, one should use all lowercase letters with dash (**-**) connecting words.

Example: **code-learning**, **py-starter**

2. For git commit comments, one should use "noun" + "verb past tense", all in lower-case unless specific words needed.

Example: **README updated**, **more functions added**

## Choose License

You can select a type of license for your project [here](https://choosealicense.com/).

In this repo, you can see MIT License.

## Design Logo

A logo is not really necessary for your project, but you can always use few minutes to design one simple logo that based on exist template.

You can use different webside to do so. In this repo, you can see logo designed from [here](https://www.wix.com/logo/maker). Obviously, high resolution logo is expensive, however the low res one, which is good enough for us, is always free to get.

## Markdown

Markdown, or .md file, is usful in github. If you wanna use some tricks in markdown file, all you need is google.com.

Also, github supports some unique markdown feature, such as:

- [ ] To-do List
- [x] To-do List (Done)

## Learn Coding

1. [sololearn](https://www.sololearn.com/).
        You can have all types of code to learn. 
2. [cplusplus.com](http://www.cplusplus.com/doc/tutorial/) 

[back to top](#contents)
