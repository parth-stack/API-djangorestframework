from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/insert/', views.insert),
    path('api/v1/display/<product>/', views.display),
]