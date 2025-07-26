from django.contrib import admin

# Register your models here.


from .models import Registration
admin.site.register(Registration)

from .models import Feedback
admin.site.register(Feedback)

from .models import Payment
admin.site.register(Payment)



