from django.db import models
import uuid
class Video(models.Model):
   title = models.CharField(max_length=100)
   mp4_file = models.CharField(max_length=255)  # Update the field type to CharField
   vtt_file = models.CharField(max_length=255)  # Update the field type to CharField
   gif_file = models.CharField(max_length=255)  # Update the field type to CharField
   thumbnail_file = models.CharField(max_length=255)  # Update the field type to CharField
   description = models.TextField(default="No description available"
)
   # uuid = models.CharField(max_length=100)

class Videoprocess(models.Model):
   uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   title = models.CharField(max_length=100)
   description = models.TextField(default="No description available"
)

# video = Video.objects.create(
#    title='Ampere_AI_1080p',
#    mp4_file='Ampere_AI_1080p/h265/Ampere_AI_1080p_720p.mp4',
#    vtt_file='Ampere_AI_1080p/webvtt/Ampere_AI_1080p.en_US.vtt',
#    gif_file='Ampere_AI_1080p/gif/ani-preview.gif',
#    thumbnail_file='Ampere_AI_1080p/gif/thumbnail.gif'
# )

# video = Video.objects.create(
#    title='Ampere_AIC_1080p',
#    mp4_file='Ampere_AIC_1080p/h265/Ampere_AIC_1080p_720p.mp4',
#    vtt_file='Ampere_AIC_1080p/webvtt/Ampere_AIC_1080p.en_US.vtt',
#    gif_file='Ampere_AIC_1080p/gif/ani-preview.gif',
#    thumbnail_file='Ampere_AIC_1080p/gif/thumbnail.gif'
# )

