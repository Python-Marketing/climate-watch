# Generated by Django 2.2.16 on 2020-10-13 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('djangocms_blog', '0002_auto_20200929_2310'),
        ('cms', '0022_auto_20180620_1551'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('domain', models.URLField(blank=True)),
                ('term', models.CharField(blank=True, max_length=75)),
                ('page_name', models.CharField(default=None, max_length=75)),
                ('class_names', models.CharField(max_length=150)),
                ('id_names', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('author', models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('url', models.CharField(max_length=175)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('author', models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField(blank=True)),
                ('link', models.URLField(blank=True)),
                ('file', models.FileField(upload_to='development/climate-watch/media/Posts')),
                ('author', models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL)),
                ('page', models.ForeignKey(on_delete='cascade', to='api.Page')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('caption', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PageDetailExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='development/climate-watch/media/Posts')),
                ('description', models.TextField(blank=True)),
                ('file', models.FileField(upload_to='development/climate-watch/media/Posts')),
                ('extended_object', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.Page')),
                ('public_extension', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_extension', to='api.PageDetailExtension')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField(blank=True, default='Change Me')),
                ('active', models.BooleanField(default=False)),
                ('blog_post', models.ForeignKey(on_delete='cascade', to='djangocms_blog.Post')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='djangocms_blog_post_gallery', to=settings.FILER_IMAGE_MODEL, verbose_name='gallery images')),
            ],
        ),
        migrations.CreateModel(
            name='ExtendedPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('background_image', models.FileField(upload_to='development/climate-watch/media/Posts')),
                ('page', models.ForeignKey(editable=False, on_delete='cascade', related_name='extended_fields', to='api.Page', verbose_name='Page')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('author', models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL)),
                ('charity', models.ForeignKey(on_delete='cascade', to='djangocms_blog.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True)),
                ('object_id', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('author', models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(on_delete='cascade', to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='BeautifulGoogleSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=75)),
                ('link', models.URLField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('allowed', models.ForeignKey(on_delete='cascade', to='api.AllowedDomain')),
            ],
        ),
        migrations.CreateModel(
            name='BeautifulGoogleResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('subtitle', models.CharField(max_length=75)),
                ('abstract', models.TextField(blank=True)),
                ('image', models.CharField(max_length=75)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('bgs', models.ForeignKey(on_delete='cascade', to='api.BeautifulGoogleSearch')),
            ],
        ),
    ]