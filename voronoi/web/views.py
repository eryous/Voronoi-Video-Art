from .models import Video
from .forms import VideoForm
from django.shortcuts import render


def home(request):
    cur_vid = Video.objects.last()
    vid_file_path = cur_vid.videofile.url

    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'videofile': vid_file_path,
               'form': form,
               'cur_vid': cur_vid
               }

    return render(request, 'home.html', context)
