from django.urls import path
from .import views

app_name = "delta"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:driver_id>', views.get_driver, name='driver')
]
