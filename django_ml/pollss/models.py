from django.db import models

class titanic(models.Model):
    pclass = models.IntegerField()
    sex = models.IntegerField()
    age = models.IntegerField()
    sibsq = models.IntegerField()
    parch = models.IntegerField()
    fare = models.IntegerField()
    embC = models.IntegerField()
    embQ = models.IntegerField()
    embS = models.IntegerField()

    def __str__(self):
        return f"{self.pclass} {self.sex} {self.age} {self.sibsq} {self.parch} {self.fare} {self.embC} {self.embQ} {self.embS}"


