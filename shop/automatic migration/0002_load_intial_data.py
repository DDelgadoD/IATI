import django.conf
from django.db import migrations
from django.core.management import call_command
from django.conf import settings

fixture = settings.BASE_DIR / 'shop/fixtures/initial_data.json'


def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture, app_label='shop')


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
