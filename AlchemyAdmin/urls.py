from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'del/(?P<el_id>[0-9]+)', views.remove_element, name='del'),
    url(r'create-element', views.create_element, name='create-element'),
    url(r'update_element/(?P<el_id>[0-9]+)',
        views.update_element, name='update-element'),
    url(r'elements-list', views.elements_list, name='elements-list'),
    url(r'feedback-list/(?P<filter>[a-z]*)', views.feedback_list, name='feedback-list'),
    url(r'users-list', views.users_list, name='users-list'),
    url(r'create-category', views.create_category, name='create-category'),
    url(r'set-user-active/(?P<userId>[0-9]+)/(?P<active>[0-9])', views.set_user_active, name='set-user-active'),
    url(r'set-report/(?P<reportId>[0-9]+)/(?P<val>[(accepted) (rejected)]+)', views.set_report, name='set-report'),
    url(r'report-details/(?P<reportId>[0-9]+)', views.report_details, name='report-details'),
    url(r'delete-report/(?P<reportId>[0-9]+)', views.delete_report, name='delete-report'),
    url(r'get-elements-by-category/(?P<category_id>[0-9]+)', views.element_list, name='get-elements-by-cat'),
]
