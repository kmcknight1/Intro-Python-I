import sys
import os
import console
console.clear()
"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print('\nsys.argv command line arguments: ')
for i in range(0, len(sys.argv)):
    print(sys.argv[i])

# Print out the OS platform you're using:
print("\nOS platform I'm using: " + sys.platform)

# Print out the version of Python you're using:
python_path = sys.exec_prefix.split('/')
print("\nVerson of Python I'm using: %s" % python_path[len(python_path)-1])


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
process_id = os.getpid()
print('\nCurrent process ID: %s' % process_id)

# Print the current working directory (cwd):
cwd = os.getcwd()
print('\nCurrent working directory (cwd): %s ' % cwd)

# Print out your machine's login name
machine_login = os.getlogin()
print("\nMachine's login: %s" % machine_login)
