Softwares that must be preinstalled in raspberry pi
1. Opencv

Steps to followed to run the website in Raspberry Pi

1. Start the raspberry pi
2. Go to 'osvi' folder
3. Open the terminal there (right click->open terminal)
4. Type these commands one by one in terminal
	$ pip install picamera
	$ pip install flask
	$ export FLASK_APP=osvi.py
	$ flask run
5. wait for some 30sec or 1 min.
6. Go to browser and browse to localhost:5000 or 127.0.0.1:5000 or 0.0.0.0:5000
