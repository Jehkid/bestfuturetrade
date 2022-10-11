from django.contrib import admin
from .models import  investment, investors_depo, investors_payed, percentage,testimonial,profile,payment1,wallet,withdraw,Contact,investors_depo,investors_payed,percentage
# Register your models here.
admin.site.register(testimonial)
admin.site.register(profile)
admin.site.register(payment1)
admin.site.register(wallet)
admin.site.register(investment)
admin.site.register(withdraw)
admin.site.register(Contact)
admin.site.register(investors_depo)
admin.site.register(investors_payed)
admin.site.register(percentage)




