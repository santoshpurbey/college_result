from django.conf.urls import url

from .views import index, ManageStudentView

urlpatterns=[
url(r'^$', index, name='index'),
url(r'^add/student/$', ManageStudentView.as_view(), name='add-student' ),
]