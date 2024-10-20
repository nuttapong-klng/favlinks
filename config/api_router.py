from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from favlinks.favorite_urls.api.views import CategoryViewSet
from favlinks.favorite_urls.api.views import FavoriteUrlViewSet
from favlinks.favorite_urls.api.views import TagViewSet
from favlinks.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("categories", CategoryViewSet)
router.register("favorite_urls", FavoriteUrlViewSet)
router.register("tags", TagViewSet)
router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
