from django.db import models


class ActiveManager(models.Manager):
    '''
    Excludes all products for which product_type is not published
    '''
    def active(self):
        return self.filter(
            active=True,
        )
