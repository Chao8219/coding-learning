# Coding Learning Repo

This repo is for coding-learning for beginners. Please feel free to contact me to work this together.

# Contents

&nbsp;&nbsp;[1 CPP](#1-cpp)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1.1 GCC and Make](#11-gcc-and-make)

&nbsp;&nbsp;[2 Python](#2-python)

&nbsp;&nbsp;[3 Doxygen](#3-doxygen)

&nbsp;&nbsp;[4 Ubuntu Tips](#4-ubuntu-tips)

&nbsp;&nbsp;[5 General Tips](#5-general-tips)

&nbsp;&nbsp;[6 Git](#6-git)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6.1 Git and GitHub](#61-git-and-github)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6.2 Use Git on Windows](#62-use-git-on-windows)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6.3 Basic Git Command](#63-basic-git-command)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6.4 Use SSH](#64-use-ssh)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[6.5 Submodule](#65-submodule)

&nbsp;&nbsp;[7 Graphviz](#7-graphviz)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7.1 DOT Language](#71-dot-language)

# 1 CPP

## 1.1 GCC and Make

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

[Back to top](#contents)

# 2 Python

See python tips in submodule **py-starter**. (for now)

[Back to top](#contents)

# 3 Doxygen

## 3.1 Normal Use of Doxygen Steps:

1. Install Doxygen ( Personal opinion, do not use GUI version ).
2. Go to your repo directory.
3. Open terminal here, type in `doxygen -g` to generate a Doxygen config file.
4. Open the config file with editor, and go through some important tags, like "PROJECT_NAME", "INPUT", "USE_MDFILE_AS_MAINPAGE", etc.
5. Modify the comment in your code so that it could be seen by doxygen.
6. Use `doxygen Doxygen` to run the building process.

[Back to top](#contents)

# 4 Ubuntu Tips

## 4.1 Ubuntu 101
    
- Use `Ctrl+Alt+T` to open terminal.
- In terminal, use `Ctrl+Shift+T` to open a new tab.
- Use `Ctrl+D` to close terminal window.
- Use `cd` to change directory.
- Use `ls` to check list
- Use `gedit ~/.bashrc` to open the file that will automatically run the moment you open a new terminal.
    - Additionally, if you are using OS X, you can use `open -e [file name]` to open the file.

## 4.2 Set Terminal Tab Name
    
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

[Back to top](#contents)

# 5 General Tips

## 5.1 Naming Rules

1. For name of repos, one should use all lowercase letters with dash (**-**) connecting words.

Example: **coding-learning**, **py-starter**

2. For git commit comments, one should use "noun" + "verb past tense", all in lower-case unless specific words needed.

Example: **README updated**, **more functions added**

## 5.2 Choose License

You can select a type of license for your project [here](https://choosealicense.com/).

In this repo, you can see MIT License.

## 5.3 Design Logo

A logo is not really necessary for your project, but you can always use few minutes to design one simple logo that based on exist template.

You can use different webside to do so. In this repo, you can see logo designed from [here](https://www.wix.com/logo/maker). Obviously, high resolution logo is expensive, however the low res one, which is good enough for us, is always free to get.

## 5.4 Markdown

Markdown, or .md file, is usful in github. If you wanna use some tricks in markdown file, all you need is google.com.

Also, github supports some unique markdown feature, such as:

- [ ] To-do List
- [x] To-do List (Done)

## 5.5 Learn Coding

1. [sololearn](https://www.sololearn.com/).
        You can have all types of code to learn. 
2. [cplusplus.com](http://www.cplusplus.com/doc/tutorial/) 

[Back to top](#contents)

# 6 Git

Learning using git and GitHub are good for future work and our resume. Here are some simple hints to use git for this project.

## 6.1 Git and GitHub

The relationship between **git** and **GitHub** is simple: **git** is a software to help do version control; **GitHub** is a platform to store your code.

The software **git** is commonly seen in Linux or Mac OS Terminal. Although you might be able to use it in Windows prompt, Chao does not believe the prompt is very user friendly. And of course, since the names are similar, you may think **git** could only submit codes to **GitHub**, but it is not true. The thing is, you can use **git** to push your code to your local server. It is useful because we can use **git** to control the version, just like what we did in Google Drive before:

```
TermPaper_v1.pdf
TermPaper_v2.pdf
TermPaper_final.pdf
TermPaper_finalfinal.pdf
TermPaper_finalfinal_no_typo.pdf
Wonderful_TermPaper.pdf
```

On the other hand, **GitHub** supports your **git** very well, and in the mean time, it has so many other functions that we can use to build our project. We can learn the functionality with **git** together later.

[Back to Top](#contents)

## 6.2 Use Git on Windows

Install **git** on Windows is not too hard, just follow the instrutor [here](https://www.atlassian.com/git/tutorials/install-git#windows)

Other methods are pretty good too.

1. Use Git Bash

	**Git Bash** is more like a software that simulate terminal in linux. It is stright forward so please google **Git Bash** to download it.

2. Use GitHub Desktop

	Like described above, the GitHub Desktop is working for GitHub specificly. You can use it if the GitHub is the only platform you are using. By installing that app, you do not need to know how to use terminal command. But where is the fun of coding anyway? You may better want to get involved into terminal commands sooner than later.

3. Use Editor Integrated Git

	Many modern editors could do the git job for you by one single click, such as VS Code. But since it is integrated into this third-party software, you may encouter some bugs when you are using it. So why don't you just go ahead and learn termial commands?

[Back to Top](#contents)

## 6.3 Basic Git Command

When we use git, we want to "download", "update" and "upload" the codes. The terms in git are:

| Comman Name    | Term       | Command                      | Note                                      |
| -------------- | ---------- |:----------------------------:| ----------------------------------------- |
| project        | repository |                              | "repo" for short                          |
| download       | clone      |`git clone`                   | clone the repo on GitHub to your computer |
| update         | pull       |`git pull`                    | pull down the recent changes on GitHub    |
| upload_step1   | add        |`git add .`                   | add all local changes into index          |
| upload_step2   | commit     |`git commit -m "Your Message"`| store the index with message              |
| upload_step3   | push       |`git push`                    | finally upload your codes to GitHub       |
| whats going on | status     |`git status`                  | useful tool to debug                      |
| versions       | branch     |`git branch`                  | see which "version" you are in right now  |
| to be countinue|            |                              |                                           |

When you have a remote repo:

* Step1: go to the repo page, click **Clone or download**, choose **Use HTTPS**, copy the URL.

* Step2: open prompt or terminal, try `cd` to your working folder. `cd` means change directory. Let's say you get a new created folder called "git-hub-repos" in "Document" folder. Firstly, `cd Documents\git-hub-repos`. Remember, you can use "Tab" key at your keyboard to autocomplete some command, like when you only have one folder that started with "Docu" in your Windows account, you can simply type in `cd Docu`, and press "Tab" to complete the entire word.

	When you see you are in the "git-hub-repos" folder, it means you are in right path. If not, please go see this to learn command of Windows prompt [here](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands?page=1).

* Step3: use command "git clone YOUR_URL_HERE". Paste your URL to the right place, and press "Enter" key to let it finish the job.

* Step4: `cd REPOS_NAME` to cd into your repo, then you can see and modify the files!

* Step5: Once you finished modified files, you can use git to upload them. Firstly, use `git config --global user.email YOUR_EMAIL`, then `git config --global user.name YOUR_NAME` to set up your info. 

	Then use commands line by line: `git add .` to add all changes, `git commit -m "YOUR MESSAGE"` to leave a message, `git push` to push it to remote end. You may need to enter your GitHub account and password to finish uploading process.

* Step6: remember to use `git pull` to check the updates by other people every time you want to modify some files. If two or more people are modifying files and uploaded them at the same time, the git may need to process it by merging your two different commit, which could be tricky for this moment.

[Back to Top](#contents)

## 6.4 Use SSH

If you find it really annoying that you need to type in your username and password every time you want to push codes to GitHub, maybe it is time for you to use SSH key. In short, SSH is a encrypted way to push and pull. The process would be:

* Step1: generate a new local SSH key or find a exist key.

* Step2: add this key to your GitHub account

* Step3: job done!

The details could be found [here](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/). You can find both Mac, Windows, and Linux instrution there.

## 6.5 Submodule

If you want to use other repo to be a part of your project, you may want to use submodule of git. The details will be filled in later. For now, you can go [here](http://www.vogella.com/tutorials/GitSubmodules/article.html) to see how you can use it.

[Back to top](#contents)

# 7 Graphviz

The graphviz is a powerful tool to plot diagrams from source code. You can use different engines to generate diagrams as pics or pdf in graphviz.

The installation is simple and strightforward: go to [download](https://graphviz.gitlab.io/download/), find your OS and do as they said.

## 7.1 DOT Language

DOT language is simple. You could go [here](http://melp.nl/2013/08/flow-charts-in-code-enter-graphviz-and-the-dot-language/) to find a easy-handy example to plot flowchart.

As is written in the example, you can use any editor to write down the code, and generate the format you want by command in terminal: `dot -Tpng -o example.png example.gv`

[Back to top](#contents)

## 7.2 Python

You can also use python to generate dot file. See [here](https://pypi.org/project/graphviz/) to see how to use it.

You may need to use anaconda to run the script.

[Back to top](#contents)
