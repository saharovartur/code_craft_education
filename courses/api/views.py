from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from courses.api.serializers import SubjectSerializer, CourseSerializer
from courses.models import Subject, Course


class SubjectListView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Список курсов + детальная инфо о курсе"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # Запись на курс
    @action(detail=True,
            methods=['post'],
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

## Первоначальная версия кода записи на курс
# class CourseEnrollView(APIView):
#     """Запись на курс"""
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk=pk)
#         course.students.add(request.user)
#         return Response({'enrolled': True})