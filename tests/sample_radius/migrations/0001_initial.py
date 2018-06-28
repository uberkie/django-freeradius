from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_column='nasname', db_index=True, help_text='NAS Name (or IP address)', max_length=128, verbose_name='name')),
                ('short_name', models.CharField(db_column='shortname', max_length=32, verbose_name='short name')),
                ('type', models.CharField(default='other', max_length=30, verbose_name='type')),
                ('ports', models.PositiveIntegerField(blank=True, null=True, verbose_name='ports')),
                ('secret', models.CharField(help_text='Shared Secret', max_length=60, verbose_name='secret')),
                ('server', models.CharField(blank=True, max_length=64, null=True, verbose_name='server')),
                ('community', models.CharField(blank=True, max_length=50, null=True, verbose_name='community')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='description')),
                ('details', models.CharField(blank=True, max_length=64, null=True, verbose_name='details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RadiusAccounting',
            fields=[
                ('id', models.BigAutoField(db_column='radacctid', primary_key=True, serialize=False)),
                ('session_id', models.CharField(db_column='acctsessionid', db_index=True, max_length=64, verbose_name='session ID')),
                ('unique_id', models.CharField(db_column='acctuniqueid', max_length=32, unique=True, verbose_name='accounting unique ID')),
                ('username', models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='username')),
                ('groupname', models.CharField(blank=True, max_length=64, null=True, verbose_name='group name')),
                ('realm', models.CharField(blank=True, max_length=64, null=True, verbose_name='realm')),
                ('nas_ip_address', models.GenericIPAddressField(db_column='nasipaddress', db_index=True, verbose_name='NAS IP address')),
                ('nas_port_id', models.CharField(blank=True, db_column='nasportid', max_length=15, null=True, verbose_name='NAS port ID')),
                ('nas_port_type', models.CharField(blank=True, db_column='nasporttype', max_length=32, null=True, verbose_name='NAS port type')),
                ('start_time', models.DateTimeField(blank=True, db_column='acctstarttime', db_index=True, null=True, verbose_name='start time')),
                ('update_time', models.DateTimeField(blank=True, db_column='acctupdatetime', null=True, verbose_name='update time')),
                ('stop_time', models.DateTimeField(blank=True, db_column='acctstoptime', db_index=True, null=True, verbose_name='stop time')),
                ('interval', models.IntegerField(blank=True, db_column='acctinterval', null=True, verbose_name='interval')),
                ('session_time', models.PositiveIntegerField(blank=True, db_column='acctsessiontime', null=True, verbose_name='session time')),
                ('authentication', models.CharField(blank=True, db_column='acctauthentic', max_length=32, null=True, verbose_name='authentication')),
                ('connection_info_start', models.CharField(blank=True, db_column='connectinfo_start', max_length=50, null=True, verbose_name='connection info start')),
                ('connection_info_stop', models.CharField(blank=True, db_column='connectinfo_stop', max_length=50, null=True, verbose_name='connection info stop')),
                ('input_octets', models.BigIntegerField(blank=True, db_column='acctinputoctets', null=True, verbose_name='input octets')),
                ('output_octets', models.BigIntegerField(blank=True, db_column='acctoutputoctets', null=True, verbose_name='output octets')),
                ('called_station_id', models.CharField(blank=True, db_column='calledstationid', max_length=50, null=True, verbose_name='called station ID')),
                ('calling_station_id', models.CharField(blank=True, db_column='callingstationid', max_length=50, null=True, verbose_name='calling station ID')),
                ('terminate_cause', models.CharField(blank=True, db_column='acctterminatecause', max_length=32, null=True, verbose_name='termination cause')),
                ('service_type', models.CharField(blank=True, db_column='servicetype', max_length=32, null=True, verbose_name='service type')),
                ('framed_protocol', models.CharField(blank=True, db_column='framedprotocol', max_length=32, null=True, verbose_name='framed protocol')),
                ('framed_ip_address', models.GenericIPAddressField(blank=True, db_column='framedipaddress', db_index=True, null=True, verbose_name='framed IP address')),
                ('details', models.CharField(blank=True, max_length=64, null=True, verbose_name='details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RadiusBatch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_index=True, help_text='A unique batch name', max_length=128, verbose_name='name')),
                ('strategy', models.CharField(choices=[('prefix', 'Generate from prefix'), ('csv', 'Import from CSV')], db_index=True, help_text='Import users from a CSV or generate using a prefix', max_length=16, verbose_name='strategy')),
                ('csvfile', models.FileField(blank=True, help_text='The csv file containing the user details to be uploaded', null=True, upload_to='', verbose_name='CSV')),
                ('prefix', models.CharField(blank=True, help_text='Usernames generated will be of the format [prefix][number]', max_length=20, null=True, verbose_name='prefix')),
                ('pdf', models.FileField(blank=True, help_text='The pdf file containing list of usernames and passwords', null=True, upload_to='', verbose_name='PDF')),
                ('expiration_date', models.DateField(blank=True, help_text='If left blank users will never expire', null=True, verbose_name='expiration date')),
                ('users', models.ManyToManyField(blank=True, help_text='List of users uploaded in this batch', related_name='radius_batch', to=settings.AUTH_USER_MODEL)),
                ('details', models.CharField(blank=True, max_length=64, null=True, verbose_name='details')),
            ],
            options={},
        ),
        migrations.CreateModel(
            name='RadiusCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('username', models.CharField(db_index=True, max_length=64, verbose_name='username')),
                ('value', models.CharField(max_length=253, verbose_name='value')),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('==', '=='), ('+=', '+='), ('!=', '!='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<='), ('=~', '=~'), ('!~', '!~'), ('=*', '=*'), ('!*', '!*')], default=':=', max_length=2, verbose_name='operator')),
                ('attribute', models.CharField(blank=True, choices=[('Cleartext-Password', 'Cleartext-Password'), ('NT-Password', 'NT-Password'), ('LM-Password', 'LM-Password'), ('MD5-Password', 'MD5-Password'), ('SMD5-Password', 'SMD5-Password'), ('SSHA-Password', 'SSHA-Password'), ('Crypt-Password', 'Crypt-Password')], default='NT-Password', max_length=64, verbose_name='attribute')),
                ('is_active', models.BooleanField(default=True)),
                ('valid_until', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('details', models.CharField(blank=True, max_length=64, null=True, verbose_name='details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RadiusGroup',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('groupname', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='group name')),
                ('priority', models.IntegerField(default=1, verbose_name='priority')),
                ('notes', models.CharField(blank=True, max_length=64, null=True, verbose_name='notes')),
                ('details', models.CharField(blank=True, max_length=64, null=True, verbose_name='details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RadiusGroupCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('groupname', models.CharField(db_index=True, max_length=64, verbose_name='group name')),
                ('attribute', models.CharField(max_length=64, verbose_name='attribute')),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('==', '=='), ('+=', '+='), ('!=', '!='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<='), ('=~', '=~'), ('!~', '!~'), ('=*', '=*'), ('!*', '!*')], default=':=', max_length=2, verbose_name='operator')),
                ('value', models.CharField(max_length=253, verbose_name='value')),
                ('details', models.CharField(blank=True, max_length=64, null=True, verbose_name='details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RadiusGroupReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('groupname', models.CharField(db_index=True, max_length=64, verbose_name='group name')),
                ('attribute', models.CharField(max_length=64, verbose_name='attribute')),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('+=', '+=')], default='=', max_length=2, verbose_name='operator')),
                ('value', models.CharField(max_length=253, verbose_name='value')),
                ('details', models.CharField(blank=True, max_length=64, null=True, verbose_name='details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RadiusGroupUsers',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='username')),
                ('groupname', models.CharField(max_length=255, unique=True, verbose_name='group name')),
                ('details', models.CharField(blank=True, max_length=64, null=True, verbose_name='details')),
                ('radius_check', models.ManyToManyField(blank=True, db_column='radiuscheck', to=settings.DJANGO_FREERADIUS_RADIUSCHECK_MODEL, verbose_name='radius check')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RadiusPostAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='username')),
                ('password', models.CharField(blank=True, db_column='pass', max_length=64, verbose_name='password')),
                ('reply', models.CharField(max_length=32, verbose_name='reply')),
                ('called_station_id', models.CharField(blank=True, db_column='calledstationid', max_length=50, null=True, verbose_name='called station ID')),
                ('calling_station_id', models.CharField(blank=True, db_column='callingstationid', max_length=50, null=True, verbose_name='calling station ID')),
                ('date', models.DateTimeField(auto_now_add=True, db_column='authdate', verbose_name='date')),
                ('details', models.CharField(blank=True, max_length=64, null=True, verbose_name='details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RadiusReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('username', models.CharField(db_index=True, max_length=64, verbose_name='username')),
                ('value', models.CharField(max_length=253, verbose_name='value')),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('+=', '+=')], default='=', max_length=2, verbose_name='operator')),
                ('attribute', models.CharField(max_length=64, verbose_name='attribute')),
                ('details', models.CharField(blank=True, max_length=64, null=True, verbose_name='details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RadiusUserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('username', models.CharField(db_index=True, max_length=64, verbose_name='username')),
                ('groupname', models.CharField(max_length=64, verbose_name='group name')),
                ('priority', models.IntegerField(default=1, verbose_name='priority')),
                ('details', models.CharField(blank=True, max_length=64, null=True, verbose_name='details')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='radiusgroupusers',
            name='radius_reply',
            field=models.ManyToManyField(blank=True, db_column='radiusreply', to=settings.DJANGO_FREERADIUS_RADIUSREPLY_MODEL, verbose_name='radius reply'),
        ),
        migrations.CreateModel(
            name='RadiusProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_index=True, help_text='A unique profile name', max_length=128, verbose_name='name')),
                ('daily_session_limit', models.BigIntegerField(blank=True, null=True, verbose_name='daily session limit')),
                ('daily_bandwidth_limit', models.BigIntegerField(blank=True, null=True, verbose_name='daily bandwidth limit')),
                ('max_all_time_limit', models.BigIntegerField(blank=True, null=True, verbose_name='maximum all time session limit')),
                ('default', models.BooleanField(default=False, verbose_name='Use this profile as the default profile')),
                ('details', models.CharField(blank=True, max_length=64, null=True, verbose_name='details')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
