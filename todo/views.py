from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskFrom
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created')
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskFrom(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskFrom()
    return render(request, 'add_task.html', {'form':form})
    
@login_required
def delete_task(request, task_id):
    Task.objects.get(id=task_id, user=request.user).delete()
    return redirect('task_list')

@login_required
def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
