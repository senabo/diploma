from rest_framework import serializers
from .models import *
from django.db import IntegrityError




class TagScanSerializer(serializers.Serializer):
    tag = serializers.CharField()
    student = serializers.CharField(allow_blank=True)
    scanned = serializers.DateTimeField(allow_null=True)

    def create(self, validated_data):
        try:
            tag = validated_data['tag']
            student = TagRegister.objects.get(tag=tag).student
            print(student)
            res = TagReader.objects.create(tag=tag, student=student)
            return f'{student}'
        # return TagReader.objects.create(**validated_data)
        except TagRegister.DoesNotExist:
            return ('unknown tag')

class TagRegisterSerializer(serializers.Serializer):
    tag = serializers.CharField()
    student = serializers.CharField(allow_blank=True)

    def create(self, validated_data):
        try:
            res =  TagRegister.objects.create(tag=validated_data['tag'])
            return f'{res} saved'
        except IntegrityError:
            return ('already in database')
        except:
            return 'unknown error'
