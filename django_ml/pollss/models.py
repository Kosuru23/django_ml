from django.db import models

class PredictionInput(models.Model):
    income = models.FloatField()
    children = models.IntegerField()
    home_owner = models.BooleanField(default=False)
    cars = models.IntegerField()
    age = models.IntegerField()

    OCCUPATION_CHOICES = [
        ('Clerical', 'Clerical'),
        ('Management', 'Management'),
        ('Manual', 'Manual'),
        ('Professional', 'Professional'),
        ('Skilled Manual', 'Skilled Manual'),
    ]
    occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES)

    EDUCATION_CHOICES = [
        ('Bachelors', 'Bachelors'),
        ('Graduate Degree', 'Graduate Degree'),
        ('High School', 'High School'),
        ('Partial College', 'Partial College'),
        ('Partial High School', 'Partial High School'),
    ]
    education = models.CharField(max_length=50, choices=EDUCATION_CHOICES)

    marital_status = models.BooleanField(default=False)  # Married or not
    gender = models.BooleanField()  # 1 = Male, 0 = Female

    commute_lower = models.FloatField()
    commute_upper = models.FloatField()

    REGION_CHOICES = [
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('Pacific', 'Pacific'),
    ]
    region = models.CharField(max_length=50, choices=REGION_CHOICES)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase ID: {self.id}, Age: {self.age}, Purchased: {self.purchased_bike_binary}"

