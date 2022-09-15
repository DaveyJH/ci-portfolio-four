from django import forms
from .models import Review
from therapists.models import Therapist

RATINGS = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)


class CreateReviewForm(forms.ModelForm):
    """Form to add and edit Review"""
    class Meta:
        """Define model, form fields (and labels as needed)"""
        model = Review
        fields = [
            'title',
            'rating',
            'content',
            'therapist',
        ]

    def __init__(self, *args, **kwargs):
        """Only display therapists that are assigned to therapy"""
        super().__init__(*args, **kwargs)
        if 'therapy' in self.data:
            self.fields['therapist'].queryset = Therapist.objects.filter(
                therapies=self.data['therapy']
            )

    title = forms.CharField(max_length=30)
    rating = forms.Select(
        choices=RATINGS,
    )
    content = forms.CharField(
        max_length=220,
        widget=forms.Textarea(attrs={'rows': 4}),
    )
