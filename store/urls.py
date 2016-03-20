from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^info/(?P<item_id>[0-9]+)$', views.info, name='info'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^add-to-cart/$', views.add, name='add'),
    url(r'^accounts/logout/$', views.account_logout, name='logout'),
    url(r'^accounts/login/$', views.accounts_login, name='login'),
    url(r'^accounts/profile/$', views.account_profile, name='profile'),
    url(r'^payment/success/$', views.paypal_success, name='success'),
]