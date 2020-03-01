from django.contrib import admin
from .models import *


class MysiteAdmin(admin.AdminSite):
    index_title = 'Система контролю відвідуваності'
    site_header = 'Система контролю відвідуваності'
    site_title = 'Система контролю відвідуваності'


tracker_admin = MysiteAdmin(name="tracker_admin")


class TagRegisterInline(admin.StackedInline):
    model = TagRegister
    readonly_fields = ('tag',)
    # fields = ('tag',)


class TagReaderInline(admin.StackedInline):
    model = TagReader
    readonly_fields = ('tag',)
    extra = 0


class StudentInline(admin.TabularInline):
    model = Student
    readonly_fields = ('name',)
    extra = 0


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'number_scan')
    list_filter = ('group',)
    search_fields = ('name',)
    list_editable = ('group',)
    readonly_fields = ('number_scan',)
    inlines = (TagRegisterInline, TagReaderInline)
    # list_display_links = ('name','tag')


class TagReaderAdmin(admin.ModelAdmin):
    list_display = ('student', 'scanned', 'tag')
    list_filter = ('scanned',)
    search_fields = ('student',)
    readonly_fields = ('student', 'scanned', 'tag')
    # list_editable = ('group',)
    # list_display_links = ('name', 'tag')


class TagRegisterAdmin(admin.ModelAdmin):
    list_display = ('tag', 'student')
    list_filter = ('scanned',)
    list_editable = ('student',)
    readonly_fields = ('tag',)
    # search_fields = ('student',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('group',)
    inlines = (StudentInline,)


tracker_admin.register(Student, StudentAdmin)
tracker_admin.register(TagReader, TagReaderAdmin)
tracker_admin.register(TagRegister, TagRegisterAdmin)
tracker_admin.register(Group, GroupAdmin)
