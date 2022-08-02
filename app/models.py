from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now=True)
    is_updated = models.DateTimeField(auto_now=True)



class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    min_salary = models.BigIntegerField(default=0)
    max_salary = models.BigIntegerField(default=0)
    job_type = models.CharField(max_length=150)
    jobcategory = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    highestedu = models.CharField(max_length=150)
    experience = models.CharField(max_length=150)
    website = models.CharField(max_length=150)
    shift = models.CharField(max_length=150)
    jobdescription = models.CharField(max_length=500)
    profile_pic = models.ImageField(upload_to="app/img/candidate")


class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    website = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    logo_pic = models.ImageField(upload_to="app/img/company")


class JobDetails(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    jobname = models.CharField(max_length=250)
    companyname = models.CharField(max_length=250)
    companyaddress = models.CharField(max_length=250)
    jobdescription = models.TextField(max_length=500)
    qualification = models.CharField(max_length=250)
    responsibility = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    companywebsite = models.CharField(max_length=100)
    companyemail = models.EmailField(max_length=50)
    companycontact = models.CharField(max_length=20)
    salarypackage = models.CharField(max_length=50)
    experience = models.IntegerField()
    logo = models.ImageField(upload_to="app/img/jobpost")
    is_created = models.DateField(auto_now=True)
    is_upload = models.TimeField(auto_now=True)


class ApplyList(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    job = models.ForeignKey(JobDetails,on_delete=models.CASCADE)
    min_salary = models.CharField(max_length=100)
    max_salary = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    resume = models.FileField(upload_to="app/resume")