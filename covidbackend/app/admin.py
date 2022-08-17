from django.contrib import admin
from .models import Register, Contact
# Register your models here.


class RegisterAdmin(admin.ModelAdmin):
    list_display= ('name', 'surname', 'email', 'phoneno', 'district', 'pincode', 'gender', 'adhaarno')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phoneno', 'symptoms', 'description')    
  
admin.site.register(Register, RegisterAdmin)
admin.site.register(Contact, ContactAdmin)

# admin.site.register(Register)
# admin.site.register(Contact)