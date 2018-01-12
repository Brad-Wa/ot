from django.shortcuts import render, redirect
from models import Employee, Weekend
from django.contrib import messages
import datetime

# Create your views here.
def index(request):
    if 'logged' in request.session:
        return redirect('/home')
    return render(request, 'ot_app/login.html')

def login(request):
    if request.POST['num'] == '9999':
        request.session['logged'] = 'Admin'
        return redirect('/admin')
    try:
        Employee.objects.get(number = request.POST['num'])
        request.session['logged'] = request.POST['num']
        return redirect('/home')
    except:
        messages.add_message(request, messages.INFO, 'Employee not found')
        return redirect('/')

def home(request):
    emp = Employee.objects.get(number = request.session['logged'])
    date = datetime.date.today()
    end = datetime.date.today()
    print date.strftime('%a')
    while end.weekday() < 5:
        end= end.replace(day = end.day + 1)
        print end
        weekendnum = (end.timetuple().tm_yday)/7+1
    content={
    'employee' : emp,
    'weekend' : Weekend.objects.filter(employee = emp),
    'today' : date,
    'end' : end,
    'weekendnum' : weekendnum,
    }

    return render(request, 'ot_app/user.html', content)



def update(request):
    a = Employee.objects.get(number = request.session['logged'])

    end = datetime.date.today()
    while end.weekday() < 5:
        end= end.replace(day = end.day + 1)

    print end.timetuple()
    weekend = (end.timetuple().tm_yday)/7+1

    b = a.Weekend.get(weekend = weekend)
    b.saturday = request.POST['sat']
    b.sunday = request.POST['sun']
    b.save()

    return redirect('/home')



def admin(request):
    content = {
    'employees' : Employee.objects.all()
    }
    return render(request, 'ot_app/admin.html', content)
def create(request):
    if len(request.POST) < 1:
        messages.add_message(request, message.INFO,'Must input valid employee number')
        return redirect('/admin')
    try:
        Employee.objects.get(number = request.POST['num'])
        messages.add_message(request, messages.INFO, 'Employee already exists')
        return redirect('/admin')
    except:
        a = Employee.objects.create(number = request.POST['num'])
        for x in range(1,53):
            Weekend.objects.create(weekend = x, saturday = 0, sunday = 0, employee = a)
        return redirect('/admin')
def destroy(request, num):
    a = Employee.objects.filter(number = num)
    a.delete()
    messages.add_message(request, messages.INFO, 'Employee removed')
    return redirect('/admin')
def show(request, num):
    emp = Employee.objects.get(number = num)
    content={
    'employee' : emp,
    'weekend' : Weekend.objects.filter(employee = emp)
    }
    return render(request, 'ot_app/adminview.html', content)

def logout(request):
    request.session.clear()
    return redirect('/')
