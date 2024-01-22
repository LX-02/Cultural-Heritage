# Generated by Django 4.2.9 on 2024-01-19 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Events",
            fields=[
                (
                    "events_id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="events_id"
                    ),
                ),
                ("theme", models.CharField(max_length=64, verbose_name="主题")),
            ],
        ),
        migrations.CreateModel(
            name="MasterPieces",
            fields=[
                (
                    "pieces_id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="pieces_id"
                    ),
                ),
                ("pieces_name", models.CharField(max_length=64, verbose_name="项目名称")),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "user_id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="工号"
                    ),
                ),
                ("username", models.CharField(max_length=64, verbose_name="用户名")),
                ("password", models.CharField(max_length=64, verbose_name="密码")),
            ],
        ),
        migrations.CreateModel(
            name="Craftsman",
            fields=[
                (
                    "craftsman_id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="craftsman_id"
                    ),
                ),
                ("craftsman_name", models.CharField(max_length=64, verbose_name="姓名")),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="culapp.masterpieces",
                        verbose_name="传承项目",
                    ),
                ),
            ],
        ),
    ]