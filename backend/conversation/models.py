from django.db import models
from users.models import ApplicationUser
from date.models import Date
from django.utils.text import slugify

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "../data/user_{0}/{1}".format(instance.username, filename)


class Conversation(Date):
    username = models.ForeignKey(ApplicationUser, to_field='username', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    title_slug = models.SlugField(blank=True)
    pdf_file = models.FileField(blank=True, upload_to=user_directory_path)
    embedding_cache = models.JSONField(default=dict, null=True, blank=True, help_text="Stores cached embedding vectors for the PDF file.")

    def save(self, *args, **kwargs):
        if not self.title_slug:
            self.title_slug = slugify(self.title)
        super(Conversation, self).save(*args, **kwargs)