from django.shortcuts import render, redirect
from .forms import EmployeeForm

def employee_form_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_success')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})



def employee_success_view(request):
    return render(request, 'employee_sucess.html')  # Render the success template
from django.shortcuts import render, get_object_or_404
from .models import Employee

# View to list all employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

# View to show details of a specific employee
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

