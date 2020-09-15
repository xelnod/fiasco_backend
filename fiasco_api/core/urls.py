from django.contrib import admin
from django.urls import path, include
from core.views import RegisterView
from rest_framework.routers import SimpleRouter

# router = SimpleRouter()
# router.register(r'build', BuildViewSet, base_name='build')
# urlpatterns = router.urls

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('register/', RegisterView.as_view()),

    path('cats/', include('categories.urls')),
    path('channels/', include('channels.urls')),
    path('colors/', include('colorizer.urls')),
    path('e/', include('expenses.urls')),
    path('tags/', include('tags.urls')),

]
