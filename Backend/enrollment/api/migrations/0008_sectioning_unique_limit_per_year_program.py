# Generated by Django 5.1.3 on 2024-12-23 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_grade_grade_alter_program_id_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='sectioning',
            constraint=models.UniqueConstraint(fields=('year_level', 'program'), name='unique_limit_per_year_program'),
        ),
    ]
