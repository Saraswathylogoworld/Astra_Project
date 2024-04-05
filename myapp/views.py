from email import message
from time import ctime
from django import db
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
from myapp.models import RegsaveC, RegsaveG, regsave, logsave

def Guidance_job(request):
    return render(request,"guidance/add_course.html")    

def ga_add(request ):
    if request.method=='POST':
        gname=request.POST.get('gname')
        qua=request.POST.get('qua')
        quan=request.POST.get('quan')
        ctime=request.POST.get('ctime')
        place=request.POST.get('place')
        rfee=request.POST.get('rfee')
        des=request.POST.get('des')
        number=request.POST.get('number')
        img=request.FILES['img']
        data=G_ADD_guidance1(gname=gname,des=des,ctime=ctime,place=place,qua=qua,quan=quan,number=number,rfee=rfee,img=img)
        data.save()
    return redirect('gtable')    


def gtable(request):
    data = G_ADD_guidance1.objects.all()
    return render(request,'guidance/G_table.html',{'data':data})

def g_edit(request,geid):
    data = G_ADD_guidance1.objects.filter(id=geid)
    return render(request,'guidance/G_editdetails.html',{'data':data})

def g_update(request,g_id):
    if request.method=='POST':
        gname=request.POST.get('gname')
        qua=request.POST.get('qua')
        quan=request.POST.get('quan')
        ctime=request.POST.get('ctime')
        place=request.POST.get('place')
        rfee=request.POST.get('rfee')
        des=request.POST.get('des')
        number=request.POST.get('number')
        try:
            img=request.FILES['img']
            fs = FileSystemStorage() 
            file = fs.save(img.name, img)
        except MultiValueDictKeyError :
            file=G_ADD_guidance1.objects.get(id=g_id).img
        data=G_ADD_guidance1.objects.filter(id=g_id).update(gname=gname,ctime=ctime,des=des,place=place,qua=qua,quan=quan,number=number,rfee=rfee,img=file)
    return redirect('gtable')


def g_delete(request,g_did):
    data=G_ADD_guidance1.objects.filter(id=g_did).delete()
    return redirect('gtable') 

def homeview(request):
    return render(request,"guidance/index.html")

def login1(request):
    return render(request,"user/login1.html")

def user_contact(request):
    return render(request,"guidance/contacts.html")

def CG_details(request):
    data=C_ADD_job1.objects.all()
    return render(request,"guidance/c_details.html",{'data':data})        


def apply_details(request):
    data=C_ADD_job1.objects.all()
    return render(request,"guidance/apply_G.html",{'data':data})   

def a_add(request ):
    if request.method=='POST':
        cname=request.POST.get('cname')
        pname=request.POST.get('pname')
        qua=request.POST.get('qua')
        quan=request.POST.get('quan')
        place=request.POST.get('place')
        amount=request.POST.get('amount')
        ex=request.POST.get('ex')
        sname=request.POST.get('sname')
        gender = request.POST.get('gender')
        cv = request.FILES['cv']
        data=DETAIL_APPLY(cname=cname,pname=pname,sname=sname,ex=ex,place=place,qua=qua,quan=quan,amount=amount,gender=gender,cv=cv)
        data.save()
    return redirect('CG_details')   

def register2(request):
    return render(request,"guidance/registerG.html")

def Gregistersave(request):
    if request.method == "POST":
        b = RegsaveG()
        b.name = request.POST.get("fname")
        b.mail = request.POST.get("fmail")
        b.password = request.POST.get("fpassword")
        b.course = request.POST.get("fcourse")
        b.year = request.POST.get("fyear")
        b.number = request.POST.get("fnumber")
        b.re_pass = request.POST.get("re_pass")
        b.save()
        return render(request,"gaidance/Glogin.html")


def login2(request):
    return render(request,"guidance/Glogin.html")

def loginsave(request):
    name = request.POST.get('fname')
    password = request.POST.get('fpassword')
    if (RegsaveG.objects.filter(name=name,password=password).exists()):
        data = RegsaveG.objects.filter(name=name,password=password).values('mail','course','year','number','re_pass','id').first()
        request.session['mail']=data['mail']
        request.session['number']=data['number']
        request.session['course']=data['course']
        request.session['year']=data['year']
        request.session['re_pass']=data['re_pass']
        request.session['id']=data['id']
        request.session['name']=name 
        request.session['password']=password
        return redirect('homeview')
        
    else:
        return render(request,'user/login1.html',{'msg':"Sorry... Invalid username or password"})

