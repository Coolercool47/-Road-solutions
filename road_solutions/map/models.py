from django.db import models


class Maps(models.Model):
    y2017 = models.BooleanField('2017', default=False)
    y2018 = models.BooleanField('2018', default=False)
    y2019 = models.BooleanField('2019', default=False)
    y2020 = models.BooleanField('2020', default=False)
