from django.db import models
from django.contrib.auth.models import User
from checkout.models import Order


class ContactQuery(models.Model):

    class Meta:
        verbose_name_plural = 'Contact queries'

    GENERAL = 'general'
    ORDER = 'order'
    QUERY_TYPE_CHOICES = [
        (GENERAL, 'General Query'),
        (ORDER, 'Order Query')
    ]

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    query_type = models.CharField(
        max_length=20, choices=QUERY_TYPE_CHOICES, default=GENERAL
    )

    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True
    )
    message = models.TextField()

    def __str__(self):
        if self.user:
            return f'Query from {self.user.username} - {self.query_type}'
        return f'Query from Guest {self.email} - {self.query_type}'
