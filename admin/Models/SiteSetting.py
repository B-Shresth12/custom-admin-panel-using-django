from django.db import models
from django.core.validators import MinLengthValidator
import time

class SiteSetting(models.Model):
    site_name = models.TextField()
    site_email = models.EmailField()
    phone_number = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(10)
        ],
        null=True,
        blank=True
    )
    mobile_number = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(10)
        ],
        null=True,
        blank=True
    )
    whatsApp_number = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(10)
        ],
        null=True,
        blank=True
    )
    facebook_url = models.URLField(null=True, blank=True)
    youtube_url = models.URLField(null=True, blank=True)
    linkedIn_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    address = models.TextField()
    google_map_url = models.URLField(null=True, blank=True)
    meta_og_title = models.TextField()
    meta_og_description = models.TextField()
    og_image = models.ImageField(blank=True, null=True)
    logo = models.ImageField(upload_to="site-settings/", blank=True, null=True)
    favicon = models.ImageField(
        upload_to="site-settings/", blank=True, null=True)
    apple_touch = models.ImageField(
        upload_to="site-settings/", blank=True, null=True)

    def __str__(self):
        return "Site Settings"

    """
        Deleting Old files on saveing
    """

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = SiteSetting.objects.get(pk=self.pk)
            self._delete_old_file(old_instance.logo, self.logo)
            self._delete_old_file(old_instance.favicon, self.favicon)
            self._delete_old_file(old_instance.apple_touch, self.apple_touch)
            self._delete_old_file(old_instance.og_image, self.og_image)
        super().save(*args, **kwargs)

    def _delete_old_file(self, old_file, new_file):
        if old_file and old_file != new_file:
            max_attempts = 5
            for attempt in range(max_attempts):
                try:
                    old_file.delete(save=False)
                    break
                except PermissionError:
                    if attempt < max_attempts - 1:
                        time.sleep(1)
                    else:
                        raise
