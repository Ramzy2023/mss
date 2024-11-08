from django.db import models

# Create your models here.
class Division(models.Model):
    division_name = models.CharField(max_length=100, verbose_name='Division Name')

    def __str__(self) -> str:
        return self.division_name

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.supplier_name
    
class Classification(models.Model):
    class_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.class_name

class Office(models.Model):
    office_name = models.CharField(max_length=100, verbose_name="Office Name")
    office_code = models.CharField(max_length=200, blank=True, null=True)
    division = models.ForeignKey(Division,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.office_name

class Unit_list(models.Model):
    unit_measure = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.unit_measure
    
class Fund_cluster(models.Model):
    fund_name = models.CharField(max_length=50)
    fund_code = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.fund_name

class Position(models.Model):
    position_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.position_name

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    office = models.ForeignKey(Office,on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.employee_name

class Stock(models.Model):
    stock_num = models.CharField(max_length=100)
    stock_name = models.CharField(max_length=100)
    unit = models.ForeignKey(Unit_list,on_delete=models.CASCADE)
    stock_qty = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self) -> str:
        return self.stock_name

