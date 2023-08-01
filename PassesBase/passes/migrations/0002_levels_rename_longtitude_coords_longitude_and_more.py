# Generated by Django 4.2 on 2023-04-17 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.TextField(blank=True, max_length=2)),
                ('summer', models.TextField(blank=True, max_length=2)),
                ('autumn', models.TextField(blank=True, max_length=2)),
                ('spring', models.TextField(blank=True, max_length=2)),
            ],
        ),
        migrations.RenameField(
            model_name='coords',
            old_name='longtitude',
            new_name='longitude',
        ),
        migrations.RenameField(
            model_name='perevaladded',
            old_name='beautyTitle',
            new_name='beauty_title',
        ),
        migrations.RemoveField(
            model_name='perevaladded',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='perevaladded',
            name='level_autumn',
        ),
        migrations.RemoveField(
            model_name='perevaladded',
            name='level_spring',
        ),
        migrations.RemoveField(
            model_name='perevaladded',
            name='level_summer',
        ),
        migrations.RemoveField(
            model_name='perevaladded',
            name='level_winter',
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='add_time',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='data',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='level',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='passes.levels'),
            preserve_default=False,
        ),
    ]
