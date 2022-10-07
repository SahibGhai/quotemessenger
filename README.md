[1]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent  "Connecting To GitHub with SSH"
[2]: https://www.textnow.com  "TextNow"
# Quote Messenger
A quote messenger that uses a quote api to send sms messages to your phone that contain quotes to power you through your day!
I used multiple technologies for this project which you can find in the files.
In the future I would like to add a feature to connect you to the internet if you are not connected.
Enjoy!
## How to install and run
First off I would like to mention that this is specifically made for the raspberrypi (using bash) as you can run a crontab with the pi and have it run the script at designated
times. If you would like to still clone this project on another operating system it should still work as long as the latest version of python is installed. You could 
also use this project to send an SMS to yourself containing some other data such as weather using a weather API, jokes using a joke API, etc.
## Steps
#### 1. Clone
The first step would be to clone this repository into a directory of your choice. The steps for this look different depending on if you are using ssh or not. If you are using ssh
you must make an SSH key and put it into GitHub. Here is a resource for that: [Connecting To GitHub with SSH][1].
#### 2. Activate venv and install packages
In this project we will use a python venv or virtual environment to store all of our packages and dependencies. We will make this venv in the same directory that
we cloned the repository into.
###### venv
The command to activate venv varies based off of the OS you are using:
<br />```Windows: venv/Scripts/activate```
<br />```MacOs & Linux: source venv/bin/activate```
<br />```Deactivate venv(applys to all): deactivate```
<br />
<br />Now, to install the required packages we will first enter the directory in which we cloned this repository into. Then we will make sure our venv is activated([venv](######venv)).
then we can run this command, ```pip install -r requirements.txt```.
#### 3. PyTextNow
Once you install all the packages you will notice that there is a dir in your project directory called PyTextNow. If you enter that directory and list the different
files in it you should see a file called requirements.txt. Enter that file and remove the line that says ```mimetypes```. Then save it and run an other file in that directory
called setup.py using this command: ```python setup.py```. Once done you can delete the PyTextNow directory.
#### 4. TextNow
<br />Once this is done then we can go to [TextNow][2] and make our free account. Once you do this you can go back into your CLI and go back into the project directory.
Make a file called .env and enter it and edit it as so: 
```## .env file example
USERNAME=<insert TextNow username>
SID=<insert what your SID cookie is when on your TextNow profile>
CSRF=<insert what your CSRF cookie is when on your TextNow profile>
PHONE=<insert the phone number related to the device you would like to send the SMS to>
```
<br />The cookies can be found by right clicking on the profile page, going over to application, clicking on cookies, and finding the SID and CSRF cookies.

#### 5. Enjoy!
There you go! Now you can confirm your internet connection and do a couple of test runs by simply running the file with ```python quotemessenger.py```! You can also
make a new crontab and run a cronjob so that way the program runs at the designated time and date that you set. Please reach out if there is any bugs or 
questions. Thank you!

## Credits:
https://github.com/leogomezz4t/PyTextNow_API
<br />https://youtu.be/0eVnAHULFm0
<br />https://forum.freecodecamp.org/t/free-api-inspirational-quotes-json-with-code-examples/311373
