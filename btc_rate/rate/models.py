from django.db import models

class Rates(models.model):
    min_rate = models.FloatField()
    max_rate = models.FloatField()
    time_added = models.DateTimeField(auto_now_add = True)
