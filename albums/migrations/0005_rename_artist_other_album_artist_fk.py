# Generated by Django 4.0.5 on 2022-07-05 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_artist_album_artist_other'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='artist_other',
            new_name='artist_fk',
        ),
    ]