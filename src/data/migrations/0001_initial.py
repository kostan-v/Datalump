# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdjudgementNature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'adjudgement_natures',
            },
        ),
        migrations.CreateModel(
            name='AdjudgementRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtr_year', models.IntegerField()),
                ('year', models.IntegerField()),
                ('records_count', models.IntegerField()),
                ('url', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'adjudgement_records',
            },
        ),
        migrations.CreateModel(
            name='AdjudgementRecordAdjudgementNature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('records_count', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('adjudgement_nature', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.AdjudgementNature')),
                ('adjudgement_record', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.AdjudgementRecord')),
            ],
            options={
                'db_table': 'adjudgement_record_adjudgement_nature_entries',
            },
        ),
        migrations.CreateModel(
            name='AdjudgementRecordLegislationSubarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('records_count', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('adjudgement_record', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.AdjudgementRecord')),
            ],
            options={
                'db_table': 'adjudgement_record_legislation_subarea_entries',
            },
        ),
        migrations.CreateModel(
            name='CustomerRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtr_year', models.IntegerField()),
                ('year', models.IntegerField()),
                ('sum_money', models.DecimalField(decimal_places=2, max_digits=13)),
                ('sum_contracts', models.IntegerField()),
                ('url', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'customer_records',
            },
        ),
        migrations.CreateModel(
            name='EndUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=128)),
                ('identification', models.CharField(max_length=48)),
                ('public_official', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'end_users',
            },
        ),
        migrations.CreateModel(
            name='Esu2010Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'esu2010_codes',
            },
        ),
        migrations.CreateModel(
            name='LegalForms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('effective_from', models.DateField()),
                ('effective_to', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'organization_legal_forms',
            },
        ),
        migrations.CreateModel(
            name='LegislationSubarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'legislation_subareas',
            },
        ),
        migrations.CreateModel(
            name='MainActivityCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'main_activity_codes',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('established_on', models.DateField()),
                ('terminated_on', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('esu2010_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Esu2010Code')),
                ('main_activity_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.MainActivityCode')),
            ],
            options={
                'db_table': 'organizations',
            },
        ),
        migrations.CreateModel(
            name='OrganizationAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formatted_address', models.CharField(max_length=256)),
                ('street', models.CharField(max_length=128)),
                ('reg_number', models.IntegerField()),
                ('building_number', models.CharField(max_length=128)),
                ('postal_code', models.CharField(max_length=16)),
                ('municipality', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=64)),
                ('effective_from', models.DateField()),
                ('effective_to', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization')),
            ],
            options={
                'db_table': 'organization_address_entries',
            },
        ),
        migrations.CreateModel(
            name='OrganizationDepositEntries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256, null=True)),
                ('person_given_name', models.CharField(max_length=51, null=True)),
                ('person_family_name', models.CharField(max_length=51, null=True)),
                ('person_given_family_name', models.CharField(max_length=26, null=True)),
                ('person_prefixes', models.CharField(max_length=17, null=True)),
                ('person_postfixes', models.CharField(max_length=10, null=True)),
                ('deposit_amount', models.DecimalField(decimal_places=2, max_digits=13)),
                ('deposit_currency', models.CharField(max_length=9)),
                ('deposit_type', models.CharField(max_length=256)),
                ('effective_from', models.DateField()),
                ('effective_to', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization')),
            ],
            options={
                'db_table': 'organization_deposit_entries',
            },
        ),
        migrations.CreateModel(
            name='OrganizationEconomicActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128)),
                ('effective_from', models.DateField()),
                ('effective_to', models.DateField(null=True)),
                ('suspended_from', models.DateField(null=True)),
                ('suspended_to', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization')),
            ],
            options={
                'db_table': 'organization_economic_activity',
            },
        ),
        migrations.CreateModel(
            name='OrganizationEndUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_since', models.DateField()),
                ('last_change', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('end_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.EndUser')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization')),
            ],
            options={
                'db_table': 'organization_end_user_entries',
            },
        ),
        migrations.CreateModel(
            name='OrganizationIdentifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipo', models.IntegerField()),
                ('effective_from', models.DateField()),
                ('effective_to', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization')),
            ],
            options={
                'db_table': 'organization_identifier_entries',
            },
        ),
        migrations.CreateModel(
            name='OrganizationLegalForms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_from', models.DateField()),
                ('effective_to', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('legal_form_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='data.LegalForms')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization')),
            ],
            options={
                'db_table': 'organization_legal_forms_entries',
            },
        ),
        migrations.CreateModel(
            name='OrganizationLegalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=128)),
                ('effective_from', models.DateField()),
                ('effective_to', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization')),
            ],
            options={
                'db_table': 'organization_legal_status_entries',
            },
        ),
        migrations.CreateModel(
            name='OrganizationName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('effective_from', models.DateField()),
                ('effective_to', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization')),
            ],
            options={
                'db_table': 'organization_name_entries',
            },
        ),
        migrations.CreateModel(
            name='OrganizationOtherLegalFact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('effective_from', models.DateField()),
                ('effective_to', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization')),
            ],
            options={
                'db_table': 'organization_other_legal_fact_entries',
            },
        ),
        migrations.CreateModel(
            name='OrganizationShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_price', models.DecimalField(decimal_places=2, max_digits=13)),
                ('share_currency', models.CharField(max_length=8)),
                ('share_amount', models.BigIntegerField()),
                ('share_transfer', models.TextField(null=True)),
                ('effective_from', models.DateField()),
                ('effective_to', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization')),
            ],
            options={
                'db_table': 'organization_share_entries',
            },
        ),
        migrations.CreateModel(
            name='OrganizationStakeholderEntries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256, null=True)),
                ('person_given_name', models.CharField(max_length=51, null=True)),
                ('person_family_name', models.CharField(max_length=51, null=True)),
                ('person_given_family_name', models.CharField(max_length=26, null=True)),
                ('person_prefixes', models.CharField(max_length=17, null=True)),
                ('person_postfixes', models.CharField(max_length=10, null=True)),
                ('address_formatted', models.CharField(max_length=176, null=True)),
                ('address_street', models.CharField(max_length=128, null=True)),
                ('address_reg_number', models.IntegerField()),
                ('address_building_number', models.CharField(max_length=21, null=True)),
                ('address_postal_code', models.CharField(max_length=11, null=True)),
                ('address_municipality', models.CharField(max_length=128, null=True)),
                ('address_country', models.CharField(max_length=128, null=True)),
                ('address_effective_from', models.DateField(null=True)),
                ('address_effective_to', models.DateField(null=True)),
                ('effective_from', models.DateField()),
                ('effective_to', models.DateField(null=True)),
                ('ico', models.IntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization')),
            ],
            options={
                'db_table': 'organization_stakeholder_entries',
            },
        ),
        migrations.CreateModel(
            name='OrganizationStatutoryEntries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128, null=True)),
                ('person_given_name', models.CharField(max_length=128, null=True)),
                ('person_family_name', models.CharField(max_length=128, null=True)),
                ('person_given_family_name', models.CharField(max_length=128, null=True)),
                ('person_prefixes', models.CharField(max_length=128, null=True)),
                ('person_postfixes', models.CharField(max_length=128, null=True)),
                ('address_formatted', models.CharField(max_length=128, null=True)),
                ('address_street', models.CharField(max_length=128, null=True)),
                ('address_reg_number', models.IntegerField(null=True)),
                ('address_building_number', models.CharField(max_length=128, null=True)),
                ('address_postal_code', models.CharField(max_length=128, null=True)),
                ('address_municipality', models.CharField(max_length=128, null=True)),
                ('address_country', models.CharField(max_length=128, null=True)),
                ('effective_from', models.DateField()),
                ('effective_to', models.DateField(null=True)),
                ('ico', models.IntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization')),
            ],
            options={
                'db_table': 'organization_statutory_entries',
            },
        ),
        migrations.CreateModel(
            name='ShareForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'share_forms',
            },
        ),
        migrations.CreateModel(
            name='ShareType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'share_types',
            },
        ),
        migrations.CreateModel(
            name='StakeholderTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'stakeholder_types',
            },
        ),
        migrations.CreateModel(
            name='SupplierRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtr_year', models.IntegerField()),
                ('year', models.IntegerField()),
                ('sum_money', models.DecimalField(decimal_places=2, max_digits=13)),
                ('sum_contracts', models.IntegerField()),
                ('url', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization')),
            ],
            options={
                'db_table': 'supplier_records',
            },
        ),
        migrations.AddField(
            model_name='organizationstatutoryentries',
            name='stakeholder_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='data.StakeholderTypes'),
        ),
        migrations.AddField(
            model_name='organizationstakeholderentries',
            name='stakeholder_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.StakeholderTypes'),
        ),
        migrations.AddField(
            model_name='organizationshare',
            name='share_form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='data.ShareForm'),
        ),
        migrations.AddField(
            model_name='organizationshare',
            name='share_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.ShareType'),
        ),
        migrations.AddField(
            model_name='legalforms',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization'),
        ),
        migrations.AddField(
            model_name='customerrecord',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization'),
        ),
        migrations.AddField(
            model_name='adjudgementrecordlegislationsubarea',
            name='legislation_subarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.LegislationSubarea'),
        ),
        migrations.AddField(
            model_name='adjudgementrecord',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Organization'),
        ),
    ]
