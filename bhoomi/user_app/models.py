from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    PROVINCE_CHOICES = [
        ('Province 1', 'Province 1'),
        ('Province 2', 'Province 2'),
        ('Province 3', 'Province 3'),
        ('Province 4', 'Province 4'),
        ('Province 5', 'Province 5'),
        ('Province 6', 'Province 6'),
        ('Province 7', 'Province 7'),
        ('Province 8', 'Province 8'),
        ('Province 9', 'Province 9'),
    ]

    DISTRICT_CHOICES = [
        ('District 1', 'District 1'),
        ('District 2', 'District 2'),
        ('District 3', 'District 3'),
        ('District 4', 'District 4'),
        ('District 5', 'District 5'),
        ('District 6', 'District 6'),
        ('District 7', 'District 7'),
        ('District 8', 'District 8'),
        ('District 9', 'District 9'),
        ('District 10', 'District 10'),
        ('District 11', 'District 11'),
        ('District 12', 'District 12'),
        ('District 13', 'District 13'),
        ('District 14', 'District 14'),
        ('District 15', 'District 15'),
        ('District 16', 'District 16'),
        ('District 17', 'District 17'),
        ('District 18', 'District 18'),
        ('District 19', 'District 19'),
        ('District 20', 'District 20'),
        ('District 21', 'District 21'),
        ('District 22', 'District 22'),
        ('District 23', 'District 23'),
        ('District 24', 'District 24'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15, blank=True)
    district = models.CharField(max_length=50, choices=DISTRICT_CHOICES, blank=True)
    province = models.CharField(max_length=50, choices=PROVINCE_CHOICES, blank=True)
    unique_user_id = models.CharField(max_length=20, unique=True, blank=True, null=True)

    points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if not self.unique_user_id:
            import uuid
            self.unique_user_id = str(uuid.uuid4()).replace('-', '')[:20]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s profile"
