# CompVision-Project
Project for CITS4402 Computer Vision SEM1 2023.

## 1. Installing GitHub
Welcome to GitHub! I know this looks overly complicated but trust me when I say it is worth setting up if you're doing a coding project.  The whole point of using this  is it allows us all to edit and run the code at the same time on the same environment, it also allows us to bring back old versions of the code if we accidentally break it.
<br>
<br>
To install GitHub follow these instructions:
1. Visit the Git website at https://git-scm.com/download/win.
2. Click the "Download" button to download the latest version of Git for Windows.
3. Run the downloaded installer file (the file name should be something like "Git-2.x.x.x-64-bit.exe").
4. Review your installation choices and click "Install" to begin the installation.
5. Wait for the installation to complete.
6. Click "Finish" to exit the installer.

Then you want to do the following to access the project code.  
1. In terminal navigate to where you want to store the project using the `cd` and `dir` commands if you're in windows (`cd` and `ls` otherwise)
2. Type `git clone https://github.com/furbukit/CompVision-Project` into the terminal
3. Wait for repo to clone
4. If it asks you to sign in or for authentication at any point, find the connect using browser option and follow those instructions
5. Set your email and name <br>
`git config --global user.name "your_name"`<br>
`git config --global user.email "your_email@email.com"`<br>
6. Now if you open that folder in File Explorer you will see the 'CompVision-Project' folder containing everything in this repository
7. Now in VSCode, `File -> Open Folder -> Open this project`

## 2. Create Virtual Environent
We create a virtual environment to run the code (basically segmenting a special part of our computer for it) to ensure that the imports we currently have on our computer don't contaminate our project.  In other words we want to make sure that if someone wants to run our code on any device that they can do so.

First navigate into your the CompVision-Project folder using `dir` to list out all files/folders in your current directory and `cd FolderName` to change your directory into folder FolderName.  Using `cd ..` will take you back one directory.

In terminal, to create a new virtual environment called 'env'<br>
`python -m venv env`

To activate your 'env' virtual environment (Windows)<br>
`.\env\Scripts\activate`

To activate your 'env' virtual environment (MacOS/Linux)<br>
`source env/bin/activate`

Our terminal will then switch to have `(env)` in front of it signifying we are using a new environment.  This should also have created a folder called 'env' in your local project folder, this should NOT be uploaded to GitHub.  There is code in place to stop it uploading to GitHub as long as it's called 'env'

To exit a virtual environment just type<br>
`deactivate`

## 3. Installing Requirements and Dependencies

For some reason Django wants C++ installed on the computer beforehand so I will add that here.  
1. install Microsoft Visual C++ 14.0 or greater from the `Microsoft C++ Build Tools` package using the following link<br>
https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Launch .exe file and wait for install to complete
3. When the Visual Studio Installer GUI pops up, select 'Desktop development with C++' and Install
4. Wait for install to complete

We then will want to install all the requirements (python libraries in this case) so that we can run the code

To install requirements type <br>
`pip install -r requirements.txt`

You might have to run this every time you pull the code from the repository to ensure your libraries are up to date

## 3. Working with GitHub

There are only two kinds of 'requests' I want you to care about.  Pull requests (taking data from the repo to your local machine) and Push requests (taking data from your local machine and putting it on the repo)

You pull before you start coding, and then push when you finish coding.

Here's the command for pulling<br>
```git pull origin main```


BEFORE YOU PUSH, you want to add your changes and then commit your changes.

To add all your changes type <br>`git add .`

To commit all the changes you just made.  In the message section give a brief description of the changes you made<br>
`git commit -m "The message you want to assign to this commit`

Then you can push your changes<br>
`git push origin main`

## 4. Adding to the Requirements

Whenever you install a new python library you will need to tell the requirements.txt file that you have added a new dependancy.  Type the following command whenever you do another `pip install` command.

`pip freeze > requirements.txt`