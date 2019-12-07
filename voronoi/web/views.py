from .models import Video
from .forms import VideoForm
from django.shortcuts import render


def home(request):
    cur_vid = Video.objects.last()

    if (cur_vid):
        vid_file_path = cur_vid.videofile
    else:
        vid_file_path = "love.gif"
    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'videofile': vid_file_path,
               'form': form
               }

    return render(request, 'home.html', context)
