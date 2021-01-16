from django.conf.urls import  url
from django.urls import re_path

from healthnet import views
from healthnet import views_admin
from healthnet import views_admission
from healthnet import views_appointment
from healthnet import views_medtest
from healthnet import views_message
from healthnet import views_prescription
from healthnet import views_profile
from healthnet import views_medicalInfo

app_name = 'healthnet'
urlpatterns = [
                       re_path(r'^$', views.login_view, name='index'),
                       re_path(r'^logout/$', views.logout_view, name='logout'),
                       re_path(r'^register/$', views.register_view, name='register'),

                       #re_path(r'^message/list/$', views_message.message_view, name='message/list'),
                       #re_path(r'^message/read/$', views_message.read_view, name='message/read'),
                       #re_path(r'^message/new/$', views_message.new_view, name='message/new'),

                       re_path(r'^admin/users/$', views_admin.users_view, name='admin/users'),
                       re_path(r'^admin/activity/$', views_admin.activity_view, name='admin/activity'),
                       re_path(r'^admin/stats/$', views_admin.statistic_view, name='admin/stats'),
                       re_path(r'^admin/createemployee/$', views_admin.createemployee_view, name='admin/createemployee'),

                       re_path(r'^message/list/$', views_message.list_view, name='message/list'),
                       re_path(r'^message/new/$', views_message.new_view, name='message/new'),
                       re_path(r'^message/read/$', views_message.read_view, name='message/read'),

                       re_path(r'^appointment/list/$', views_appointment.list_view, name='appointment/list'),
                       re_path(r'^appointment/update/$', views_appointment.update_view, name='appointment/update'),
                       re_path(r'^appointment/create/$', views_appointment.create_view, name='appointment/create'),
                       re_path(r'^appointment/cancel/$', views_appointment.cancel_view, name='appointment/cancel'),

                       re_path(r'^profile/$', views_profile.profile_view, name='profile'),
                       re_path(r'^profile/update/$', views_profile.update_view, name='profile/update'),
                       re_path(r'^profile/password/$', views_profile.password_view, name='profile/password'),

                       re_path(r'^medtest/upload/$', views_medtest.create_view, name='medtest/upload'),
                       re_path(r'^medtest/list/$', views_medtest.list_view, name='medtest/list'),
                       re_path(r'^medtest/display/$', views_medtest.display_view, name='medtest/display'),
                       re_path(r'^medtest/update/$', views_medtest.update_view, name='medtest/update'),

                       re_path(r'^admission/admit/$', views_admission.admit_view, name='admission/admit'),
                       re_path(r'^admission/list/$', views_admission.list_view, name='admission/list'),
                       re_path(r'^admission/discharge/$', views_admission.discharge_view, name='admission/discharge'),

                       re_path(r'^error/denied/$', views.error_denied_view, name='error/denied'),

                       re_path(r'^prescription/create/$', views_prescription.create_view, name='prescription/create'),
                       re_path(r'^prescription/list/$', views_prescription.list_view, name='prescription/list'),
                       re_path(r'^prescription/delete/$', views_prescription.delete_view, name='prescription/delete'),

                       re_path(r'^medicalinfo/list/$', views_medicalInfo.list_view, name='medicalinfo/list'),
                       re_path(r'^medicalinfo/update/$', views_medicalInfo.update_view, name='medicalinfo/update'),
                       re_path(r'^medicalinfo/patient/$', views_medicalInfo.patient_view, name='medicalinfo/patient'),
]