from django.contrib import admin
from authentication.models import Contact,MembershipPlan,Trainer,Enrollment



# Register your models here.
admin.site.register(Contact)
admin.site.register(MembershipPlan)
admin.site.register(Trainer)
admin.site.register(Enrollment)


