from django.urls import path
from . import views
from .views import FollowUserView, UnfollowUserView  # Import the class-based views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='profile'),
    # Use class-based views for follow/unfollow
    path('follow/', FollowUserView.as_view(), name='follow'),
    path('unfollow/', UnfollowUserView.as_view(), name='unfollow'),
    path('follow-user/', views.follow_user, name='follow-user'),
    path('unfollow-user/', views.unfollow_user, name='unfollow-user'),
    path('profile/<int:user_id>/', views.user_profile_with_follow_info, name='user-profile'),
    path('following/', views.following_list, name='following-list'),
    path('followers/', views.followers_list, name='followers-list'),
    path('follow/<int:user_id>/', views.follow_user_by_id, name='follow-by-id'),
    path('unfollow/<int:user_id>/', views.unfollow_user_by_id, name='unfollow-by-id'),
]

