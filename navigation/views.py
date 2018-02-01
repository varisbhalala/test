from django.shortcuts import render
import datetime
from data.models import Publisher , Advertiser , User
from .forms import ImageUploadForm
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
        form1.avatar = request.FILES['image'].name

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
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            if role == 'p':
                m = Publisher()
            elif role == 'a':
                m = Advertiser()

            m.avatar = form.cleaned_data['image']
            m.save()

    return render(request,'navigation.html')
