# Generated by Django 4.0.4 on 2022-08-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogroopa', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(blank=True, help_text='submit image', null=True, upload_to='')),
                ('submitted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]