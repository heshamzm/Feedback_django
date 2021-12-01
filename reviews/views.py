from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
import reviews

# Create your views here.
def review(request):
    if request.method == "POST":
        entered_username = request.POST['username']
        print(entered_username)
        return HttpResponseRedirect("/thank-you")
    
    return render(request, "reviews/review.html")


def thank_you(requset):

    return render(requset, "reviews/thank_you.html" )