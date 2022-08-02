
from random import randint
from django.shortcuts import render,redirect
from .models import *


# Create your views here.
def Indexpage(request):
    return render(request,"app/index.html")

def SignupPage(request):
    return render(request,"app/signup.html")

def Register(request):
    if request.POST['role'] == "Candidate":

        role = request.POST.get('role')
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']


        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User already exists"
            return render(request,"app/signup.html",{'msg':message})

        else:
            if password == cpassword:
                otp = randint(100000,999999)

                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)

                newcand = Candidate.objects.create(user_id=newuser,firstname=firstname,lastname=lastname)

                return render(request,"app/login.html",{'email':email})
            else:
                message = "Password missmatch!!"
                return render(request,"app/signup.html",{'msg':message})

    elif request.POST['role'] == "Company":
        
        role = request.POST.get('role')
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']


        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User already exists"
            return render(request,"app/signup.html",{'msg':message})

        else:
            if password == cpassword:
                otp = randint(100000,999999)

                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)

                newcand = Company.objects.create(user_id=newuser,firstname=firstname,lastname=lastname)

                return render(request,"app/login.html",{'email':email})
            else:
                message = "Password missmatch!!"
                return render(request,"app/signup.html",{'msg':message})

    else:
        message = "Select Role"
        return render(request,"app/signup.html",{'msg':message})

def OTPPage(request):
    return render(request,"app/otp.html")

def OTPverify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)

    if user:
        if user.otp == otp:
            message = "Otp verified successfully!!"

            return render(request,"app/login.html",{'msg':message})

        else:
            message = "OTP is incorrect"
            return render(request,"app/otp.html",{'msg':message})

    else:
        message = "User not found"
        return render(request,"app/signup.html",{'msg':message})

def LoginPage(request):
    return render(request,"app/login.html")


def LoginUser(request):
    if request.POST['role']=="Candidate":
        email = request.POST['email']
        password = request.POST['password']


        user = UserMaster.objects.get(email=email)

        if user:
            if user.password==password and user.role=="Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email
                request.session['password'] = user.password

                return redirect('home')
            else:
                message = "Password Missmatch"
                return render(request,"app/login.html",{'msg':message})

        else:
            message = "User does not exists"
            return render(request,"app/login.html",{'msg':message})

    elif request.POST['role']=="Company":
        
        email = request.POST['email']
        password = request.POST['password']


        user = UserMaster.objects.get(email=email)

        if user:
            if user.password==password and user.role=="Company":
                camp = Company.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = camp.firstname
                request.session['lastname'] = camp.lastname
                request.session['email'] = user.email
                request.session['password'] = user.password

                return redirect('companyindex')
            else:
                message = "Password Missmatch"
                return render(request,"app/login.html",{'msg':message})

        else:
            message = "User does not exists"
            return render(request,"app/login.html",{'msg':message})

    else:
        message = "Select role!!"
        return render(request,"app/login.html",{'msg':message})

def Userhome(request):
    return render(request,"app/home.html")

def ProfilePage(request,pk):
       
    user = UserMaster.objects.get(pk=pk)
    can = Candidate.objects.get(user_id=user)
    return render(request,"app/profile.html",{'user':user, 'can':can})



def Updateprofile(request,pk):

    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)

        can.dob = request.POST['dob']
        can.address = request.POST['address']
        can.city = request.POST['city']
        can.state = request.POST['state']
        can.country = request.POST['country']
        can.job_type = request.POST['jobtype']
        can.jobcategory = request.POST['jobcategory']
        can.min_salary = request.POST['min']
        can.max_salary = request.POST['max']
        can.highestedu = request.POST['education']
        can.experience = request.POST['experience']
        can.website = request.POST['website']
        can.contact = request.POST['contact']
        can.gender = request.POST['gender']
        can.shift = request.POST['shift']
        can.jobdescription = request.POST['jobdescription']
        can.profile_pic = request.FILES['image']
        can.save()
        print("Data Saved!!")
        url = f'/profile/{pk}'
        return redirect(url)

############################Company Side ##############################

def companyindex(request):
    

    return render(request,"app/company/index.html")


def companyprofilepage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id=user)

    return render(request,"app/company/profile.html",{'user':user, 'comp':comp})


