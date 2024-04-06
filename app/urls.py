from django.urls import path
from . import views

urlpatterns = [
    path('find_employee_branch/<int:employee_id>/', views.find_employee_branch, name='find_employee_branch'),
    path('check_optional_car/<int:branch_id>/', views.check_optional_car, name='check_optional_car'),
]