from django.contrib import admin
from myapp.models import Member, Product,Appointment

# Register your models here.
admin.site.register(Member)
admin.site.register(Product)
admin.site.register(Appointment)

