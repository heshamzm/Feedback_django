from django.urls import path
from . import views

# add urls and path for each view
urlpatterns = [
    path("",views.ReviewView.as_view()), #this is how to add class path
    path("thank-you", views.thank_you) #this is how to add function path
]
