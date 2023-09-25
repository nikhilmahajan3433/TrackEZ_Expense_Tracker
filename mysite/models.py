from django.db import models
class usrs(models.Model):
    name=models.CharField(max_length=20)
    passw=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class transac(models.Model):
    # db_table="Transactions"

    trans=models.CharField(max_length=40)
    val=models.IntegerField()
    dtime=models.DateField(null=True)

class income(models.Model):
    title=models.CharField(max_length=40)
    value=models.IntegerField()
    timestamp=models.DateField()