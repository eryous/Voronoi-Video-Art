from .models import Video
from .forms import VideoForm
from django.shortcuts import render
from voronoi_backend.video_voronoi import video_to_voronoi


def home(request):

    print("home at last")
    cur_vid = Video.objects.last()
    form = VideoForm(request.POST or None, request.FILES or None)

    vid_file_path = "../media/videos/IMG_7028.mp4"
    print(form.errors)
    if form.is_valid():
        if (cur_vid):
            vid_file_path = cur_vid.videofile
        else:
            data = form.cleaned_data
            file_name = data["name"]
            vid_file_path = "../media/videos/" + file_name

        print("IN HOME", vid_file_path)
        data = form.cleaned_data
        print(data)
        fps = data["fps"]
        name = data["name"]
        error_rate = data["error_rate"]
        form.save()

        video_to_voronoi(name, ".."+vid_file_path.url,
                         "../media/videos/", fps, error_rate)

    context = {'videofile': vid_file_path,
               'form': form,
               }

    return render(request, 'home.html', context)
