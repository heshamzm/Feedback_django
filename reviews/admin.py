from django.contrib import admin
from .models import Review
# Register your models here.

class ReviewADmin(admin.ModelAdmin):
     list_display = ("user_name", "review_text")


admin.site.register(Review,ReviewADmin) # register the models to be shown in the admin.