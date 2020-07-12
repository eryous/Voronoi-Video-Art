# Voronoi Video Art

To run the code from the terminal, clone the repo and run the following commands (assuming you’re beginning at the root of the repo):
- pip install -r requirements.txt
- cd voronoi_backend
- Save the video you want to 'Voronoi-fy' in this folder
- python video_voronoi.py
- Enter the name of the file you’d like to see transformed without its extension (ie: mp4). Enter the desired number of frames and sampling rate, then view the converted video in the same folder stored as `voronoi_fileName` 
- Keep in mind that longer videos will take longer amounts of time to fully render the final product, a 5 second video using a 0.3 Error rate at 25 FPS took my 2.3 GHz Intel Core i5 MacBook Pro (2017) about 80 seconds to complete.
