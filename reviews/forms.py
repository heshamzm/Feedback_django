from django import forms
from django.forms import fields
from .models import Review
# class ReviewForm(forms.Form): # creat from from djanjo form
#     user_name = forms.CharField(label="your name", max_length=100, error_messages={
#         "required":"Your name must not be empty",
#         "max_length":"please enter a shorter name"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm): #create a from from an existing model
    class Meta:
        model = Review
        # fields = ['user_name', 'review_text', 'rating'] # what filed showd be rendered
        fields = '__all__'   #include all the fields
        # exclude = ['user_name'] # not include a fields.