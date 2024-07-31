
from django.urls import path

from restapp2 import views
from restapp2.views import StudentListAPIView, student_list_view, student_update_view, student_delete_view, student_add

urlpatterns = [
    path('',views.student_list_view),
    path('get',views.getData),
    path('post/',views.postData),
    path('delete/<str:pk>/',views.deleteData),
    path('students/', student_list_view, name='student-list-view'),

    path('api/students/', StudentListAPIView.as_view(), name='student-list'),
    path('students/update/<int:stdid>/', student_update_view, name='student-update-view'),
    path('students/delete/<int:pk>/', student_delete_view, name='student-delete-view'),
    path('students/add',student_add, name='student-add'),
]
