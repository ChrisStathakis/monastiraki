# Generated by Django 2.0.5 on 2019-02-17 08:51

from django.db import migrations, models
import frontend.validators


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20190215_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorysite',
            name='title',
        ),
        migrations.AlterField(
            model_name='categorysite',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Κατάσταση'),
        ),
        migrations.AlterField(
            model_name='categorysite',
            name='image',
            field=models.ImageField(blank=True, help_text='600*600', null=True, upload_to=frontend.validators.category_site_directory_path),
        ),
        migrations.AlterField(
            model_name='categorysite',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Τίτλος'),
        ),
        migrations.AlterField(
            model_name='categorysite',
            name='show_on_menu',
            field=models.BooleanField(default=False, verbose_name='Εμφάνιση στην Navbar'),
        ),
    ]
