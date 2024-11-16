from django.contrib import admin
from django.urls import path, include
from tasks import views as task_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path("logout", task_views.logout_view, name="logout"),
    path("", task_views.task_list, name="task_list"),
    path("task/create/", task_views.task_create, name="task_create"),
    path("task/<int:pk>/edit/", task_views.task_edit, name="task_edit"),
    path("task/<int:pk>/delete/", task_views.task_delete, name="task_delete"),
]
