# Generated by Django 4.2 on 2024-09-29 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=30, verbose_name='Word')),
                ('mean', models.TextField(max_length=400, verbose_name='意味')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
