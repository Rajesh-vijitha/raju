from django.urls import path
from .views import *

urlpatterns = [
    path('',fruit_app_landingpage,name="fr_lp"),
    path('fruit/', fruit_view, name="fruit"),
    path('places/',places_view,name="places")
]