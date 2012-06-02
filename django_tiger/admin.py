from django.contrib import admin

from .models import CreditCard, Subscription, Charge

class CCAdmin (admin.ModelAdmin):
  list_display = ('name', 'ctype', 'last4', 'expiration', 'active', 'created')
  search_fields = ('name', 'last4')
  list_filter = ('ctype', 'active')
  date_hierarchy = 'created'
  
class ChargeAdmin (admin.ModelAdmin):
  list_display = ('desc', 'Amount', 'Refunded', 'created', 'Actions')
  search_fields = ('desc',)
  date_hierarchy = 'created'
  raw_id_fields = ('card',)
  
  class Media:
    css = {"all": ()}
    js = ("tiger/admin_tiger.js",)
    
class SubAdmin (admin.ModelAdmin):
  list_display = ('plan_id', 'card', 'status', 'created')
  list_filter = ('status',)
  date_hierarchy = 'created'
  raw_id_fields = ('card',)
  
admin.site.register(CreditCard, CCAdmin)
admin.site.register(Charge, ChargeAdmin)
admin.site.register(Subscription, SubAdmin)
