from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from courses.services.mixins import OwnerCourseMixin, OwnerCourseEditMixin


class ManageCourseListView(PermissionRequiredMixin, OwnerCourseMixin, ListView):
    template_name = 'course/list.html'
    permission_required = 'courses.view_course'


class CourseCreateView(PermissionRequiredMixin, OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_course'


class CourseUpdateView(PermissionRequiredMixin, OwnerCourseEditMixin, UpdateView):
    permission_required = 'courses.change_course'


class CourseDeleteView(PermissionRequiredMixin, OwnerCourseMixin, DeleteView):
    template_name = 'course/delete.html'
    permission_required = 'courses.delete_course'

