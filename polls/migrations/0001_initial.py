# Generated by Django 2.0.2 on 2018-02-17 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DecisionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scenario_title', models.CharField(max_length=400)),
                ('scenario_description', models.CharField(default=None, max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probability', models.CharField(choices=[('VL', 'Very low'), ('LW', 'Low'), ('MD', 'Medium'), ('HI', 'High'), ('VH', 'Very high')], default='MD', max_length=2)),
                ('age', models.CharField(choices=[('C', 'Child'), ('A', 'Adult'), ('O', 'Old')], default='A', max_length=1)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'NA')], default='N', max_length=1)),
                ('status', models.CharField(choices=[('C', 'Criminal'), ('A', 'Average Worker'), ('D', 'Doctor')], default='A', max_length=1)),
                ('decision', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.Decision')),
            ],
        ),
        migrations.AddField(
            model_name='decision',
            name='decision_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.DecisionGroup'),
        ),
    ]
