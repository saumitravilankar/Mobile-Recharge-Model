# Generated by Django 4.1.4 on 2022-12-19 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recharge", "0006_rename_validity_plan_validity_in_days_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recharge",
            name="plan",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="recharge.plan",
            ),
            preserve_default=False,
        ),
    ]
