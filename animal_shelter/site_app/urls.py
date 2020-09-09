from django.urls import path
from . import views

urlpatterns = [
    path("", views.PetList.as_view()),
    path("pet/<str:pk>", views.PetDetails.as_view()),
    path("about", views.About.as_view()),
    path("recall", views.RecallList)
]