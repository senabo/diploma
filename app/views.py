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
        return Response({'tags': serializer.data})

    def post(self, request):
        tag = request.data.get("body")
        serializer = TagScanSerializer(data=tag)
        if serializer.is_valid(raise_exception=True):
            tag_saved = serializer.save()
            print(tag_saved)
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
    for s in students:
        s.number_scan = s.tags.all().count()
        s.save()

    context = {'students': students,
               'groups': groups,
               }

    return render(request, 'index.html', context)


def student_detail(request, pk, ):
    scans_object = TagReader.objects.filter(student=pk)
    if not scans_object.exists():
        name = Student.objects.get(pk=pk)
    else:
        name = scans_object.first().student

    show_all = request.GET.get('show_all')
    if show_all != "1":
        paginator = Paginator(scans_object, 12)
    else:
        paginator = Paginator(scans_object, scans_object.count())

    page = request.GET.get('page')
    try:
        scans = paginator.page(page)
    except PageNotAnInteger:
        scans = paginator.page(1)
    except EmptyPage:
        scans = paginator.page(paginator.num_pages)

    context = {'scans': scans,
               'name': name,
               'page': page,
               'show_all': show_all,
               }

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
