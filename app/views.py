from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class TagScan(APIView):
    def get(self, request):
        tags = TagReader.objects.all()
        serializer = TagScanSerializer(tags, many=True)
        return Response({'tags':serializer.data})

    def post(self, request):
        tag = request.data.get("body")
        serializer = TagScanSerializer(data=tag)
        if serializer.is_valid(raise_exception=True):
            tag_saved = serializer.save()
            print(tag_saved)
            # print('Succes ', tag_saved.student)
            return Response(tag_saved)
        return Response('error')


class TagRegistration(APIView):
    def get(self, request):

        tags = TagRegister.objects.all()
        serializer = TagRegisterSerializer(tags, many=True)
        return Response({'tags': serializer.data})

    def post(self, request):
        tag = request.data.get("body")
        serializer = TagRegisterSerializer(data=tag)
        if serializer.is_valid(raise_exception=True):
            tag_saved = serializer.save()
            print(tag_saved)
            return Response(tag_saved)
        return Response('error')


def index(request):
    students = Student.objects.order_by('name')
    groups = Group.objects.all()
    scan_count = TagReader.objects.order_by('scanned')
    context = {'students': students,
               'groups' : groups,
               'scan_count' : scan_count}
    return render(request, 'index.html', context)


'''

register
{
    "body": 
        {
            "tag": "mitka",
    "student":""
        }
    
}


scan
{
    "body": 
        {
            "tag": "mitka",
    "student":"",
"scanned":null
        }
    
}
'''