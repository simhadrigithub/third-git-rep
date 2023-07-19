from django.contrib import admin
from django.urls import path
from THIRDAPP.views import fine

urlpatterns = [
    path('admin/',admin.site.urls),
    path("",fine,name='fine'),
]
