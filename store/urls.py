from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),
    url(r'^info/', views.info, name='info'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^add-to-cart/$', views.add, name='add'),

    # url(r'^choose/$', views.choose_item, name='choose_item'),
    # url(r'^info/(?P<item_id>\d+)/$', views.info_by_item, name='info_by_item'),
    # url(r'^item/<slug>', ProductView.as_view(), name='product')
]
