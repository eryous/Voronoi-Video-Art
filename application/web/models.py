from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(
        upload_to='videos/', null=True, verbose_name="")
    fps = models.IntegerField(null=True)
    error_rate = models.DecimalField(
        null=True, decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.videofile)
