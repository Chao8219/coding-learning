=============
4 Ubuntu Tips
=============

4.1 Ubuntu 101
==============
    
- Use **Ctrl+Alt+T** to open terminal.
- In terminal, use **Ctrl+Shift+T** to open a new tab.
- Use **Ctrl+D** to close terminal window.
- Use **cd** to change directory.
- Use **ls** to check list
- Use **gedit ~/.bashrc** to open the file that will automatically run the moment you open a new terminal.

  - Additionally, if you are using OS X, you can use **open -e [file name]** to open the file.

4.2 Set Terminal Tab Name
=========================
    
Use **gedit ~/.bashrc** to open .bashrc file. Add script as follow:
::

    function set-title(){
    if [[ -z "$ORIG" ]]; then
    ORIG=$PS1
    fi
    TITLE="\[\e]2;$*\a\]"
    PS1=${ORIG}${TITLE}
    }

Then you can use the function **set-title** to set title up.

4.3 Bash Shell Script
=====================

Write and run bash shell script is simple. Please see the bash file in 
this repo to use it.
