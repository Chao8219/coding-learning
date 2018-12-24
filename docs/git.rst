=====
6 Git
=====

Learning using git and GitHub are good for future work and our resume. 
Here are some simple hints to use git for this project.

6.1 Git and GitHub
==================

The relationship between **git** and **GitHub** is simple: **git** is 
a software to help do version control; **GitHub** is a platform to 
store your code.

The software **git** is commonly seen in Linux or Mac OS Terminal. 
Although you might be able to use it in Windows prompt, Chao does not 
believe the prompt is very user friendly. And of course, since the names 
are similar, you may think **git** could only submit codes to **GitHub**, 
but it is not true. The thing is, you can use **git** to push your code 
to your local server. It is useful because we can use **git** to 
control the version, just like what we did in Google Drive before:
::

    TermPaper_v1.pdf
    TermPaper_v2.pdf
    TermPaper_final.pdf
    TermPaper_finalfinal.pdf
    TermPaper_finalfinal_no_typo.pdf
    Wonderful_TermPaper.pdf

On the other hand, **GitHub** supports your **git** very well, and in 
the mean time, it has so many other functions that we can use to build 
our project. We can learn the functionality with **git** together later.

6.2 Use Git on Windows
======================

Install **git** on Windows is not too hard, just follow the instrutor 
`here <https://www.atlassian.com/git/tutorials/install-git#windows>`_.

Other methods are pretty good too.

1. Use Git Bash

   **Git Bash** is more like a software that simulate terminal in linux. 
   It is stright forward so please google **Git Bash** to download it.

2. Use GitHub Desktop

   Like described above, the GitHub Desktop is working for GitHub 
   specificly. You can use it if the GitHub is the only platform 
   you are using. By installing that app, you do not need to know 
   how to use terminal command. But where is the fun of coding anyway? 
   You may better want to get involved into terminal commands 
   sooner than later.

3. Use Editor Integrated Git

   Many modern editors could do the git job for you by one 
   single click, such as VS Code. But since it is integrated into this 
   third-party software, you may encouter some bugs when you are 
   using it. So why don't you just go ahead and learn termial commands?

6.3 Basic Git Command
=====================

When we use git, we want to "download", "update" and "upload" the codes. The terms in git are:

+----------------+------------+------------------------------+-------------------------------------------+
| Common Name    | Term       | Command                      | Note                                      |
+================+============+==============================+===========================================+
| project        | repository |                              | "repo" for short                          |
+----------------+------------+------------------------------+-------------------------------------------+
| download       | clone      |*git clone*                   | clone the repo on GitHub to your computer |
+----------------+------------+------------------------------+-------------------------------------------+
| update         | pull       |*git pull*                    | pull down the recent changes on GitHub    |
+----------------+------------+------------------------------+-------------------------------------------+
| upload_step1   | add        |*git add .*                   | add all local changes into index          |
+----------------+------------+------------------------------+-------------------------------------------+
| upload_step2   | commit     |*git commit -m "Your Message"*| store the index with message              |
+----------------+------------+------------------------------+-------------------------------------------+
| upload_step3   | push       |*git push*                    | finally upload your codes to GitHub       |
+----------------+------------+------------------------------+-------------------------------------------+
| whats going on | status     |*git status*                  | useful tool to debug                      |
+----------------+------------+------------------------------+-------------------------------------------+
| versions       | branch     |*git branch*                  | see which "version" you are in right now  |
+----------------+------------+------------------------------+-------------------------------------------+
| to be countinue|            |                              |                                           |
+----------------+------------+------------------------------+-------------------------------------------+


The markdown table is shown as follow:
::

    | Common Name    | Term       | Command                      | Note                                      |
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

* Step1: go to the repo page, click **Clone or download**, choose 
  **Use HTTPS**, copy the URL.

* Step2: open prompt or terminal, try *cd* to your working folder. 
  *cd* means change directory. Let's say you get a new created folder 
  called "git-hub-repos" in "Document" folder. Firstly, 
  *cd Documents\git-hub-repos*. Remember, you can use "Tab" key at your 
  keyboard to autocomplete some command, like when you only have one 
  folder that started with "Docu" in your Windows account, you can simply 
  type in *cd Docu*, and press "Tab" to complete the entire word.

  When you see you are in the "git-hub-repos" folder, it means you are in 
  right path. If not, please go see this to learn command of Windows 
  prompt here: `Windows prompt <https://www.digitalcitizen.life/
  command-prompt-how-use-basic-commands?page=1>`_.

* Step3: use command "git clone YOUR_URL_HERE". Paste your URL to 
  the right place, and press "Enter" key to let it finish the job.

* Step4: *cd REPOS_NAME* to cd into your repo, then you can see and 
  modify the files!

* Step5: Once you finished modified files, you can use git to upload them. 
  Firstly, use *git config --global user.email YOUR_EMAIL*, then 
  *git config --global user.name YOUR_NAME* to set up your info. 

  Then use commands line by line: *git add .* to add all changes, 
  *git commit -m "YOUR MESSAGE"* to leave a message, *git push* to push it 
  to remote end. You may need to enter your GitHub account and password to 
  finish uploading process.

* Step6: remember to use *git pull* to check the updates by other people 
  every time you want to modify some files. If two or more people are 
  modifying files and uploaded them at the same time, the git may 
  need to process it by merging your two different commit, 
  which could be tricky for this moment.

6.4 Use SSH
===========

If you find it really annoying that you need to type in your username and 
password every time you want to push codes to GitHub, maybe it is time 
for you to use SSH key. In short, SSH is a encrypted way to 
push and pull. The process would be:

* Step1: generate a new local SSH key or find a exist key.

* Step2: add this key to your GitHub account

* Step3: job done!

The details could be found here: `generate ssh key <https://help.github.
com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/>`_. 
You can find both Mac, Windows, and Linux instrution there.

6.5 Submodule
=============

If you want to use other repo to be a part of your project, you may want 
to use submodule of git. The details will be filled in later. For now, 
you can go here: `submodule <http://www.vogella.com/tutorials/
GitSubmodules/article.html>`_ to see how you can use it.
