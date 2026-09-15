from django.urls import path
from . import views

app_name = "social"

urlpatterns = [
    path('', views.feed, name='feed'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('u/<str:username>/', views.profile, name='profile'),
    path('u/<str:username>/follow/', views.toggle_follow, name='toggle_follow'),
    path('members/', views.member_list, name='members'),
    path('int/<pk>/', views.post_detail, name='post_detail'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('message/<int:pk>/delete/', views.delete_message, name='delete_message'),
]