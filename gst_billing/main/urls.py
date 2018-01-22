from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^create/', views.add_new_item_form, name='add_new_form'),
    url(r'^inventory/', views.inventory, name='inventory'),
    url(r'^updateItem/', views.Update_current_item, name="update_current_item"),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
]