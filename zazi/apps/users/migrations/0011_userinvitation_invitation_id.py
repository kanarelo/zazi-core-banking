# Generated by Django 2.2.3 on 2019-12-22 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_userinvitation_invitation_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinvitation',
            name='invitation_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
