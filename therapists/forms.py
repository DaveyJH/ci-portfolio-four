from django import forms
from .models import Therapist
from cloudinary.models import CloudinaryField


class CreateTherapistForm(forms.ModelForm):
    """
    Form to edit and delete menus
    """
    class Meta:
        """
        Define model, form fields and label
        """
        model = Therapist
        fields = [
            'first_name',
            'last_name',
            'bio',
            'image',
            'image_alt_text',
            'hourly_rate',
        ]

    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    bio = forms.CharField(
        max_length=240, widget=forms.Textarea(attrs={'rows': 4}),
    )
    image = CloudinaryField('image')
    image_alt_text = forms.CharField(
        max_length=80,
        label="Accessibility description of image",
        required=False
    )
    hourly_rate = forms.IntegerField(max_value=100)
