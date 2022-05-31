from django.urls import path

from employee.views import CreateReadEmployeeView

urlpatterns = [
    path('', CreateReadEmployeeView.as_view(), name='employees')
]
