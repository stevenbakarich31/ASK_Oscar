# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 14:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('sb_mail', '0013_mail_message_attachment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email_subscription',
            options={'verbose_name': 'Subscription', 'verbose_name_plural': 'Subscriptions'},
        ),
        migrations.AlterModelOptions(
            name='mail_message',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterModelOptions(
            name='mail_message_attachment',
            options={'verbose_name': 'Message Attachment', 'verbose_name_plural': 'Message Attachments'},
        ),
        migrations.AlterModelOptions(
            name='mail_server',
            options={'verbose_name': 'Out Server'},
        ),
        migrations.AlterModelOptions(
            name='sb_mail_server',
            options={'verbose_name': 'In Server', 'verbose_name_plural': 'In Servers'},
        ),
        migrations.AlterModelOptions(
            name='sbmail_template',
            options={'verbose_name': 'Template', 'verbose_name_plural': 'Templates'},
        ),
        migrations.RemoveField(
            model_name='mail_message',
            name='name',
        ),
    ]