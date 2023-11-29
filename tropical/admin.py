from django.contrib import admin

from .models import Branch,Account,Account_type

class BranchAdmin(admin.ModelAdmin):
    list_display = ("name","location","manager")
admin.site.register(Branch, BranchAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ("account_number","opening_date","account_balance","status")
admin.site.register(Account, AccountAdmin)

class Account_typeAdmin(admin.ModelAdmin):
    list_display = ("name","description")
admin.site.register(Account_type, Account_typeAdmin)

