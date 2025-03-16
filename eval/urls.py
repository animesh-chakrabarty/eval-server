from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth', include('users.urls')),
    path('api/contest', include('contest.urls')),
    path('api/evaluate', include('evaluation.urls')),
    path('api/proctor', include('proctor.urls')),
]
