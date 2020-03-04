from django.db import models


class Group(models.Model):
    group = models.CharField(verbose_name='група', max_length=120)

    def __str__(self):
        return self.group

    class Meta:
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'


class Student(models.Model):
    name = models.CharField(verbose_name='ім\'я', max_length=250)
    group = models.ForeignKey(Group, verbose_name='група', on_delete=models.CASCADE)
    number_scan = models.IntegerField(verbose_name='кількість сканувань', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенти'


class TagRegister(models.Model):
    tag = models.CharField(verbose_name='Мітка', max_length=120, unique=True)
    scanned = models.DateTimeField(verbose_name='Створено', auto_now_add=True)
    student = models.OneToOneField(Student, related_name='student_in_tag',verbose_name='Студент',null=True,blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ('-scanned',)
        verbose_name = 'Зареєстрована мітка'
        verbose_name_plural = 'Зареєстровані мітки'


class TagReader(models.Model):
    student = models.ForeignKey(Student, verbose_name='Студент',related_name = 'tags',  on_delete= models.CASCADE)
    tag = models.CharField(verbose_name='Мітка', max_length=120)
    scanned = models.DateTimeField(verbose_name='Проскановано', auto_now_add=True)

    def __str__(self):
        return self.scanned.astimezone().strftime('%d-%m-%Y | %H:%M')

    class Meta:
        ordering = ('-scanned',)
        verbose_name = 'Мітка відсканована'
        verbose_name_plural = 'Відскановані мітки'
