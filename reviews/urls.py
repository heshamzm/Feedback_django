from django.urls import path
from . import views

# add urls and path for each view
urlpatterns = [
    path("",views.ReviewView.as_view()), #this is how to add class path
    path("thank-you", views.Thank_you.as_view()), 
    path("review-list", views.ReviewsListView.as_view(), name="All-views"),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("review/<int:pk>", views.ReviewDetailsView.as_view(), name="review-details")
]
