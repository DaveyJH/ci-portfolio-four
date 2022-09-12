from django import forms
from cloudinary.models import CloudinaryField
from django.contrib.postgres.forms import SimpleArrayField
from .models import Therapy
from therapists.models import Therapist

BODY_AREAS = (
    (1, "Head"),
    (2, "Neck"),
    (3, "Shoulders"),
    (4, "Torso"),
    (5, "Upper Legs"),
    (6, "Lower Legs"),
    (7, "Buttocks"),
    (8, "Feet"),
    (9, "Full Body"),
    (10, "Upper Body"),
    (11, "Lower Body"),
    (12, "Back"),
)


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
            'image',
            'image_alt_text',
            'therapists',
            'duration_is_variable',
            'specialism',
        ]

    therapy_name = forms.CharField(max_length=40)
    body_area = forms.MultipleChoiceField(
        label='Body areas treated',
        choices=BODY_AREAS
    )
    benefits = SimpleArrayField(forms.CharField(max_length=50))
    description = forms.CharField(max_length=180)
    duration = forms.IntegerField(label="Duration in minutes")
    image = CloudinaryField('image')
    image_alt_text = forms.CharField(
        max_length=80,
        label="Accessibility description of image",
        required=False
    )
    therapists = forms.ModelMultipleChoiceField(
        queryset=Therapist.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    duration_is_variable = forms.BooleanField()
    specialism = forms.ModelMultipleChoiceField(
        queryset=Therapist.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
