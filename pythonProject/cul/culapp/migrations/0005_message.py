# Generated by Django 4.2.9 on 2024-01-26 05:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("culapp", "0004_rename_craftsman_name_craftsman_craftsman_name_ch_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, default="", max_length=20, verbose_name="姓名"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, default="", max_length=254, verbose_name="邮箱"
                    ),
                ),
                ("text", models.TextField(blank=True, default="", verbose_name="留言内容")),
                (
                    "create_time",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2024, 1, 26, 5, 46, 53, 88144, tzinfo=datetime.timezone.utc
                        ),
                        verbose_name="创建时间",
                    ),
                ),
            ],
            options={
                "verbose_name": "留言板内容",
                "db_table": "meassage",
                "ordering": ["-create_time"],
            },
        ),
    ]
