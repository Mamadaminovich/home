from django.http import JsonResponse
from .models import Employee, Branch
from django.shortcuts import render

def find_employee_branch(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        branch = employee.branch.name if employee.branch else None
        return JsonResponse({'branch': branch})
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)

def check_optional_car(request, branch_id):
    try:
        branch = Branch.objects.get(id=branch_id)
        optional_car = branch.optional_car_available
        return JsonResponse({'optional_car_available': optional_car})
    except Branch.DoesNotExist:
        return JsonResponse({'error': 'Branch not found'}, status=404)
    
def home(context):
    return render(context, "index.html", {})