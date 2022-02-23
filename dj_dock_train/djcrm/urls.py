from django.contrib import admin
from django.urls import path, include
from publications.views import LandingPageView
#from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('publications/', include('publications.urls', namespace="publications")),
]
