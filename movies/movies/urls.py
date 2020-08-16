from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("movie.urls")),
    # path('register/', views.Register.as_view(), name="register"),
]
