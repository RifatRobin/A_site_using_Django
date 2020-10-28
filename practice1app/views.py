from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Member
from practice1app.forms import MemberForm
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    members = Member.objects.all()
    member_list = members
    paginator = Paginator(member_list, 5)  # Show 5 contacts per page

    page = request.GET.get('page')
    members = paginator.get_page(page)

    #employees = Employee.objects.all()
    return render(request, "index.html", {'members': members})


def home(request):
    return render(request, 'home.html')


def reg(request):
    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print(form)
            try:
                form.save()

                return redirect('/home')

            except:
                pass

    else:
        form = MemberForm()

    return render(request, "reg.html", {'form': form})


def login(request):
    return render(request, 'login.html')