def adminlogin(request):
    return render(request,"admin/admin.html")

def IndexAdmin(request):
    return render(request,"admin/adminindex.html")
    
def Userindex(request):
    data=G_ADD_guidance1.objects.all()
    data1=C_ADD_job1 .objects.all()
    return render(request,"user/user_index.html",{'data':data,'data1':data1})

def register3(request):
    return render(request,"company/registerC.html")

def Cregistersave(request):
    if request.method == "POST":
        b = RegsaveC()
        b.name = request.POST.get("fname")
        b.mail = request.POST.get("fmail")
        b.password = request.POST.get("fpassword")
        b.jobcate = request.POST.get("fjobcate")
        b.year = request.POST.get("fyear")
        b.number = request.POST.get("fnumber")
        b.re_pass = request.POST.get("re_pass")
        b.save()
        return render(request,"company/Clogin3.html")


def login3(request):
    return render(request,"company/Clogin3.html")

def loginsave3(request):
    name = request.POST.get('fname')
    password = request.POST.get('fpassword')
    if (RegsaveC.objects.filter(name=name,password=password).exists()):
        data = RegsaveC.objects.filter(name=name,password=password).values('mail','jobcate','year','number','re_pass','id').first()
        request.session['mail']=data['mail']
        request.session['number']=data['number']
        request.session['jobcate']=data['jobcate']
        request.session['year']=data['year']
        request.session['re_pass']=data['re_pass']
        request.session['id']=data['id']
        request.session['name']=name 
        request.session['password']=password
        return redirect('Company_index')
        
    else:
        return render(request,'company/Clogin3.html',{'msg':"Sorry... Invalid username or password"})


def Company_index(request):
    return render(request,"company/CIndex.html")

def Company_contact(request):
    return render(request,"company/contactC.html")

def Company_job(request):
    data = C_ADD_job1.objects.all()
    return render(request,"company/add_job.html",{'data':data})    

def c_add(request ):
    if request.method=='POST':
        pname=request.POST.get('pname')
        cname=request.POST.get('cname')
        qua=request.POST.get('qua')
        place=request.POST.get('place')
        quan=request.POST.get('quan')
        ex=request.POST.get('ex')
        amount=request.POST.get('amount')
        vaccancy=request.POST.get('vaccancy')
        des=request.POST.get('des')
        img=request.FILES['img']
        data=C_ADD_job1(pname=pname,cname=cname,des=des,place=place,ex=ex,qua=qua,quan=quan,vaccancy=vaccancy,amount=amount,img=img)
        data.save()
    return redirect('ctable')    

def ctable(request):
    data = C_ADD_job1.objects.all()
    return render(request,'company/C_table.html',{'data':data})

def c_edit(request,ceid):
    data = C_ADD_job1.objects.filter(id=ceid)
    return render(request,'company/C_editdetails.html',{'data':data})

def c_update(request,c_id):
    if request.method=='POST':
        pname=request.POST.get('pname')
        cname=request.POST.get('cname')
        qua=request.POST.get('qua')
        quan=request.POST.get('quan')
        place=request.POST.get('place')
        ex=request.POST.get('ex')
        amount=request.POST.get('amount')
        des=request.POST.get('des')
        vaccancy=request.POST.get('vaccancy')
        try:
            img=request.FILES['img']
            fs = FileSystemStorage() 
            file = fs.save(img.name, img)
        except MultiValueDictKeyError :
            file=C_ADD_job1.objects.get(id=c_id).img
        data=C_ADD_job1.objects.filter(id=c_id).update(pname=pname,des=des,cname=cname,place=place,ex=ex,qua=qua,quan=quan,vaccancy=vaccancy,amount=amount,img=file)
    return redirect('ctable')


def c_delete(request,c_did):
    data=C_ADD_job1.objects.filter(id=c_did).delete()
    return redirect('ctable') 

def Company_details(request):
    data=G_ADD_guidance1.objects.all()
    return render(request,"company/detailsC.html",{'data':data}) 

def Company_about(request):
    return render(request,"company/aboutC.html") 

def C_shedule(request):
    data = S_Details1.objects.all()
    data1 = C_Details.objects.all()
    return render(request,"user/shedule_C.html",{'data':data,'data1':data1})

