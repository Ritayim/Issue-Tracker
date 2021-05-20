# Generated by Django 3.1.7 on 2021-05-19 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20)),
                ('project', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='base.project')),
            ],
        ),
    ]