# Generated by Django 2.1.3 on 2019-01-02 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("contracts", "0003_auto_20181203_1542")]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="effective_date_from",
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name="contract",
            name="effective_date_to",
            field=models.DateTimeField(db_index=True),
        ),
    ]
