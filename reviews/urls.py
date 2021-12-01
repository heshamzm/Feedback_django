from django.urls import path
from . import views

# add urls and path for each view
urlpatterns = [
    path("",views.review)
]
