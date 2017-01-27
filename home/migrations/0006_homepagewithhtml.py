# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-01 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
        ('home', '0005_auto_20161128_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageWithHtml',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField((('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='doc-full', label='Rich Text')), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock(icon='site', label='HTML'))))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]