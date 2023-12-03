# WMI-Domain-Controller-Test
This script will try to connect to the domain controller using the WMI module and query the operating system information. 
If the connection is successful, it will print the OS name and version. If the connection fails, it will print the error code. 
You can run this script on any machine that has Python and the WMI module installed. You can also modify the script to test
other WMI queries or classes. For more information about WMI, you can refer to the [Microsoft documentation]. 

I hope this helps. =)

Prerequisites:
==============

Python (Version 3 is suggested.)
--------------------------------

To install Python 3 on your Windows machine, you can follow these steps:

    Go to the official Python download page for Windows (https://www.python.org/downloads/)

    Find a stable Python 3 release. This tutorial was tested with Python version 3.10.10.
    Click the appropriate link for your system to download the executable file: Windows installer (64-bit) or Windows installer (32-bit).

    Run the installer and click through the setup steps, leaving all the pre-selected installation defaults.

    Check the option to add Python to your PATH environment variable.

    After the installation, click Disable path length limit and then Close.
    To verify that Python is installed correctly, open a command prompt and type python --version. You should see the Python version number that you installed.

There are different ways to install Python 3 on Linux, depending on your distribution and version. Here are some general steps that may work for most Linux systems:

    First, update your system with the package manager of your distribution. For example, on Ubuntu, Debian, or Mint, you can use the apt command:
    sudo apt update

    Next, install Python 3 from the repository of your distribution. For example, on Ubuntu, Debian, or Mint, you can use the apt command:
    sudo apt install python3

    To verify that Python 3 is installed correctly, run the following command:
    python3 --version

    You should see the Python version number that you installed. If you want to install a specific version of Python 3, such as 3.8 or 3.9, you may need to add a Personal Package Archive (PPA) or use a third-party repository. For example, on Ubuntu, you can use      the deadsnakes PPA to install Python 3.8:
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.8

    To install pip, the package installer for Python, you can use the package manager of your distribution. For example, on Ubuntu, Debian, or Mint, you can use the apt command:
    sudo apt install python3-pip

    To launch Python 3, you can use the python3 command. To exit Python 3, you can use the exit() function or press Ctrl+D.

To install the WMI module in Python, you need to have the following prerequisites:
----------------------------------------------------------------------------------
Python
pywin32 (was win32all)
WMI

You can use the pip command to install the WMI module from PyPI, which is a repository of Python packages. To do that, open a command prompt and type:
pip install WMI

