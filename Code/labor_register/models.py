from django.db import models



GENDER_CHOICE = (
    ("Male","Male"),
    ("Female","Female"),
    ("Bigender","Bigender")
)

WORK_CHOICE = (
    ("Professionals","Professionals"),
    ("Legislators","Legislators"),
    ("Senior officials and managers","Senior officials and managers"),
    ("Technicians and associate professionals","Technicians and associate professionals"),
    ("Elementary occupations","Elementary occupations"),
    ("Service workers","Service workers"),
    ("Shop and market sales workers","Shop and market sales workers"),
    ("Skilled agricultural and fishery workers","Skilled agricultural and fishery workers"),
    ("Craft and related trades workers","Craft and related trades workers"),
    ("Plant and machine operators and assemblers","Plant and machine operators and assemblers"),
    ("Clerks","Clerks"),
    ("Other","Other")
)

WORK_TYPE_CHOICE = (
    ("Daily","Daily"),
    ("Weekly","Weekly")
)

COMMUNITY_CHOICE = (
    ("Urban","Urban"),
    ("Rural","Rural")
)

# Create your models here.

class Supervisor(models.Model):
    Supervisor_ID =models.IntegerField(primary_key=True)
    Rating = models.FloatField()
    No_of_laborers = models.IntegerField()
    class Meta:
        db_table = 'Supervisor'
    def __str__(self):
        return str(self.Supervisor_ID)   
        
class Municipal_Department(models.Model):
    City_ID = models.IntegerField()
    Dept_ID = models.IntegerField(primary_key=True)
    Overall_rating = models.FloatField()
    Total_expense = models.IntegerField()
    UPI_ID_payer = models.CharField(max_length=1000)
    class Meta:
        db_table = 'Municipal Department'
    def __str__(self):
        return str(self.Dept_ID)      

class City_Details(models.Model):
    City_ID = models.ForeignKey(Municipal_Department, on_delete=models.CASCADE)
    Dept_ID = models.IntegerField(primary_key=True)
    City_name = models.CharField(max_length=100)
    No_of_Laborers = models.IntegerField()
    No_of_Supervisor = models.IntegerField()
    class Meta:
        db_table = 'City details'
    def __str__(self):
        return self.City_name     

class Labor(models.Model):
    Labor_ID = models.IntegerField(primary_key=True)
    Supervisor_ID = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    Rating = models.FloatField()
    City_ID  = models.ForeignKey(City_Details,on_delete=models.Aggregate)
    Name = models.CharField(max_length=500)
    Gender = models.CharField(max_length=20,choices = GENDER_CHOICE)
    Work = models.CharField(max_length=500,choices=WORK_CHOICE)
    Work_type = models.CharField(max_length=25,choices=WORK_TYPE_CHOICE,default="Daily")
    class Meta:
        db_table = 'Labor'
    def __str__(self):
        return str(self.Labor_ID)     

class Labor_Personal_Details(models.Model):
    Labor_ID = models.ForeignKey(Labor, on_delete=models.CASCADE)
    PinCode = models.IntegerField()
    Gender = models.CharField(max_length=20,choices = GENDER_CHOICE)
    Date_of_Birth = models.DateTimeField()
    Name = models.CharField(max_length=500)
    Community = models.CharField(max_length=10,choices=COMMUNITY_CHOICE,default='Urban')
    City_ID = models.ForeignKey(City_Details,on_delete=models.DO_NOTHING)
    class Meta:
        db_table = 'Labor_Personal_Details'
    def __str__(self):
        return str(self.Labor_ID)     
                



