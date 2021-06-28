from django.shortcuts import render
from django.http import HttpResponse
from .models import Register

# Create your views here.

def home(request):
	return HttpResponse("Hi Good Evening to All...")

def htmltag(y):
	return HttpResponse("<h2> Hi welcome to APSSDC program </h2>")

def usernameprint(request,uname):
	return HttpResponse("<h2>Hi Welcome <span style='color:blue'>{}</span></h2>".format(uname))

def usernameage(request,un,ag):
	return HttpResponse("<h3 style='text-align:center;background-color:pink'>Hi User <span style='color:blue'>{}</span> and your age is: <span style='color:green'>{}</span></h3>".format(un,ag))

def empdetails(request,eid,eage,ename):
	return HttpResponse("<script>alert('HI Welcome {}')</script><h3>Hi Welcome {} and your age is: {} and your id is: {}</h3>".format(ename,ename,eage,eid))
def htm(req):
	return render(req,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def empname(request,id,ename):
	k = {'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)

def studentdetails(request):
	return render(request,'html/std.html')

def  internalJS(request):
	return render(request,'html/internalJS.html')

def myform(req):
	if req.method=="POST":
		#print(req.POST)
		uname = req.POST['uname']
		Rollno = req.POST['Rollno']
		Emailid = req.POST['Emailid']
		#print(uname,Rollno,Emailid)
		data = {'username':uname,'rno':Rollno,'emailid':Emailid}
		return render(req,'html/display.html',data)
	return render(req,'html/myform.html')

def register(req):
	if req.method=="POST":
		fname = req.POST['fname']
		lname = req.POST['lname']
		psd = req.POST['psd']
		gender = req.POST['gender']
		email = req.POST['email']
		phnno = req.POST['phnno']
		address = req.POST['address']
		lang = req.POST['lang']
		data = {'Firstname':fname,'Lastname':lname,'Password':psd,'Gender':gender,'Email':email,'Phnno':phnno,'Address':address,'Languages':lang}
		return render(req,'html/Rdisplay.html',data)
	return render(req,'html/register.html')

def submit(req):
	if req.method=="POST":
		fname = req.POST['fname']
		lname = req.POST['lname']
		pwd = req.POST['pwd']
		gender = req.POST['gender']
		email = req.POST['email']
		phone = req.POST['phone']
		address = req.POST['address']
		lang = req.POST['lang']
		data = {'Firstname':fname,'Lastname':lname,'Password':pwd,'Gender':gender,'Email':email,'phone':phone,'Address':address,'Languages':lang}
		return render(req,'html/submitdisplay.html',data)
	return render(req,'html/submit.html')

def login(req):
	return render(req,'html/login.html')

def btregi(request):
	return render(request,'html/btregst.html')

def register1(request):
	# name = "sowmya"
	# email = "sowmya@gmail.com"
	reg = Register(name = "sneha",email = "sneha@gmail.com")
	reg.save()
	return HttpResponse("row inserted successfully......")

def register2(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST.get('email')
		reg = Register(name = name,email = email)
		reg.save()
		return HttpResponse("record inserted successfully.....")
	return render(request,"html/register2.html")

def display1(request):
	data = Register.objects.all()
	return render(request,"html/display1.html",{'data':data})

def sview(request,y):
	w = Register.objects.get(id=y)
	return HttpResponse("Your Name is: {} and your email id is: {}".format(w.name,w.email))

def sview(request,y):
	w = Register.objects.get(id=y)
	return render(request,'html/sview.html',{'y':w})
	# return HttpResponse("Your Name is: {} and Your email id is: {}".format(w.name,w.email))

def supt(request,q):
	t = Register.objects.get(id=q)
	if request.method == "POST":
		na = request.POST['n']
		em = request.POST['e']
		ry = Register()
		t.name = na
		t.email = em
		t.save()
		return redirect('/display')
	return render(request,'html/supdate.html',{'p':t})

def sudl(request,p):
	b = Register.objects.get(id=p)
	if request.method == "POST":
		b.delete()
		return redirect('/display')
	return render(request,'html/sndlt.html',{'z':b})