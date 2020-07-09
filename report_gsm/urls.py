from django.urls import path
from .views import *


urlpatterns = [
    path('',Get_report.as_view(),name='get_gsm_report'),

]