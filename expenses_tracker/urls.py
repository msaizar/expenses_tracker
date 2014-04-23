from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from expenses.views import (
    ExpenseCreateView, IncomeCreateView, HomeView, TransferListView
)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'expenses_tracker.views.home', name='home'),
    # url(r'^expenses_tracker/', include('expenses_tracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', HomeView.as_view(), name='home'),


    url(r'^add-expense/$', ExpenseCreateView.as_view(), name='create_expense'),
    url(r'^add-income/$', IncomeCreateView.as_view(), name='create_income'),
    url(r'^all-transfers/$', TransferListView.as_view(), name='transfer_list'),
    # Uncomment the next line to enable the admin:
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    
    
    url(r'^admin/', include(admin.site.urls)),
)
