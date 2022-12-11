from rest_framework.routers import DefaultRouter
from core.api.views import PostApiViewSet

router_post = DefaultRouter()

router_post.register(prefix='seguimientos', basename='seguimiento', viewset=PostApiViewSet)