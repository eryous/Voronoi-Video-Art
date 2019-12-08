import os
from os.path import isfile, join
from multiprocessing import Pool
import cv2
import numpy as np
from voronoi import voro

prompt_user = input("Enter the video you would like to 'Voronoi-fy': ")
frames_per_second = int(input("Enter the amount of frames per second you would like to see the final product in: "))
error_rate = float(input("Enter an error rate between .1 - .5, the smaller the rate, the more sampling is done: "))
frames = './frames/'
vid_dir = frames + prompt_user + '/'
voro_vid_dir = frames + "voro_" + prompt_user + '/'
vid = prompt_user + '.mp4'

def vid_to_frames(video_title):
    capture = cv2.VideoCapture(video_title)

    if not os.path.exists(frames):
        os.makedirs(frames)

    if not os.path.exists(vid_dir):
        os.makedirs(vid_dir)

    if not os.path.exists(voro_vid_dir):
        os.makedirs(voro_vid_dir)

    current_frame = 0

    while (True):
        ret, frame = capture.read()
        if not ret:
            break

        name = vid_dir + str(current_frame) + '.jpg'
        cv2.imwrite(name, frame)
        current_frame += 1
    capture.release()
    cv2.destroyAllWindows()
vid_to_frames(vid)

pics = [f for f in os.listdir(vid_dir) if isfile(join(vid_dir, f))]
input_voro = []
for i in range(0,len(pics)):
    input_voro.append((vid_dir + pics[i],pics[i][:-4],voro_vid_dir, error_rate))
    # voro(vid_dir + pics[i],pics[i][:-4],voro_vid_dir)

pool = Pool(30)
pool.map(voro, input_voro)
pool.close()
def frames_to_vid(in_dir, fps):  #
    frame_array = []
    files = [f for f in os.listdir(in_dir) if isfile(join(in_dir, f))]
    for i in range(0, len(files)):
        frame_name = str(i) + '.jpg'
        img = cv2.imread(in_dir+frame_name)
        height, width, layers = img.shape
        size = (width, height)
        frame_array.append(img)
    output = cv2.VideoWriter("voronoi_" + vid, cv2.VideoWriter_fourcc(*'DIVX'),
                             fps, size)
    for i in range(0, len(frame_array)):
        output.write(frame_array[i])
    output.release()


frames_to_vid(voro_vid_dir, frames_per_second)
