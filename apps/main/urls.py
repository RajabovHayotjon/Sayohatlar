from django.urls import path
from apps.main.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]
