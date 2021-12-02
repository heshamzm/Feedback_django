from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
            })
    def post(self, request):
        
        form = ReviewForm(request.POST) #instance = existing_model # get the values of the inputs/ the instance is for updating the data if using the from model.

        if form.is_valid(): # check if the form is valid
            form.save() # this is an easy way to save data into the database if using a model form.
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
            })

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


def thank_you(requset):

    return render(requset, "reviews/thank_you.html" )