def updatecompanyprofile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)

        comp.firstname = request.POST['fname']
        comp.lastname = request.POST['lname']
        comp.company_name = request.POST['cname']
        comp.state = request.POST['state']
        comp.city = request.POST['city']
        comp.website = request.POST['cwebsite']
        comp.address = request.POST['caddress']
        comp.contact = request.POST['ccontact']
        comp.description = request.POST['cdescription']
        comp.logo_pic = request.FILES['img']
        comp.save()
        print("Data Saved")

        

        url = f'/companyprofile/{pk}'
        return redirect(url)



################## Posting a Job #################

def joblist(request):
    all_job = JobDetails.objects.all()
    return render(request,"app/job-list.html",{'all_job':all_job})


def jobpostpage(request):
    return render(request,"app/company/jobpost.html")


def jobdetailsubmit(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        jname = request.POST['jobname']
        jdescription = request.POST['jdescription']
        qualification = request.POST['qualification']
        experience = request.POST['jexperience']
        responsibilities = request.POST['responsibilities']
        salary = request.POST['salary']
        cname = request.POST['compname']
        caddress = request.POST['compaddress']
        ccontact = request.POST['compcontact']
        cemail = request.POST['compemail']
        cwebsite = request.POST['compwebsite']
        clocation = request.POST['complocation']
        logo = request.FILES['compimg']

        newjob = JobDetails.objects.create(company_id=comp,jobname=jname,jobdescription=jdescription,qualification=qualification,experience=experience,responsibility=responsibilities,salarypackage=salary,companyname=cname,companyaddress=caddress,companycontact=ccontact,companyemail=cemail,companywebsite=cwebsite,location=clocation,logo=logo)

        message = "Job has been posted successfully!!"

        return render(request,"app/company/jobpost.html",{'msg':message})



def joblistpage(request):
    all_job = JobDetails.objects.all()
    return render(request,"app/company/joblist.html",{'all_job':all_job})


################# Job apply ###############

def jobapplypage(request,pk):

    user = request.session['id']
    if user:
        cand = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(id=pk)


    


    return render(request,"app/apply.html",{'user':user, 'cand':cand, 'job':job})


def Applyjob(request,pk):
    user = request.session['id']
    if user:
        cand = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(id=pk)

        min_salary = request.POST['min']
        max_salary = request.POST['max']
        experience = request.POST['experience']
        website = request.POST['website']
        gender = request.POST['gender']
        state = request.POST['state']
        resume = request.FILES['resume']

        newapply = ApplyList.objects.create(candidate=cand,job=job,min_salary=min_salary,max_salary=max_salary,website=website,gender=gender,experience=experience,state=state,resume=resume)

        message = "Job applied successfully"

        return render(request,"app/apply.html",{'msg':message})



def jobapplylist(request):

    all_apply = ApplyList.objects.all()

    return render(request,"app/company/applyjoblist.html",{'alljob':all_apply})




################ Admin Side #################


def Adminloginpage(request):
    return render(request,"app/admin/login.html")





def Aminlogin(request):
    username = request.POST['username']
    password = request.POST['password']

    if username == "admin" and password == "admin":

        request.session['username'] = username
        request.session['password'] = password
        return redirect('adminindex')

    else:
        message = "Username and password not match"
        return render(request,"app/admin/login.html",{'msg':message})


def AdminIndexpage(request):
    if 'username' in request.session and 'password' in request.session:
        return render(request,"app/admin/index.html")
    else:
        return redirect('adminloginpage')


def AdminUserList(request):
    all_user = UserMaster.objects.filter(role="Candidate")
    return render(request,"app/admin/userlist.html",{'all_user':all_user})

def AdminCompanyList(request):
    all_company = UserMaster.objects.filter(role="Company")
    return render(request,"app/admin/companylist.html",{'all_company':all_company})


def UserDelete(request,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()

    return redirect('userlist')


def VerifyCompanyPage(request,pk):
    comp = UserMaster.objects.get(pk=pk)

    if comp:
        return render(request,"app/admin/companyverify.html",{'comp':comp})


def VerifyCompany(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        company.is_verified = request.POST['verify']
        company.save()
        return redirect('companylist')


def CompanyDelete(request,pk):
    company = UserMaster.objects.get(pk=pk)
    company.delete()

    return redirect('companylist')


def logout(request):
    del request.session['email']
    del request.session['password']
    del request.session['role']
    return redirect('index')

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect('index')

