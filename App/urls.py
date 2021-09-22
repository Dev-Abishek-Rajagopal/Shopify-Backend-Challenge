

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


from .views import (RepUserVeiwSet, ImgRepVeiwSet, search_ImgRep, ImgCartVeiwSet)

repuser = RepUserVeiwSet.as_view({
    'get' : 'list_RepUser',
    'post' : 'create_RepUser',
})

repuser_id = RepUserVeiwSet.as_view({
    'get' : 'get_RepUser',
    'put': 'update_RepUser',
    'delete': 'delete_RepUser'
})

imgrep = ImgRepVeiwSet.as_view({
    'get' : 'list_ImgRep',
    'post' : 'create_ImgRep',
})

imgrep_id = ImgRepVeiwSet.as_view({
    'get' : 'get_ImgRep',
    'put': 'update_ImgRep',
    'delete': 'delete_ImgRep'
})

imgcart = ImgCartVeiwSet.as_view({
    'get' : 'list_ImgCart',
    'post' : 'create_ImgCart',
})

imgcart_id = ImgCartVeiwSet.as_view({
    'get' : 'get_ImgCart',
    'put': 'update_ImgCart',
    'delete': 'delete_ImgCart'
})

# imgsearch = ImgRepVeiwSet.as_view({
#     'get' : 'search_ImgRep',
#
# })


urlpatterns = [
    url(r'^user/$', repuser),
    url(r'^user/(?P<pk>\d+)/$', repuser_id),
    url(r'^img/$', imgrep),
    url(r'^img/(?P<pk>\d+)/$', imgrep_id),
    url(r'^search/$', search_ImgRep),
    url(r'^cart/$', imgcart),
    url(r'^cart/(?P<pk>\d+)/$', imgcart_id),
]