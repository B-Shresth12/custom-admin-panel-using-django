from django import forms
from ..Models.SiteSetting import *

# Validator
from django.core.exceptions import ValidationError


"""
This class model is for the updaing the basic data for site settings
"""


class SitesettingBasicForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        fields = [
            'site_name',
            'site_email',
            'phone_number',
            'mobile_number',
            'whatsApp_number',
            'facebook_url',
            'youtube_url',
            'linkedIn_url',
            'twitter_url',
            'instagram_url',
            'address',
            'google_map_url',
            'logo',
            'favicon'
        ]

    def clean_site_email(self):
        site_email = self.cleaned_data.get('site_email')
        if not site_email:
            raise ValidationError("Site Email is required")

        return site_email

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        if not mobile_number:
            raise ValidationError("Mobile Number is required")

        return mobile_number

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise ValidationError("Phone Number is required")

        return phone_number

    def clean_facebook_url(self):
        facebook_url = self.cleaned_data.get('facebook_url')
        if facebook_url and not facebook_url.startswith('https://facebook.com/'):
            raise ValidationError("Invalid Facebook URL.")
        return facebook_url

    def instagram_url(self):
        instagram_url = self.cleaned_data.get('instagram_url')
        if instagram_url and not instagram_url.startswith('https://instagram.com/'):
            raise ValidationError("Invalid Instagram URL.")

        return instagram_url

    def clean_youtube_url(self):
        youtube_url = self.cleaned_data.get('youtube_url')
        if youtube_url and not youtube_url.startswith('https://youtube.com/'):
            raise ValidationError("Invalid Youtube URL.")

        return youtube_url

    def clean_linkedIn_url(self):
        linkedIn_url = self.cleaned_data.get('linkedIn_url')
        if linkedIn_url and not linkedIn_url.startswith('https://linkedin.com/'):
            raise ValidationError("Invalid Linked In URL.")

        return linkedIn_url

    def clean_twitter_url(self):
        twitter_url = self.cleaned_data.get('twitter_url')
        if twitter_url and not (
            twitter_url.startswith('https://twitter.com/')
            or twitter_url.startswith('https://x.com/')
        ):
            raise ValidationError("Invalid Twitter URL.")

        return twitter_url

    def clean_logo(self):
        logo = self.cleaned_data.get('logo')
        if logo:
            ext = logo.name.split('.')[-1].lower()
            if ext not in ['png', 'jpg', 'jpeg']:
                raise ValidationError(
                    'File must be PNG, JPG, or JPEG')

        return logo

    def clean_favicon(self):
        favicon = self.cleaned_data.get('favicon')
        if favicon:
            ext = favicon.name.split('.')[-1].lower()
            if ext not in ['png', 'jpg', 'jpeg']:
                raise ValidationError(
                    'File must be PNG, JPG, or JPEG')

        return favicon

    def apple_touch(self):
        apple_touch = self.cleaned_data.get('apple_touch')
        if apple_touch:
            ext = apple_touch.name.split('.')[-1].lower()
            if ext not in ['png', 'jpg', 'jpeg']:
                raise ValidationError(
                    'File must be PNG, JPG, or JPEG')

        return apple_touch


"""
This class model is for the SEO options of the Site
"""


class SiteSettingSEOForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        fields = [
            'meta_og_title',
            'meta_og_description',
            'og_image',
        ]

        def clean_meta_og_title(self):
            meta_og_title = self.cleaned_data.get('meta_og_title')
            if not meta_og_title:
                raise ValidationError("Meta Og Title is required")

            return meta_og_title

        def clean_meta_og_description(self):
            meta_og_description = self.cleaned_data.get('meta_og_description')
            if not meta_og_description:
                raise ValidationError("Meta Og Title is required")

            return meta_og_description

        def clean_og_image(self):
            og_image = self.cleaned_data.get('og_image')
            if og_image:
                ext = og_image.name.split('.')[-1].lower()
                if ext not in ['png', 'jpg', 'jpeg']:
                    raise forms.ValidationError(
                        'File must be PNG, JPG, or JPEG')

            return og_image
