from django import forms
from cloudinary.models import CloudinaryField
from django.contrib.postgres.forms import SimpleArrayField
from .models import Therapy, BodyArea
from therapists.models import Therapist


class CreateTherapyForm(forms.ModelForm):
    """Form to add and edit Therapy"""
    class Meta:
        """Define model, form fields (and labels as needed)"""
        model = Therapy
        fields = [
            'therapy_name',
            'body_area',
            'benefits',
            'description',
            'duration',
            'duration_is_variable',
            'image',
            'image_alt_text',
            'therapists',
            'specialism',
        ]

    therapy_name = forms.CharField(max_length=40)
    body_area = forms.ModelMultipleChoiceField(
        label='Body areas treated',
        queryset=BodyArea.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    benefits = SimpleArrayField(forms.CharField(max_length=50))
    description = forms.CharField(
        max_length=180,
        widget=forms.Textarea(attrs={'rows': 4}),
    )
    duration = forms.IntegerField(label="Duration in minutes")
    duration_is_variable = forms.BooleanField(required=False)
    image = CloudinaryField('image')
    image_alt_text = forms.CharField(
        max_length=80,
        label="Accessibility description of image",
        required=False,
    )
    therapists = forms.ModelMultipleChoiceField(
        queryset=Therapist.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )
    specialism = forms.ModelMultipleChoiceField(
        queryset=Therapist.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )
