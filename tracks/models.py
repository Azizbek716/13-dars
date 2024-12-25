from django.db import models
from django.shortcuts import reverse


class MusicTrack(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    duration = models.DurationField()
    cover_image = models.ImageField(upload_to='cover_images/', null=True, blank=True)
    audio_file = models.FileField(upload_to='audio_file/')

    def get_detail_url(self):
        return reverse('tracks:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('tracks:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('tracks:delete', args=[self.pk])