# BookManagementApp
Book management application is application for managemening book.

Requirements to run this project.
Python 3 
 
Clone the repo to your computer. For example, to place it on your Desktop.
cd ~/Desktop
git clone https://github.com/Pragesh-yadav/BookManagementApp.git
cd BookManagementApp

Install the Pipenv packages and start a new shell. Then cd into the backend directory and run the local server.

pipenv install
Now go to project env
pipenv shell
 Once you are inside project env below packages are required. 

1: pip install django==2.1.7
once above command executed run below command to install django  rest framework
2 djangorestframework==3.10
3: pipenv install django-cors-headers

You can see the App now at http://127.0.0.1:8000/

Here you can login into app and add new books , edit and delete book.
