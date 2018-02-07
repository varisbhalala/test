from django.shortcuts import render ,HttpResponseRedirect , HttpResponse
import datetime
from data.models import Publisher , Advertiser , User ,Board
from geopy.geocoders import Nominatim
from django.core.mail import send_mail , EmailMessage
from django.utils.crypto import get_random_string
# Create your views here.
def navigation(request):
    return render(request,'navigation.html')


def register(request):
    return render(request,'register.html')

def store(request):


        # if form.is_valid():
    if request.POST:
        role = request.POST.get('role')
        if role == 'p':
            form1 = Publisher()
        elif role == 'a':
            form1 = Advertiser()


        form1.name = request.POST.get('name')
        form1.contact = request.POST.get('contact_number')
        form1.email = request.POST.get('email')
        form1.avatar = request.FILES['image']

        form1.company_name = request.POST.get('company_name')
        form1.company_address = request.POST.get('company_address')
        form1.state = request.POST.get('state')
        form1.city = request.POST.get('city')
        created_at = datetime.datetime.now()
        form1.save()

        if role == 'p':
            record = Publisher.objects.all().order_by('-id')[0]
        elif role == 'a':
            record = Advertiser.objects.all().order_by('-id')[0]

        form_user = User()
        form_user.username = request.POST.get('username' )
        form_user.password = request.POST.get('password')
        created_at = datetime.datetime.now()
        form_user.role = request.POST.get('role')
        form_user.uid = form1.id
        form_user.save()
                # instance = form.save(commit=False)
                # instance.save()
        # form = ImageUploadForm(request.POST, request.FILES)
        # if form.is_valid():
        #     if role == 'p':
        #         m = Publisher()
        #     elif role == 'a':
        #         m = Advertiser()
        #
        #     m.avatar = form.cleaned_data['image']
        #     m.save()

    return render(request,'navigation.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/navigation/')

def login_check(request):
    if request.POST:
        username_session = request.POST.get('username')
        password_session = request.POST.get('password')


        if User.objects.filter(username = username_session, password = password_session):
            record = User.objects.get(username = username_session, password = password_session)
            request.session['username'] = username_session
            if record.role == 'p':
                record1 = Publisher.objects.filter(id = record.uid)
                record2 = Board.objects.filter(Publisher_id = record1[0].id)
                return render(request,'publisher_panel.html',{'record1':record1 , 'record2':record2})
            elif record.role == 'a':
                record1 = Advertiser.objects.filter(id = record.uid)
                return render(request,'advertiser_panel.html',{'record1':record1})
            else:
                return render(request, 'login.html' , {'error_message' : "username or password incorrect"})
        else:
            return render(request, 'login.html' , {'error_message' : "username or password incorrect"})

def publisher_panel(request):

    return render(request, 'publisher_panel.html')

def advertiser_panel(request):
    return render(request, 'advertiser_panel.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def check_email(request):
    if request.POST:
        role = request.POST.get('role')

        if role == 'p':
            record = Publisher.objects.get(email=request.POST.get('email'))

        elif role == 'a':
            record = Advertiser.objects.get(email=request.POST.get('email'))

        if record:
            unique_token = get_random_string(length=32)
            record1 = User.objects.get(uid=record.id)
            record1.token = unique_token
            record1.save()
            send_mail('Mail_from_mayur', "127.0.0.1:8000/new_password/?key="+unique_token,'digiboard2030@gmail.com', [request.POST.get('email')])
            # email = EmailMessage('reset password', 'your key is here' , request.POST.get('email'))
            # email.send()
            return HttpResponseRedirect('/forgot_password/')

        else:
            return render(request, 'forgot_password.html',{'incorrect_email': "email_id is incorrect"})



def new_password(request):
    token1 = request.GET['key']
    record1 = User.objects.filter(token=token1)
    return render(request, 'new_password.html',{'record1': record1})


def save_password(request):
    user = User.objects.get(id = request.POST.get('user_id'))
    new_password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    if new_password == confirm_password:
        user.password = new_password
        user.token = "NULL"
        user.updated_at = datetime.datetime.now()
        user.save()
        return HttpResponseRedirect('/login/')
    else:
        return render(request, 'new_password.html',{'incorrect_email': "new password and confirm password does not match"})


def create_board(request):
    return render(request, 'create_board.html')


def save_board(request):

    geolocator = Nominatim()
    form = Board()
    record1 = User.objects.get(username = request.session['username'])
    form.lat = request.POST['lat']
    form.lng = request.POST['lng']
    form.street = request.POST['street']
    form.area = request.POST['area']
    form.city = request.POST['city']
    form.state = request.POST['state']
    form.created_at = datetime.datetime.now()
    form.updated_at = datetime.datetime.now()
    form.Publisher_id = record1.uid
    form.save()
    return HttpResponseRedirect('/publisher_panel/')
