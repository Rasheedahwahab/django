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
from django.urls import path
from tropical.views import home_view
from tropical.views import account_view
from tropical.views import branch_view
from tropical.views import transaction_view
from tropical.views import acc_type_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('account/', account_view ,  name='account'),
    path('branch/', branch_view, name='branch'),
    path('transaction/', transaction_view, name='transaction'),
    path('acc_type/', acc_type_view,name='acc_type'),
]
