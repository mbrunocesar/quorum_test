from django.urls import path

from . import views

urlpatterns = [
    path("legislators", views.legislators_summary, name="Display legislators infos"),
    path("legislators/<str:output_format>", views.legislators_summary, name="Display legislators infos"),
    path("bills", views.bills_summary, name="Display bills infos"),
    path("bills/<str:output_format>", views.bills_summary, name="Display bills infos"),
]
