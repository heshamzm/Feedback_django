from django.db import models
from django.forms import fields
from django.forms.forms import Form
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView

# Create your views here.

# def store_file(file):         this function manually upload a file
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render (request, "profiles/create_profile.html", {
#             "form": form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request, request.FILES)

#         if submitted_form.is_valid():
#             profile  = UserProfile(image = request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
        
#         return render (request, "profiles/create_profile.html", {
#             "form": submitted_form
#         })
        