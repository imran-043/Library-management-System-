# Generated by Django 4.0.5 on 2022-09-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='std_no',
        ),
        migrations.AddField(
            model_name='student',
            name='std_id',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
