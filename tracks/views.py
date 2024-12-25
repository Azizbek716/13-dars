from django.shortcuts import render, get_object_or_404, redirect
from .models import MusicTrack


def index(request):
    return render(request, 'index.html')


def music_list(request):
    tracks = MusicTrack.objects.all()
    return render(request, 'music_list.html', {'tracks': tracks})


def music_detail(request, id):
    track = get_object_or_404(MusicTrack, id=id)
    return render(request, 'music_detail.html', {'track': track})


def music_create(request):
    if request.method == 'POST':
        form = MusicTrack(request.POST)
        if form.is_valid():
            form.save()
            return redirect('music_list')
    else:
        form = MusicTrack()
    return render(request, 'music_create.html', {'form': form})


def music_update(request, id):
    track = get_object_or_404(MusicTrack, id=id)
    if request.method == 'POST':
        form = MusicTrack(request.POST, instance=track)
        if form.is_valid():
            form.save()
            return redirect('music_detail', id=track.id)
    else:
        form = MusicTrack(instance=track)
    return render(request, 'music_update.html', {'form': form})


def music_delete(request, id):
    track = get_object_or_404(MusicTrack, id=id)
    if request.method == 'POST':
        track.delete()
        return redirect('music_list')
    return render(request, 'music_delete_confirm.html', {'track': track})
