# Generated by Django 3.1.1 on 2020-11-02 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parlante',
            fields=[
                ('id_parlante', models.AutoField(db_column='id_alumno', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('tipo', models.CharField(blank=True, max_length=10, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos')),
            ],
            options={
                'ordering': ['tipo'],
            },
        ),
    ]