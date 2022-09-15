from reviews import views
from django.urls import path

urlpatterns = [
    path(
        'add_review/<int:pk>/',
        views.CreateReviewView.as_view(),
        name='add_review'
    ),
]
