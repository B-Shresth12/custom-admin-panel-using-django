from django.db import models
from django.core.validators import MinLengthValidator


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
    logo = models.ImageField(blank=True, null=True)
    favicon = models.ImageField(blank=True, null=True)
    apple_touch = models.ImageField(blank=True, null=True)

    def __str__(self):
        return "Site Settings"
