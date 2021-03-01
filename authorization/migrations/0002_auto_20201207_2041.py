# Generated by Django 3.1.4 on 2020-12-07 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nagroda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.CharField(choices=[('1', '1. stopień'), ('2', '2. stopień'), ('3', '3. stopień'), ('4', '4. stopień'), ('5', '5. stopień'), ('6', '6. stopień'), ('7', '7. stopień'), ('8', '8. stopień'), ('9', '9. stopień'), ('10', '10. stopień')], max_length=28)),
            ],
        ),
        migrations.DeleteModel(
            name='Award',
        ),
    ]
