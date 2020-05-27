from django.conf.urls import url
from . import views

# The carrot symbol means start with, the dollar sign means end with
# This is going to look in our views file for a name of index
urlpatterns = [
    url(r'^$', views.index, name='index')
]
