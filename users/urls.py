from django.conf.urls import url
from . import views
app_name = 'users'
urlpatterns = [
    url("^$", views.index, name="index"),
    url(r"^(?P<user_id>[0-9]+)/$", views.detail, name="detail"),
    
]
