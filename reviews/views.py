from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from reviews import forms
from .models import Review

# Create your views here.
def review(request):
    
    if request.method == "POST":
        form = ReviewForm(request.POST) # get the values of the inputs

        if form.is_valid(): # check if the form is valid
            review = Review(user_name = form.cleaned_data['user_name'], # save the inputs to the database. 
                review_text = form.cleaned_data['review_text'], 
                rating = form.cleaned_data['rating'])
            review.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
        return render(request, "reviews/review.html", {
            "form": form
    })


def thank_you(requset):

    return render(requset, "reviews/thank_you.html" )