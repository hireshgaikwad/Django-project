from django.urls import path
from .import views
urlpatterns = [
    path("",views.Indexpage,name="index"),
    path("signup/",views.SignupPage,name="signup"),
    path("register/",views.Register,name="register"),
    path("otppage/",views.OTPPage,name="otppage"),
    path("otp/",views.OTPverify,name="otp"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("login/",views.LoginUser,name="login"),
    path("profile/<int:pk>",views.ProfilePage,name="profile"),
    path("update/<int:pk>",views.Updateprofile,name="update"),
    path("joblist/",views.joblist,name="joblist"),


    ###################Company Side ######################


    path("companyindex/",views.companyindex,name="companyindex"),
    path("companyprofile/<int:pk>",views.companyprofilepage,name="companyprofile"),
    path("updatecompanyprofile/<int:pk>",views.updatecompanyprofile,name="updatecompanyprofile"),

    ################## Job post ##################

    path("jobpostpage/",views.jobpostpage,name="jobpostpage"),
    path("jobsubmit/<int:pk>",views.jobdetailsubmit,name="jobsubmit"),
    path("jobpostlist/",views.joblistpage,name="jobpostlist"),

    path("applypage/<int:pk>",views.jobapplypage,name="applypage"),
    path("apply/<int:pk>",views.Applyjob,name="apply"),
    path("applyjoblist/",views.jobapplylist,name="applyjoblist"),



    ################## Admin Login ################

    path("adminloginpage/",views.Adminloginpage,name="adminloginpage"),
    path("adminindex/",views.AdminIndexpage,name="adminindex"),
    path("adminlogin/",views.Aminlogin,name="adminlogin"),
    path("adminuserlist/",views.AdminUserList,name="userlist"),
    path("admincompanylist/",views.AdminCompanyList,name="companylist"),
    path("deleteuser/<int:pk>",views.UserDelete,name="deleteuser"),
    path("verifycompanypage/<int:pk>",views.VerifyCompanyPage,name="verifycompanypage"),
    path("verifycompany/<int:pk>",views.VerifyCompany,name="verifycompany"),
    path("deletecompany/<int:pk>",views.CompanyDelete,name="deletecompany"),
    
    path("home/",views.Userhome,name="home"),
    path("logout/",views.logout,name="logout"),
    path("adminlogout/",views.adminlogout,name="adminlogout")

    
]