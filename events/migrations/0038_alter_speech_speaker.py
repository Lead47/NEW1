# Generated by Django 4.2.7 on 2024-03-08 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0004_rename_spekaer_type_speaker_speaker_type'),
        ('events', '0037_alter_speech_speaker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speech',
            name='speaker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='speakers.speaker'),
        ),
    ]
