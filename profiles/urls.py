from profiles import views
from django.urls import path

urlpatterns = [
    path(
        'profile/<int:pk>/',
        views.UserProfileView.as_view(),
        name='user_profile'
    ),
]
