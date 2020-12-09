from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer
from rest_framework.views import View

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(View):
    def get(self, request, *args, **kwargs):
        teacher = get_object_or_404(Teacher, pk=kwargs['id'])
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        teacher = get_object_or_404(Teacher, pk=kwargs['id'])
        serializer = TeacherSerializer(teacher, data=request.data, partial=True)
        if serializer.is_valid():
            teacher = serializer.save()
            return Response(TeacherSerializer(teacher).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        teacher = get_object_or_404(Teacher, pk=kwargs['id'])
        teacher.delete()
        return Response("Name deleted", status=status.HTTP_204_NO_CONTENT)
