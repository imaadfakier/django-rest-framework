from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from drf.serializers import StudentSerializer
from drf.models import Student
from rest_framework.permissions import IsAuthenticated

class TestView(APIView):
    '''...'''

    # ...

    permission_classes = (IsAuthenticated, )

    # GET
    def get(self, request, *args, **kwargs):
        # data = {
        #     'username': 'admin', 
        #     'years_active': 11,
        # }
        # return Response(data)

        query_set = Student.objects.all()
        student1 = query_set.first()
        # serializer = StudentSerializer(query_set, many=True)
        serializer = StudentSerializer(student1)
        return Response(serializer.data)
    
    # POST
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
