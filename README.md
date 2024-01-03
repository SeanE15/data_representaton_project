## <div align="center">Data Representation</div>
### Author: Sean Elliott
### Due Date: last commit on or before 05/01/2024
----

### <div align="center">Introduction</div>

Hello, and welcome to my Github Repository. This repository has been created in order to satify the work required to complete the Data Representation module - which is a key part to my completion of the HDip in Computer Science with Data Analytics at the Atlantic Technological University. This repository contains one main body of work - a project in which we were tasked with writing a program that creates and comsumes RESTful APIs. We had to create a web application in Flask that has a RESTful API and link the app with one or more database tables. We then had to create a webpage that consumes the API (ie. perform CRUD operations).

---- 

## <div align="center">Remote Hosting</div>

This program is hosted remotely through the medium of PythonAnywhere the link to which is here: http://g00411288.pythonanywhere.com/

----

## <div align="center">System Requirements</div>

To modify or run the program on a local machine requires the latest version of Python. Anaconda is an easy to use version available at the following URL's for Windows, Mac and Linux.

[1] Download Python from https://www.python.org/

[2] Go to https://github.com/SeanE15/data_representaton_project, click the 'Code' button and then 'Download ZIP'. Unzip the downloaded file on your local machine.

[3] Ensure all the required modules are installed. In the folder, where the repository has been unzipped, start the terminal (on windows I prefer to use CMDer). Install the required modules that are specified in the requirements.txt file:

    pip3 install -r requirements.txt

[4] Navigate to the 'data_representation_project' folder in the command line of your choosing.

[5] In the project folder load the virtual environment; typing:

    .\venv\Scripts\activate.bat

[6] The run the server:

    python server,py

[7] You can now navigate to your web browser of your choosing, typing into the address bar:

    http://127.0.0.1:5000/

----

**The breakdown of the project files are as follows:**

[1] data folder: This contains an old JSON file which I started working on at the start of the project and abandoned as i couldnt get the JSON file to integrate with my MySQL database. With more time; this is where I will expand the project to incorporate this JSON.

[2] staticpages folder: This is the parent folder that holds the child folder 'images' that houses the two images that are on the carousel on the homepage of the website.

[3] templates folder: This folder houses the webpage HTML program.

[4] .gitignore: This file holds the important information that I didnt want sent up to github; which includes the config.py file.

[5] cso-formatted.json: This is the formatted JSON file of the CSO data.

[6] csoDAO.py: This program is responsible for reading the data from the CSO webpage, pulling it down and breaking the file into readable chunks so that the information can be stored in a database. It outputs the readable file to cso-formatted.json.

[7] partDAO.py: This program creates and runs the MySQL database for the parts catalogue that the user can use. The user has free reign to add/delete and update any parts within the database.

[8] pointsDAO.py: This program is an attempt to utilise the cso-formatted.json file and output it into a mysql database for viewing by the user on the webpage. The envisioned goal would be that the user could enter a county and a year and see the break down of penalty points issued in that county within a certain year.

[9] README: This is the file that details the files contained within the project. You are reading it currently, fair play!

[10] requirements.txt: This file details the required programs that the system must have installed in order to run the programs locally. See directions about how to utilise this file.

[11] server.py: This program allows the user to perform CRUD operations on the parts database.

---- 

## <div align="center">References</div>

[1] https://jackmckew.dev/make-a-readme-documentation-with-jupyter-notebooks.html

[2] https://www.kaggle.com/code/geethikakandala0503/exploratory-data-analysis - Date Accessed: 28/12/2023

[3] https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho/code - Date Accessed: 28/12/2023

----

## <div align="center">Credits</div>

- My wife Donna McCafferty for her patience

- Google and its many wonders

