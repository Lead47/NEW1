# Generated by Django 4.1.6 on 2023-12-03 20:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0005_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verification_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
