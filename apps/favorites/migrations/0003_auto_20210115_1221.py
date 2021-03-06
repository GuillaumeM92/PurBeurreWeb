# Generated by Django 3.0.7 on 2021-01-15 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("favorites", "0002_favorite_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="favorite",
            name="user",
        ),
        migrations.AddField(
            model_name="favorite",
            name="email",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
