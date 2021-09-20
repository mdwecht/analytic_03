from django.db import models


class Job(models.Model):
    '''
    DSAE Fields Common to all Jobs:
    '''
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    period = models.IntegerField(default=3600)
    last_ts = models.DateTimeField(auto_now_add=True)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    '''
    DSAE Fields Specific to 'analytic_03' Job Type:
    '''
    src_host = models.CharField(max_length=20, default='Source Host')
    src_port = models.CharField(max_length=20, default='0')
    dest_host = models.CharField(max_length=20, default='Destination Host')
    dest_port = models.CharField(max_length=20, default='0')
    search =  models.CharField(max_length=20)
    sid = models.CharField(max_length=20)
    session = models.CharField(max_length=20)

    def __str__(self):
        return self.name
