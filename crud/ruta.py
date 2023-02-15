from rest_framework import  routers
from .api import ProjectViewSet


router = routers.DefaultRouter()

router.register('crud/projects',ProjectViewSet,'crud')

urlpatterns = router.urls