# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-21 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20170815_2235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailtemplate',
            options={'ordering': ('name',), 'permissions': (('send_email', 'Can send emails using the SendEmailView'),), 'verbose_name': 'Email template', 'verbose_name_plural': 'Email templates'},
        ),
        migrations.AlterModelOptions(
            name='eventoccurrence',
            options={'ordering': ('event', 'startTime'), 'verbose_name': 'Event occurrence', 'verbose_name_plural': 'Event occurrences'},
        ),
        migrations.AlterModelOptions(
            name='eventstaffcategory',
            options={'ordering': ('name',), 'verbose_name': 'Event staff category', 'verbose_name_plural': 'Event staff categories'},
        ),
        migrations.AlterModelOptions(
            name='eventstaffmember',
            options={'ordering': ('event', 'staffMember__lastName', 'staffMember__firstName'), 'verbose_name': 'Event staff member', 'verbose_name_plural': 'Event staff members'},
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ('-modifiedDate',), 'permissions': (('view_all_invoices', 'Can view invoices without passing the validation string.'), ('send_invoices', 'Can send invoices to students requesting payment'), ('process_refunds', 'Can refund customers for registrations and other invoice payments.')), 'verbose_name': 'Invoice', 'verbose_name_plural': 'Invoices'},
        ),
        migrations.AlterModelOptions(
            name='paymentrecord',
            options={'ordering': ('-modifiedDate',), 'verbose_name': 'Payment record', 'verbose_name_plural': 'Payment records'},
        ),
        migrations.AlterModelOptions(
            name='pricingtier',
            options={'ordering': ('name',), 'verbose_name': 'Pricing tier', 'verbose_name_plural': 'Pricing tiers'},
        ),
        migrations.AlterModelOptions(
            name='staffmember',
            options={'ordering': ('lastName', 'firstName'), 'permissions': (('view_staff_directory', 'Can access the staff directory view'), ('view_school_stats', "Can view statistics about the school's performance.")), 'verbose_name': 'Staff member', 'verbose_name_plural': 'Staff members'},
        ),
    ]
