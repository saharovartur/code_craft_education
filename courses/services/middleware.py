from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from courses.models import Course


def subdomain_course_middleware(get_response):
    """
    Поддомены курсов
    :param get_response:
    """
    def middleware(request):
        host_parts = request.get_host().split('.')
        if len(host_parts) > 2 and host_parts[0] != 'www':
            course = get_object_or_404(Course, slug=host_parts[0])  # Получить курс для заданного поддомена
            course_url = reverse('course_detail',
                                 args=[course.slug])

            url = '{}://{}{}'.format(request.scheme,
                                     '.'.join(host_parts[1:]),
                                     course_url)
            return redirect(url)
        response = get_response(request)
        return response
    return middleware


