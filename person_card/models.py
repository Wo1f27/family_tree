from django.db import models
from django.shortcuts import reverse


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    profile_avatar = models.ImageField(upload_to='profile/', blank=True, null=True)
    deleted = models.BooleanField(default=False, blank=False)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'person'
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        return f'{self.first_name} {self.patronymic} {self.last_name}'

    # def get_absolute_url(self):
    #     return reverse()


class Email(models.Model):
    person = models.ForeignKey('Person', related_name='emails', on_delete=models.CASCADE)
    email = models.EmailField(max_length=256, blank=False)
    is_primary = models.BooleanField(default=False, blank=False)

    class Meta:
        db_table = 'emails'
        unique_together = ['person', 'email']

    def __str__(self):
        return f'{self.email}'


class PhoneNumber(models.Model):
    person = models.ForeignKey('Person', related_name='phones', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=False)
    is_primary = models.BooleanField(default=False, blank=False)

    class Meta:
        db_table = 'phone_numbers'
        unique_together = ['person', 'phone_number']

    def __str__(self):
        return f'{self.phone_number}'

