from django.contrib import admin

from.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('location','total_price','quantity', 'order_created','date_updated')


admin.site.register(Order, OrderAdmin)
