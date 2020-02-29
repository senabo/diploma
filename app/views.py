from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    students = Student.objects.order_by('-number_scan')
    groups = Group.objects.all()
    scan_count = TagReader.objects.order_by('-scanned')

    for s in students:
        s.number_scan = scan_count.filter(student=s.id).count()
        s.save()

    context = {'students': students,
               'groups': groups,
               }

    return render(request, 'index.html', context)


def student_detail(request, pk):
    scans_object = TagReader.objects.filter(student=pk)
    name = Student.objects.get(pk=pk)
    paginator = Paginator(scans_object, 15)
    page = request.GET.get('page')
    try:
        scans = paginator.page(page)
    except PageNotAnInteger:
        scans = paginator.page(1)
    except EmptyPage:
        scans = paginator.page(paginator.num_pages)
    context = {'scans':scans,
               'name':name,
               'page':page}
    return render(request, 'student.html', context)

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

# {"body":{"tag": "mitka","student": "","scanned": null}}