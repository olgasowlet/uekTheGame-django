from rest_framework import routers

from quests.views import QuestsViewSet

router = routers.DefaultRouter()
router.register(r'', QuestsViewSet, basename='quests')

urlpatterns = router.urls
