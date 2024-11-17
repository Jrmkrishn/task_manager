from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Task
from .forms import TaskForm
from django.contrib.auth import logout
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

@login_required
def task_list(request):
    # Only show tasks owned by the current user
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "tasks/task_list.html", {
        "tasks": tasks,
        "user": request.user
    })

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign current user as owner
            task.save()
            messages.success(request, "Task created successfully!")
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form})

@login_required
def task_edit(request, pk):
    # Use get_object_or_404 and ensure user owns the task
    task = get_object_or_404(Task, pk=pk)
    
    # Check if the user owns this task
    if task.user != request.user:
        logger.warning(f"Unauthorized access attempt to task {pk} by user {request.user.id}")
        raise PermissionDenied("You don't have permission to edit this task.")
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form": form, "task": task})

@login_required
def task_delete(request, pk):
    # Use get_object_or_404 and ensure user owns the task
    task = get_object_or_404(Task, pk=pk)
    
    # Check if the user owns this task
    if task.user != request.user:
        logger.warning(f"Unauthorized access attempt to delete task {pk} by user {request.user.id}")
        raise PermissionDenied("You don't have permission to delete this task.")
    
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect("task_list")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})

@login_required
def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect("/")