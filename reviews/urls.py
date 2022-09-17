from reviews import views
from django.urls import path

urlpatterns = [
    path(
        'add_review/<int:pk>/',
        views.CreateReviewView.as_view(),
        name='add_review'
    ),
    path(
        'edit_review/<int:therapy_pk>/<int:pk>/',
        views.EditReviewView.as_view(),
        name='edit_review'
    ),
    path(
        'delete_review/<int:therapy_pk>/<int:pk>/',
        views.DeleteReviewView.as_view(),
        name='delete_review'
    ),
]
