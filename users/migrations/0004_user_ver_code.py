# Generated by Django 4.2.6 on 2023-11-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_email_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='617267206452', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
