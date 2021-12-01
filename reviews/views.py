from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from reviews import forms

# Create your views here.
def review(request):
    
    if request.method == "POST":
        form = ReviewForm(request.POST) # get the values of the inputs

        if form.is_valid(): # check if the form is valid
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(requset):

    return render(requset, "reviews/thank_you.html" )