# Generated by Django 2.2.16 on 2021-06-17 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0150_rename_inv_sources_inv_updates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credential',
            old_name='managed_by_tower',
            new_name='managed',
        ),
        migrations.RenameField(
            model_name='credentialtype',
            old_name='managed_by_tower',
            new_name='managed',
        ),
        migrations.RenameField(
            model_name='executionenvironment',
            old_name='managed_by_tower',
            new_name='managed',
        ),
    ]