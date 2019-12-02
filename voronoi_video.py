import os
from os.path import isfile, join

import cv2
import numpy as np

prompt_user = input("Enter the video you would like to 'Voronoi-fy': ")
frames = './frames/'
vid_dir = frames + prompt_user + '/'
vid = prompt_user + '.mp4'

def vid_to_frames(video_title):
    capture = cv2.VideoCapture(video_title)

    if not os.path.exists(frames):
        os.makedirs(frames)

    if not os.path.exists(vid_dir):
        os.makedirs(vid_dir)

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


def frames_to_vid(in_dir, fps):  #
    frame_array = []
    files = [f for f in os.listdir(in_dir) if isfile(join(in_dir, f))]
    for i in range(0, len(files)):
        frame_name = in_dir + str(i) + '.jpg'
        img = cv2.imread(frame_name)
        height, width, layers = img.shape
        size = (width, height)
        frame_array.append(img)
    output = cv2.VideoWriter("voronoi_" + vid, cv2.VideoWriter_fourcc(*'DIVX'),
                             fps, size)
    for i in range(0, len(frame_array)):
        output.write(frame_array[i])
    output.release()


vid_to_frames(vid)
frames_to_vid(vid_dir, 25)
