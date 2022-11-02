from rest_framework import routers

from .api import MascotasviewSet

router=routers.DefaultRouter()
router.register('Api/Mascotas',MascotasviewSet, 'ApiMascotas')

urlpatterns=router.urls

