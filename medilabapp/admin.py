from django.contrib import admin
from medilabapp.models import product,student,Patient,company,Appointment,Member

# Register your models here.
admin.site.register(product)
admin.site.register(student)
admin.site.register(Patient)
admin.site.register(company)
admin.site.register(Appointment)
admin.site.register(Member)



