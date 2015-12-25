from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime


class EmployeeDetail(models.Model):
        OFFICE_ROLE = (
            ('ADMIN', 'AD'),
            ('EMPLOYEE', 'EM'),
            ('GUEST', 'GU'),
        )
        user_id = models.ForeignKey('auth.User', related_name='UserInfo')
        dob = models.DateField(auto_now_add=False)
        address = models.CharField(max_length=100)
        contact = models.CharField(max_length=12)
        gender = models.CharField(max_length=1)
        role = models.CharField(max_length=9, choices=OFFICE_ROLE, default='GU')
        created = models.DateTimeField(default=datetime.now, blank=False)
        updated = models.DateTimeField(auto_now=True, blank=True)
        v_token = models.CharField(max_length=20)
        p_token = models.CharField(max_length=20)
        p_expire_at = models.IntegerField()


class TimeSchedual(models.Model):
        user_id = models.ForeignKey('auth.User', related_name='UserId')
        work_date = models.DateField(default=datetime.date)
        chunk_id = models.IntegerField()
        M_time_in = models.TimeField(blank=True)
        M_time_out = models.TimeField(blank=True)
        L_time_in = models.TimeField(blank=True)
        L_time_out = models.TimeField(blank=True)
        N_time_in = models.TimeField(blank=True)
        N_time_out = models.TimeField(blank=True)
        work_desc = models.CharField(max_length=100)
        created = models.DateTimeField(default=datetime.now, blank=False)
        updated = models.DateTimeField(auto_now=True, blank=True)

        class Meta:
            unique_together = (("user_id", "work_date"),)


class TimeSheets(models.Model):
        user_id = models.ForeignKey('auth.User', related_name='UserValue')
        work_date = models.DateField(default=datetime.date)
        chunk_id = models.IntegerField()
        in_time = models.TimeField(blank=True)
        out_time = models.TimeField(blank=True)
        created = models.DateTimeField(default=datetime.now, blank=False)
        updated = models.DateTimeField(auto_now=True, blank=True)

        class Meta:
            unique_together = (("user_id", "work_date", "chunk_id"),)