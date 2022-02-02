# Generated by Django 4.0 on 2021-12-25 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('posts', '0003_alter_post_name_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_model', to='auth.user'),
        ),
    ]
