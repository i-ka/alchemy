from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'del/(?P<el_id>[0-9]+)', views.remove_element, name='del'),
    url(r'create-element', views.create_element, name='create-element'),
    url(r'update_element/(?P<el_id>[0-9]+)',
        views.update_element, name='update-element'),
    url(r'elements-list', views.elements_list, name='elements-list'),
    url(r'feedback-list', views.feedback_list, name='feedback-list'),
    url(r'users-list', views.users_list, name='users-list'),
    url(r'create-category', views.create_category, name='create-category'),
]
