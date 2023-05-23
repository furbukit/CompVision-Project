# CITS4402 Computer Vision Project
Created by William Tran, Matthew Walsh, Jasper Greenland. 

This file contains instructions on how to run our project, which is a web app with a ReactJS frontend and a Django backend. 

## 1. Access the Code and Install Requirements and Dependencies
To access the project code, either:<br>
1. Unzip provided project zip file; or<br>
2. In terminal navigate to where you want to store the project using the `cd` and `dir` commands if you're in windows (`cd` and `ls` otherwise)
3. Type `git clone https://github.com/furbukit/CompVision-Project` into the terminal
4. Wait for repo to clone
5. If it asks you to sign in or for authentication at any point, find the connect using browser option and follow those instructions
6. Set your email and name <br>
`git config --global user.name "your_name"`<br>
`git config --global user.email "your_email@email.com"`<br>
7. After Step 6, opening that folder in File Explorer will display the 'CompVision-Project' folder containing everything in this repository
8. Now in VSCode, `File -> Open Folder -> Open this project`
<br>
Now, to install the requirements necessary for our project, run this following command into Terminal:<br>
`pip install -r requirements.txt`

## 2. Create Virtual Environment
Before the code can be run, a virtual environment should be created to prevent current imports from contaminating the project.
This can be accomplished from the following steps:
In terminal,
1. Navigate to the folder containing our project's files with `cd FolderName`.
2. Create a new virtual environment called 'env' with <br>
`python -m venv env`
3. Activate the 'env' virtual environment with: <br>
`.\env\Scripts\activate` in Windows, or <br>
`source env/bin/activate` in MacOS/Linux <br>

Terminal will now have `(env)` in front of the directory showing the activated virtual environment.<br>
4. To exit the virtual environment, type `deactivate`

## 3. Launching the Web Application
To access our project, we must first complete the following steps.
1. Navigate into the project folder by typing the following into terminal:<br>
`cd CompVision-Project`<br>
2. Run the app with<br>
`python manage.py runserver`<br>
3. Access the web app through your browser of choice by typing `http://localhost:3000/` into the URL bar.

# The Project
To follow is a rundown of the project, and how to operate the web app. Navigate the relevant Tasks of the project via the bar at the top of the page.

##  Task 1: The Rough Detection
This task of the project detects candidate targets in the images. It firstly utilises a rough segmentation mask to segment out pixels likely to be part of the targets. Then connected components is done 

## Bug-fixing Issues
Initially, we encountered errors in installing the requirements necessary for our project to run. If this occurs:<br>
1. install Microsoft Visual C++ 14.0 or greater from the `Microsoft C++ Build Tools` package using the following link<br>
https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Launch .exe file and wait for install to complete
3. When the Visual Studio Installer GUI pops up, select 'Desktop development with C++' and Install
4. Wait for install to complete

Then the requirements should install properly.



