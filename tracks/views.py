from django.shortcuts import render, get_object_or_404, redirect
from .models import MusicTrack


def index(request):
    return render(request, 'index.html')


def music_list(request):
    tracks = MusicTrack.objects.all()
    return render(request, 'tracks/music-list.html', {'tracks': tracks})


def music_detail(request, id):
    track = get_object_or_404(MusicTrack, id=id)
    return render(request, 'music-detail.html', {'track': track})


def music_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        genre = request.POST.get('genre')
        release_date = request.POST.get('release_date')
        duration = request.POST.get('duration')
        cover_image = request.FILES.get('cover_image')
        audio_file = request.FILES.get('audio_file')
        if title and artist and genre and release_date and duration and cover_image and audio_file:
            MusicTrack.objects.create(
                title=title,
                artist=artist,
                genre=genre,
                release_date=release_date,
                duration=duration,
                cover_image=cover_image,
                audio_file=audio_file,
            )
            form = MusicTrack()
        return render(request, 'music-create.html', {'form': form})



def music_update(request, id):
    track = get_object_or_404(MusicTrack, id=id)
    if request.method == 'POST':
        form = MusicTrack(request.POST, instance=track)
        if form.is_valid():
            form.save()
            return redirect('music_detail', id=track.id)
    else:
        form = MusicTrack(instance=track)
    return render(request, 'music-update.html', {'form': form})


def music_delete(request, id):
    track = get_object_or_404(MusicTrack, id=id)
    if request.method == 'POST':
        track.delete()
        return redirect('music_list')
    return render(request, 'music_delete_confirm.html', {'track': track})
