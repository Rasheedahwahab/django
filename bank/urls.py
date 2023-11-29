"""
URL configuration for bank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from tropical.views import home_view
from tropical.views import add_branch_view
from tropical.views import add_acc_type_view
from tropical.views import add_account_view
from tropical.views import edit_add_account_view
from tropical.views import delete_add_account_view
from tropical.views import edit_branch_view
from tropical.views import delete_add_branch_view
from tropical.views import  edit_acc_view
from tropical.views import delete_add_acc_view
from tropical.views import delete_customer_view
from tropical.views import add_customer_view
from tropical.views import edit_customer_view
from tropical.views import delete_transaction_view
from tropical.views import add_transaction_view
from tropical.views import edit_transaction_view
from tropical.views import sign_up_view
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('sign_up/', sign_up_view,name='sign_up'),
     path('accounts/',include('django.contrib.auth.urls')),
    path('add_account/', add_account_view,name='add_account'),
    path('edit_add_account/<int:account_id>/', edit_add_account_view,name='edit_add_account'),
    path('delete_add_account/<int:account_id>/', delete_add_account_view,name='delete_add_account'),
    path('branch/',add_branch_view,name='add_branch'),
    path('edit_branch/<int:branch_id>/', edit_branch_view,name='edit_branch'),
    path('delete_add_branch/<int:branch_id>/', delete_add_branch_view,name='delete_add_branch'),
    path('acc_type/',add_acc_type_view,name='add_acc_type'),
    path('edit_acc/<int:account_type_id>/', edit_acc_view,name='edit_acc_type'),
    path('delete_add_acc/<int:account_type_id>/', delete_add_acc_view,name='delete_add_acc'),
    path('customer/',add_customer_view,name='add_customer'),
    path('edit_customer/<int:customer_id>/', edit_customer_view,name='edit_customer'),
    path('delete_customer/<int:customer_id>/', delete_customer_view,name='delete_customer'),
     path('transaction/',add_transaction_view,name='add_transaction'),
    path('edit_transaction/<int:transaction_id>/', edit_transaction_view,name='edit_transaction'),
    path('delete_transaction/<int:transaction_id>/', delete_transaction_view,name='delete_transaction'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

