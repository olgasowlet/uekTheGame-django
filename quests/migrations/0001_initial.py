# Generated by Django 3.1.4 on 2021-03-07 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('unique_number', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('N', 'Naukowa'), ('E', 'Edukacyjna'), ('O', 'Organizacyjna'), ('F', 'Fun Part')], max_length=1)),
                ('type', models.CharField(choices=[('NK', 'Konferencje'), ('NA', 'Artykuły'), ('ND', 'Debaty'), ('NB', 'Badania'), ('NS', 'Specjalista'), ('EA', 'Średnia'), ('ES', 'Semestry'), ('EO', 'Obowiązki Pierwszaka'), ('ET', 'Szkolenia'), ('EP', 'Praktyki'), ('EC', 'Certyfikaty'), ('EB', 'Bierny udział'), ('EW', 'Wyjazdy edukacyjne'), ('EE', 'Specjaliści'), ('E', 'Specjalne'), ('OO', 'Organizacje Studenckie'), ('OW', 'Wydarzenia'), ('OP', 'Praca podczas studiów'), ('OS', 'Specjaliści'), ('OE', 'Specjalne'), ('FW', 'Wyjazdy'), ('FI', 'Imprezy integracyjne'), ('FA', 'Absurdy'), ('FJ', 'Juvenalia'), ('FS', 'Specjaliści')], max_length=2)),
                ('name', models.CharField(max_length=256)),
                ('credits', models.CharField(max_length=5)),
                ('terms', models.CharField(max_length=256)),
                ('approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
