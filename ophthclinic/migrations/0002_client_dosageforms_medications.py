# Generated by Django 4.1.3 on 2023-02-06 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ophthclinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('yearofbirth', models.IntegerField()),
                ('datesubmitted', models.DateTimeField()),
                ('leftleft', models.IntegerField()),
                ('leftmiddle', models.IntegerField()),
                ('leftright', models.IntegerField()),
                ('rightleft', models.IntegerField()),
                ('rightmiddle', models.IntegerField()),
                ('rightright', models.IntegerField()),
                ('diabetesmellitus', models.BooleanField(default=False)),
                ('deabetesnumber', models.IntegerField()),
                ('hypertension', models.BooleanField(default=False)),
                ('ihd', models.BooleanField(default=False)),
                ('cvs', models.BooleanField(default=False)),
                ('asthma', models.BooleanField(default=False)),
                ('atopy', models.BooleanField(default=False)),
                ('liver', models.BooleanField(default=False)),
                ('kidney', models.BooleanField(default=False)),
                ('cataract', models.BooleanField(default=False)),
                ('glucoma', models.BooleanField(default=False)),
                ('glucomasurgery', models.BooleanField(default=False)),
                ('refractive', models.BooleanField(default=False)),
                ('medication', models.CharField(max_length=400)),
                ('bov', models.BooleanField(default=False)),
                ('diplopia', models.BooleanField(default=False)),
                ('headache', models.BooleanField(default=None)),
                ('burning', models.BooleanField(default=False)),
                ('foreign', models.BooleanField(default=False)),
                ('epiphoria', models.BooleanField(default=False)),
                ('glare', models.BooleanField(default=False)),
                ('note', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='dosageforms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='medications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('concentration', models.IntegerField()),
                ('dosage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ophthclinic.dosageforms')),
            ],
        ),
    ]
