# Generated by Django 3.2.13 on 2022-06-21 21:29

from django.db import migrations


def forwards(apps, schema_editor):
    InventorySource = apps.get_model('main', 'InventorySource')
    InventorySource.objects.filter(update_on_project_update=True).update(update_on_launch=True)

    Project = apps.get_model('main', 'Project')
    Project.objects.filter(scm_inventory_sources__update_on_project_update=True).update(scm_update_on_launch=True)


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0163_convert_job_tags_to_textfield'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='inventorysource',
            name='scm_last_revision',
        ),
        migrations.RemoveField(
            model_name='inventorysource',
            name='update_on_project_update',
        ),
    ]
