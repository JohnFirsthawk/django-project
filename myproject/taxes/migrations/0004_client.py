# Generated by Django 3.1.7 on 2021-09-23 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxes', '0003_rename_userid_users_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_inserted', models.DateField()),
                ('tax', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxes.taxes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxes.users')),
            ],
        ),
    ]