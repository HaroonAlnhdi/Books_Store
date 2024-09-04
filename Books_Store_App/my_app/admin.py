from django.contrib import admin


from .models import *

admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(Review)
