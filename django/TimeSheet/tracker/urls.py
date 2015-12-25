from django.conf.urls import include, url
from tracker import views

urlpatterns = [
      url(r'^tracker/$', views.EmployeeList.as_view(), name="emp-list"),
      url(r'^tracker/(?P<pk>[0-9]+)/$', views.EmployeeDetail.as_view(), name="emp-detail"),
      url(r'^users/$',views.UserList.as_view(),name="user-list"),
      url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name="user-detail"),
      #url(r'^timesheet/(?P<user_id>[0-9])+/$', views.TimeSchedualList.as_view(), name="time-list"),
      url(r'^timesheet/(?P<pk>[0-9])+/$', views.TimeSheetList.as_view(), name="time-list"),
      url(r'^timesheet/(?P<pk>[0-9])+/'
          r'(?P<work_date>([0-9]{4}|[0-9]{2})[./-]([0]?[1-9]|[1][0-2])[./-]([0]?[1-9]|[1|2][0-9]|[3][0|1]))/$',
          views.TimeSheetDetail.as_view(), name="time-detail"),
      # url(r'^timesheet/(?P<pk>[0-9])+/'
      #     r'(?P<work_date>([0-9]{4}|[0-9]{2})[./-]([0]?[1-9]|[1][0-2])[./-]([0]?[1-9]|[1|2][0-9]|[3][0|1]))/$',
      #     views.TimeSchedualDetail.as_view(), name="time-detail"),
     # url(r'^timesheet/(?P<work_date>([0-9]{4}|[0-9]{2})[./-]([0]?[1-9]|[1][0-2])[./-]([0]?[1-9]|[1|2][0-9]|[3][0|1]))/$',
     #      views.TimeSchedualDetail.as_view(), name="time-detail"),
 ]

