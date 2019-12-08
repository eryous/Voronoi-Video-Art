from .models import Video
from .forms import VideoForm
from django.shortcuts import render
from voronoi_backend.video_voronoi import video_to_voronoi
import cv2


def home(request):

    cur_vid = Video.objects.all()[0]
    form = VideoForm(request.POST or None, request.FILES or None)
    print(cur_vid)
    vid_file_path = "../media/videos/IMG_7028.mp4"
    print(form.errors)

    vid_file_path = cur_vid.videofile
    if form.is_valid():
        # if (cur_vid):
            # vid_file_path = cur_vid.videofile
        # else:
            # data = form.cleaned_data
            # file_name = data["name"]
            # vid_file_path = "../media/videos/" + file_name

        print("IN HOME", vid_file_path)
        data = form.cleaned_data
        print(data)
        fps = data["fps"]
        name = data["name"]
        error_rate = data["error_rate"]
        form.save()

        capture = cv2.VideoCapture(vid_file_path.url[1:])

        video_to_voronoi(name, ".."+vid_file_path.url,
                         "media/videos/", fps, error_rate, capture)
    context = {'videofile': "media/videos/voronoi_"+name+".mp4",
               'form': form,
               }

    return render(request, 'home.html', context)
