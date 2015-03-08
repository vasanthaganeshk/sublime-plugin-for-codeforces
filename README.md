# sublime-plugin-for-codeforces
custom build for taking testcase from codeforces and checking if the program is correct.

Platform: Gnu/Linux, should work with osx with a little hack.
Language: Python

Description: This program takes testcases from codeforces and tells if your program's output matches the output from testcases.

Hello my dear user,

Are you using python on codeforces?
Are you using sublime3 for writing code?

Then this must be a gold mine for you. Just copy and paste the three files namely master.py, MyParser.py and new_code.py in your current working directory. Wait you are not done yet, take the "codeforces_python.sublime-build" and copy it to your ~/.config/sublime-text-3/Packages/User. Now open sublime text editor and go to tools>Build system>codeforces_python.

How to use it?

comment the first line of your program as the problem code.
For example:
If your problem is 158A, then comment your first line like this "#158A" (without quotes).

press "ctrl-b" to build and done.
By the way you need a working internet connection.

Thankyou for reading this page completely.
