from django.urls import path
from .migrations.views import student


urlpatterns = [
    path("students/create/", student.create, name='student-create'),
    path("students/", student.list_all, name='student-list'),
    path("students/<int:pk>/", student.detail, name='student-detail'),
    path("students/<int:pk>/update/", student.update, name='student-update'),
    path("student/<int:pk>/delete/", student.delete, name='student-delete')
]