# Generated by Django 5.0 on 2024-03-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccountmodel',
            name='Maximum_otp_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccountmodel',
            name='Maximum_otp_try',
            field=models.CharField(default=3, max_length=2),
        ),
        migrations.AddField(
            model_name='useraccountmodel',
            name='Otp',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccountmodel',
            name='Otp_expre_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
