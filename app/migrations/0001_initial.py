# Generated by Django 3.0.3 on 2020-02-20 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=120, verbose_name='група')),
            ],
            options={
                'verbose_name': 'Група',
                'verbose_name_plural': 'Групи',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name="ім'я")),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Group', verbose_name='група')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенти',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='TagRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=120, unique=True, verbose_name='Мітка')),
                ('scanned', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('student', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_in_tag', to='app.Student', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Зареєстрована мітка',
                'verbose_name_plural': 'Зареєстровані мітки',
                'ordering': ('-scanned',),
            },
        ),
        migrations.CreateModel(
            name='TagReader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=120, verbose_name='Мітка')),
                ('scanned', models.DateTimeField(auto_now_add=True, verbose_name='Проскановано')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='app.Student', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Відсканована мітка',
                'verbose_name_plural': 'Відскановані мітки',
                'ordering': ('-scanned',),
            },
        ),
    ]
