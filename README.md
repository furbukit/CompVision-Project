# CompVision-Project
Project for CITS4402 Computer Vision SEM1 2023.

## Development:
### 1. Getting the Code
Welcome to GitHub! I know this looks overly complicated but trust me when I say it is worth setting up if you're doing a coding project.  The whole point of using this  is it allows us all to edit and run the code at the same time on the same environment, it also allows us to bring back old versions of the code if we accidentally break it.
<br>
<br>
To install GitHub follow these instructions:
1. Download the latest version of the GitHub CLI from the official website: https://cli.github.com/
2. Once the download is complete, open the downloaded file and run the installation wizard.
3. Follow the prompts in the installation wizard to complete the installation process. You can choose the default installation options or customize them as per your requirements.
4. After the installation is complete, open the command prompt or PowerShell and type the following command to verify the installation:
`gh --version`
This should display the version of the GitHub CLI that you have installed.
6. You will also need to authenticate the GitHub CLI using your GitHub account credentials before you can start using it. You can do this by running the following command:
`gh auth login`
Follow the prompts to complete the authentication process.

Once GtiHub is installed, in the terminal navigate to the folder you want your project in and type the following command
`git clone https://github.com/furbukit/CompVision-Project`
Now if you open that folder in File Explorer you will see the 'CompVision-Project' folder containing everything in this repository

### 2. Create Virtual Environent
We create a virtual environment to run the code (basically segmenting a special part of our computer for it) to ensure that the imports we currently have on our computer don't contaminate our project.  In other words we want to make sure that if someone wants to run our code on any device that they can do so.

In terminal, to create a new virtual environment called 'env'
`python -m venv env`

To activate your 'env' virtual environment (Windows)
`.\env\Scripts\activate`

To activate your 'env' virtual environment (MacOS/Linux)
`source env/bin/activate`

Our terminal will then switch to have (env) in front of it signifying we are using a new environment.  

### 3. Installing Requirements
We then will want to install all the requirements (python libraries in this case) so that we can run the code

To install requirements:
`pip install -r requirements.txt`

You might have to run this every time you pull the code from the repository to ensure your libraries are up to date

### 3. Working with GitHub

There are only two kinds of 'requests' I want you to care about.  Pull requests (taking data from the repo to your local machine) and Push requests (taking data from your local machine and putting it on the repo)

You pull before you start coding, and then push when you finish coding.

Here's the command for pulling (I know you need it @Will)
`git pull origin main`

BEFORE YOU PUSH, you want to add your changes and then commit your changes.

To add all your changes
`git add .`

To commit all the changes you just made.  In the message section give a brief description of the changes you made
`git commit -m "The message you want to assign to this commit`

Then you can push your changes
`git push origin main`

### 4. Adding to the Requirements
