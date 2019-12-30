# CS 6161: Algorithms Term Project

To run the code from the terminal, clone the repo and run the following commands (assuming you’re beginning at the root of the repo):
- pip install -r requirements.txt
- cd voronoi_backend
- python video_voronoi.py
- Enter the name of the file you’d like to see transformed without its extension (ie: mp4). Enter the desired number of frames and sampling rate, then view the converted video in the same folder stored as `voronoi_fileName` 

To run the web application, clone the repo and run the following commands in your terminal: 
- pip3 install -r requirements.txt
- python3 manage.py migrate
- python3 manage.py makemigrations
- python3 manage.py runserver
- Once that’s done, navigate to 127.0.0.1:8000 and view the webapp. You should see the following screen: 

Navigate through the webapp, and enter in a file name. Select an mp4 file that is less than 4 seconds, and enter an error rate (how much to sample: more samples will make it slower) and the desired number of frames per second (how fast or slow you want the final video; higher FPS will make the program slower). Select upload. There is a slight bug with the webapp, so if the video doesn’t appear in your /application/media/videos from the root of the project, you might have to upload the video again. 
