from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import UserFeedView

from .views import LikePostView, UnlikePostView


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),  # Ensure this is added
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),  # Ensure this is added
    path('feed/', UserFeedView.as_view(), name='user-feed'),
]
