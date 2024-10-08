# Generated by Django 5.1 on 2024-08-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0015_resourcecategory_resourceitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='resourceitem',
            name='category',
        ),
        migrations.DeleteModel(
            name='ResourceCategory',
        ),
        migrations.DeleteModel(
            name='ResourceItem',
        ),
    ]
