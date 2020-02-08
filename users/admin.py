from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import AccountCreationForm, AccountChangeForm
from users.models import Account


class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = Account
    list_display = ['username', 'email']


admin.site.register(Account, AccountAdmin)