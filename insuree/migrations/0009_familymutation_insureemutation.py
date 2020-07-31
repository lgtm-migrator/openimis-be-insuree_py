# Generated by Django 3.0.3 on 2020-07-31 05:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_mutationlog_client_mutation_details'),
        ('insuree', '0008_auto_20200731_0443'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsureeMutation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('insuree', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mutations', to='insuree.Insuree')),
                ('mutation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='insurees', to='core.MutationLog')),
            ],
            options={
                'db_table': 'insuree_InsureeMutation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FamilyMutation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mutations', to='insuree.Family')),
                ('mutation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='families', to='core.MutationLog')),
            ],
            options={
                'db_table': 'insuree_FamilyMutation',
                'managed': True,
            },
        ),
    ]
