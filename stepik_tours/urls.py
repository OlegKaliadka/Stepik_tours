
from django.contrib import admin
from django.urls import path

from tours.views import MainView, custom_handler404
from tours.views import DepartureView
from tours.views import TourView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('departure/<str:departure>/', DepartureView.as_view(), name='departure'),
    path('tour/<int:id>/', TourView.as_view(), name='tour'),
    path('admin/', admin.site.urls),
]

handler404 = custom_handler404