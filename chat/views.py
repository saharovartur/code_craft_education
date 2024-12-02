from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render


@login_required
def course_chat_room(request, course_id):
    try:
        course = request.user.courses_joined.get(id=course_id) # извлечь курс с заданным id к которому присоединился текущий юзер
    except:
        return HttpResponseForbidden()  # юзер не студент курса или курса не существует
    return render(request, 'chat/room.html', {'course': course})

