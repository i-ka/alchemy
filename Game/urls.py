from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
import django

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$',
        auth_views.login,
        {"template_name": "Game/loginform.html"},
        name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'get-elements-by-category/(?P<category_id>[0-9]+)',
        views.element_list, name='get-elements-by-cat'),
    url(r'get_categories', views.get_categories, name='get_categories'),
    url(r'^new-login/$', views.login_view, name='new-login'),
    url(r'check_element', views.check_element, name='check_element'),
    url(r'get-open-elements-by-category/(?P<category_id>[0-9]+)',
        views.get_user_open_element_list, name='get-open-elements-by-cat'),
    ]