def register1(request):
    return render(request,"user/regstr.html")

def registersave(request):
    if request.method == "POST":
        a = regsave()
        a.name = request.POST.get("fname")
        a.mail = request.POST.get("fmail")
        a.password = request.POST.get("fpassword")
        a.mark = request.POST.get("fmark")
        a.number = request.POST.get("fnumber")
        a.re_pass = request.POST.get("re_pass")
        a.save()
        return render(request,"user/login1.html")                   

def logchk(request):
    name = request.POST.get('fname')
    password = request.POST.get('fpassword')
    type = request.POST.get('type')  
    if (name=='Admin1' and password=="Admin1"):
        return render(request,'admin/adminindex.html')
    elif (regsave.objects.filter(name=name,password=password).exists()and type=='user'):
        data = regsave.objects.filter(name=name,password=password).values('mail','mark','number','re_pass','id').first()
        request.session['mail']=data['mail']
        request.session['number']=data['number']
        request.session['mark']=data['mark']
        request.session['re_pass']=data['re_pass']
        request.session['id']=data['id']
        request.session['name']=name 
        request.session['password']=password
        request.session['type']=type
        return redirect('home6')
    elif (RegsaveG.objects.filter(name=name,password=password).exists()and type=='guidance'):
        return render (request,'guidance/index.html')

    elif (RegsaveC.objects.filter(name=name,password=password).exists()and type=='company'):
        return render (request,'company/CIndex.html')    
   
    else:
        return render(request,'user/login1.html',{'msg':"Sorry... Invalid username or password"})

def Viewlogout(request):
    del request.session['name']
    del request.session['password']  
    del request.session['mail']
    del request.session['re_pass']
    del request.session['mark']
    del request.session['number']
    del request.session['id']
    return redirect('home1') 


def Cuser(request):
    return render(request,"user/company_user.html")    

def u_add(request ):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        pname=request.POST.get('pname')
        ex=request.POST.get('ex')
        message=request.POST.get('message')
        file=request.FILES['file']
        data=C_USER1(name=name,email=email,number=number,pname=pname,ex=ex,message=message,file=file)
        data.save()
    return redirect('Cuser')     

def G_Job_table_admin(request):
    data1 = G_USER1.objects.all()
    return render(request,'admin/guidance_job.html',{'data1':data1})

def applyJob_table_admin(request):
    data1 = C_USER1.objects.all()
    return render(request,'admin/job_apply_table.html',{'data1':data1})

def U_user(request):
    return render(request,"user/course_user.html")   

def g_add(request ):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        cname=request.POST.get('cname')
        qua=request.POST.get('qua')
        message=request.POST.get('message')
        file=request.FILES['file']
        data=G_USER1(name=name,email=email,number=number,cname=cname,qua=qua,message=message,file=file)
        data.save()
    return redirect('U_user')        

def admin_c_table(request):
    data1 = C_ADD_job1.objects.all()
    return render(request,'admin/company_D.html',{'data1':data1})


def guidance_details(request):
    data1=G_ADD_guidance1.objects.all()
    return render(request,"admin/G_detailsT.html",{'data1':data1})

def sd(request):
    return render(request,"admin/studntdetail.html") 

def s_add_d(request ):
    if request.method=='POST':
        sname=request.POST.get('sname')
        cname=request.POST.get('cname')
        location=request.POST.get('location')
        number=request.POST.get('number')
        email=request.POST.get('email')
        year=request.POST.get('year')
        img=request.FILES['img']
        data=S_Details1(sname=sname,year=year,cname=cname,location=location,email=email,number=number,img=img)
        data.save()
    return redirect('ld')    


def ld(request):
    data = S_Details1.objects.all()
    return render(request,"admin/lists.html",{'data':data})           


def admin_d(request):
    return render(request,"admin/CourseAdd.html") 

def c_d(request ):
    if request.method=='POST':
        pname=request.POST.get('pname')
        month=request.POST.get('month')
        location=request.POST.get('location')
        number=request.POST.get('number')
        cs=request.POST.get('cs')
        ctime=request.POST.get('ctime')
        img=request.FILES['img']
        data=C_Details(pname=pname,month=month,ctime=ctime,location=location,cs=cs,number=number,img=img)
        data.save()
    return redirect('ad')    


def ad(request):
    data = C_Details.objects.all()
    return render(request,"admin/corse_table.html",{'data':data})           



