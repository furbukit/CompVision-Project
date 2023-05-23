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
<br>
The following dependencies are needed for running the frontend of our web application.  
1. Node.js 18.12 https://nodejs.org/en/blog/release/v18.12.0
2. Yarn
<br>
To install yarn follow the instructions below.  Open a new administrator terminal instance type `corepack enable`.  Then type `corepack prepare yarn@3.5.1 --activate`.  If this does not work follow the instructions here https://yarnpkg.com/getting-started/install.  We are using yarn version 3.5.1 for reference

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
2. Activate your virtual environment (above)
3. Install requirements.txt with `pip install -r requirements.txt`
4. Run the backend of the app with<br>
`python manage.py runserver`<br>
<br><br>
Now open a second terminal instance, and navigate to `CompVision-Project/frontend`
1. Type `yarn install` to install the frontend dependencies
2. Type `yarn start` to start the frontend server
3. The web app should automatically open, if it does not you can access the web app through your browser of choice by typing `http://localhost:3000/` into the URL bar.

# The Project
To follow is a rundown of the project, and how to operate the web app. Navigate the relevant Tasks of the project via the bar at the top of the page.

##  Task 1: The Rough Detection
This task of the project detects candidate targets in the images. It firstly utilises a rough segmentation mask to segment out pixels likely to be part of the targets. Then connected components analysis is done to set up segmentation. Then object clusters that are not obviously round are filtered out by thresholding and by their area. To view this function in the web app:<br>
1. Select Task 1 in the top bar.
2. In the drop-down box, select the image to analyse. Images are arranged by camera. 
3. The slider bars adjust the parameters for image analysis
The output of Task 1 is an image containing red dots highlighting the centers of clusters, and green elipses for identified hexagonal targets
## Task 2: Targets analysis and refinement
This task implements the analysis and refinement methods required. This Task takes the output from Task 1, and includes a list of the clusters sorted into 6 for the hexagonal targets, and the coloured image. It overlays rectangles onto individual clusters in the targets, then draws a red dot in the middle of the target before using identifying the underlying colour of the coloured image, accounting for gain. It then appends this colour to the unique identifier of that target, which is displayed above the target. 
1. Select Task 2 in the bar at the top of the page.
2. Select image to analyse as in Task 1. 
3. Images should display the rectangles overlayed onto the targets.

## Bug-fixing Issues
Initially, we encountered errors in installing the requirements necessary for our project to run. If this occurs:<br>
1. install Microsoft Visual C++ 14.0 or greater from the `Microsoft C++ Build Tools` package using the following link<br>
https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Launch .exe file and wait for install to complete
3. When the Visual Studio Installer GUI pops up, select 'Desktop development with C++' and Install
4. Wait for install to complete

Then the requirements should install properly.
<br>
<br>
If there are issues with Django installation, please follow the following instructions at https://docs.djangoproject.com/en/4.2/topics/install/


