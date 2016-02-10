from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'del/(?P<el_id>[0-9]+)',views.remove_element, name='del'),
    url(r'create-element',views.create_element, name='create-element'),
    url(r'update_element/(?P<el_id>[0-9]+)',views.update_element, name='update-element'),
]
