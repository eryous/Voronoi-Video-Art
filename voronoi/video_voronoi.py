import os
from os.path import isfile, join
from multiprocessing import Pool
import cv2
import numpy as np
from voronoi import voro

FRAMES = './frames/'


def video_to_frames(video_path, original_video_frames, voronoi_video_frames):
    capture = cv2.VideoCapture(video_path)

    if not os.path.exists(FRAMES):
        os.makedirs(FRAMES)

    if not os.path.exists(original_video_frames):
        os.makedirs(original_video_frames)

    if not os.path.exists(voronoi_video_frames):
        os.makedirs(voronoi_video_frames)

    current_frame = 0

    while (True):
        ret, frame = capture.read()
        if not ret:
            break

        name = original_video_frames + str(current_frame) + '.jpg'
        cv2.imwrite(name, frame)
        current_frame += 1
    capture.release()
    cv2.destroyAllWindows()


def generate_voronoi_multicore(video_frames_dir, voronoi_frame_dir, error_rate):
    """ Creates the voronoi video using all cores
    :returns: None. All processes write to file
    """

    original_frames = [f for f in os.listdir(
        video_frames_dir) if isfile(join(video_frames_dir, f))]
    input_voro = []
    for i in range(len(original_frames)):
        input_voro.append(
            (video_frames_dir + original_frames[i], original_frames[i][:-4], voronoi_frame_dir, error_rate))

    pool = Pool(30)
    pool.map(voro, input_voro)
    pool.close()


def frames_to_video(frame_source, video_dest_dir, fps, video_dir):
    frame_array = []
    files = [f for f in os.listdir(
        frame_source) if isfile(join(frame_source, f))]
    for i in range(len(files)):
        frame_name = str(i) + '.jpg'
        img = cv2.imread(frame_source+frame_name)
        height, width, layers = img.shape
        size = (width, height)
        frame_array.append(img)

    output = cv2.VideoWriter(video_dest_dir+"voronoi_" + video_dir, cv2.VideoWriter_fourcc(*'DIVX'),
                             fps, size)
    for i in range(len(frame_array)):
        output.write(frame_array[i])
    output.release()


def video_to_voronoi(video_name, from_path, to_path, fps, error_rate):
    """ Takes a video, runs voronoi, writes the result """

    original_video_frames = FRAMES + video_name + '/'
    voronoi_video_frames = FRAMES + "voro_" + video_name + '/'

    video_to_frames(from_path, FRAMES+video_name, to_path)
    generate_voronoi_multicore(
        original_video_frames, voronoi_video_frames, error_rate)
    frames_to_video(voronoi_video_frames, to_path, fps, video_name+".mp4")


if __name__ == "__main__":
    prompt_user = input("Enter the video you would like to 'Voronoi-fy': ")
    frames_per_second = int(input(
        "Enter the amount of frames per second you would like to see the final product in: "))
    error_rate = float(input(
        "Enter an error rate between .1 - .5, the smaller the rate, the more sampling is done: "))

    original_video_frames = FRAMES + prompt_user + '/'
    voronoi_video_frames = FRAMES + "voro_" + prompt_user + '/'
    video_name = prompt_user + '.mp4'

    print("Converting video to frames")
    video_to_frames(video_name, original_video_frames, voronoi_video_frames)

    print("Generating voronoi video")
    generate_voronoi_multicore(
        original_video_frames, voronoi_video_frames, error_rate)

    print("Writing voronoi video")
    frames_to_video(voronoi_video_frames, ".", frames_per_second, video_name)
