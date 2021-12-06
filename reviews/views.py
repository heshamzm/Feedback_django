from django import views
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import FormView

import reviews
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
# Create your views here.


class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html" # these two line of code replace the get method in the function below.
    success_url = "/thank-you" # what to do after the success.

    def form_valid(self, form):
        form.save() #save the input to database.
        return super().form_valid(form)

# !!! the class above is spicified for the Forms it replace the class below

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()

#         return render(request, "reviews/review.html", {
#             "form": form
#             })
#     def post(self, request):
        
#         form = ReviewForm(request.POST) #instance = existing_model # get the values of the inputs/ the instance is for updating the data if using the from model.

#         if form.is_valid(): # check if the form is valid
#             form.save() # this is an easy way to save data into the database if using a model form.
#             return HttpResponseRedirect("/thank-you")

#         return render(request, "reviews/review.html", {
#             "form": form
#             })

## !!! the class above is the same functionality as the function below, but without if statments.

# def review(request):
    
#     if request.method == "POST":
#         # existing_model = Review.objects.get(pk = 1)
#         form = ReviewForm(request.POST) #instance = existing_model # get the values of the inputs/ the instance is for updating the data if using the from model.

#         if form.is_valid(): # check if the form is valid
#             form.save() # this is an easy way to save data into the database if using a model form.
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {
#             "form": form
#     })


class Thank_you(TemplateView): #this TemplateView is for rendering template without calling the get method.
    template_name = "reviews/thank_you.html"
# !!!! the class above do the same functionality as the function below.

# def thank_you(requset):
#     return render(requset, "reviews/thank_you.html" )


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review # fetch all the data from model.
    context_object_name = "reviews" #name the fetched object to use it in the template

    # def get_queryset(self): this function querey the model on spicific
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data



class ReviewDetailsView(DetailView): # this function is to fetch a spicific data.
    template_name = "reviews/review_details.html"
    model = Review




    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"] #get the id from the selcted review.
    #     review = Review.objects.get(pk = review_id) #fetch the review from the database.
    #     context["review"] = review 
    #     return context


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review "] = fav_review
        return HttpResponseRedirect("/reviews/" + review_id)