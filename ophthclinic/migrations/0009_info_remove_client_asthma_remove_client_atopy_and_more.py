# Generated by Django 4.1.3 on 2023-02-13 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ophthclinic', '0008_client_leftleftr_client_leftmiddler_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datesubmitted', models.DateTimeField(blank=True, null=True)),
                ('leftleft', models.FloatField(blank=True, null=True)),
                ('leftmiddle', models.FloatField(blank=True, null=True)),
                ('leftright', models.FloatField(blank=True, null=True)),
                ('rightleft', models.FloatField(blank=True, null=True)),
                ('rightmiddle', models.FloatField(blank=True, null=True)),
                ('rightright', models.FloatField(blank=True, null=True)),
                ('leftleftr', models.FloatField(blank=True, null=True)),
                ('leftmiddler', models.FloatField(blank=True, null=True)),
                ('leftrightr', models.FloatField(blank=True, null=True)),
                ('rightleftr', models.FloatField(blank=True, null=True)),
                ('rightmiddler', models.FloatField(blank=True, null=True)),
                ('rightrightr', models.FloatField(blank=True, null=True)),
                ('idpdist', models.FloatField(blank=True, null=True)),
                ('idpread', models.FloatField(blank=True, null=True)),
                ('diabetesmellitus', models.BooleanField(default=None)),
                ('deabetesnumber', models.FloatField(blank=True, default=None, null=True)),
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
                ('medication', models.CharField(blank=True, max_length=400, null=True)),
                ('bov', models.BooleanField(default=False)),
                ('diplopia', models.BooleanField(default=False)),
                ('headache', models.BooleanField(default=None)),
                ('burning', models.BooleanField(default=False)),
                ('foreign', models.BooleanField(default=False)),
                ('epiphoria', models.BooleanField(default=False)),
                ('glare', models.BooleanField(default=False)),
                ('note', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='asthma',
        ),
        migrations.RemoveField(
            model_name='client',
            name='atopy',
        ),
        migrations.RemoveField(
            model_name='client',
            name='bov',
        ),
        migrations.RemoveField(
            model_name='client',
            name='burning',
        ),
        migrations.RemoveField(
            model_name='client',
            name='cataract',
        ),
        migrations.RemoveField(
            model_name='client',
            name='cvs',
        ),
        migrations.RemoveField(
            model_name='client',
            name='datesubmitted',
        ),
        migrations.RemoveField(
            model_name='client',
            name='deabetesnumber',
        ),
        migrations.RemoveField(
            model_name='client',
            name='diabetesmellitus',
        ),
        migrations.RemoveField(
            model_name='client',
            name='diplopia',
        ),
        migrations.RemoveField(
            model_name='client',
            name='epiphoria',
        ),
        migrations.RemoveField(
            model_name='client',
            name='foreign',
        ),
        migrations.RemoveField(
            model_name='client',
            name='glare',
        ),
        migrations.RemoveField(
            model_name='client',
            name='glucoma',
        ),
        migrations.RemoveField(
            model_name='client',
            name='glucomasurgery',
        ),
        migrations.RemoveField(
            model_name='client',
            name='headache',
        ),
        migrations.RemoveField(
            model_name='client',
            name='hypertension',
        ),
        migrations.RemoveField(
            model_name='client',
            name='ihd',
        ),
        migrations.RemoveField(
            model_name='client',
            name='kidney',
        ),
        migrations.RemoveField(
            model_name='client',
            name='leftleft',
        ),
        migrations.RemoveField(
            model_name='client',
            name='leftleftr',
        ),
        migrations.RemoveField(
            model_name='client',
            name='leftmiddle',
        ),
        migrations.RemoveField(
            model_name='client',
            name='leftmiddler',
        ),
        migrations.RemoveField(
            model_name='client',
            name='leftright',
        ),
        migrations.RemoveField(
            model_name='client',
            name='leftrightr',
        ),
        migrations.RemoveField(
            model_name='client',
            name='liver',
        ),
        migrations.RemoveField(
            model_name='client',
            name='medication',
        ),
        migrations.RemoveField(
            model_name='client',
            name='note',
        ),
        migrations.RemoveField(
            model_name='client',
            name='refractive',
        ),
        migrations.RemoveField(
            model_name='client',
            name='rightleft',
        ),
        migrations.RemoveField(
            model_name='client',
            name='rightleftr',
        ),
        migrations.RemoveField(
            model_name='client',
            name='rightmiddle',
        ),
        migrations.RemoveField(
            model_name='client',
            name='rightmiddler',
        ),
        migrations.RemoveField(
            model_name='client',
            name='rightright',
        ),
        migrations.RemoveField(
            model_name='client',
            name='rightrightr',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='patientid',
        ),
        migrations.AddField(
            model_name='client',
            name='relatedprescriptions',
            field=models.ManyToManyField(blank=True, null=True, to='ophthclinic.prescription'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='datesubmitted',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='client',
            name='lastprofile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lastprofile', to='ophthclinic.info'),
        ),
        migrations.AddField(
            model_name='client',
            name='relatedprofiles',
            field=models.ManyToManyField(blank=True, null=True, related_name='relatedprofiles', to='ophthclinic.info'),
        ),
    ]