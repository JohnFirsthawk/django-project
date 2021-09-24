from django.shortcuts import render,get_object_or_404
from .models import Users,Taxes
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

def index(request):
    num_users = Users.objects.all().count()
    num_taxes = Taxes.objects.all().count()
    num_taxes_extended = Taxes.objecs.filter(amount>100.000).count()

    context = {
        'num_users' : num_users,
        'num_taxes' : num_taxes,
        'num_taxes_extended' : num_taxes_extended,
    }
    return render(request, 'index.html', context=context)

def viewTaxes(request):
    data = Taxes.objects.all()
    context = {'alltaxes' : data}
    return render(request, 'taxes/taxes.html', context)

def viewUsers(request):
    data = Users.objects.all()
    context = {'allusers' : data}
    return render(request, 'taxes/users.html', context)

def detail(request, user_id):
    taxes = get_object_or_404(Taxes, pk=user_id)
    return render(request, 'taxes/detail.html', {'taxes': taxes})

class UserFormView(FormView):
    template_name = 'request.html'
    

def request(request,user_id):
    form = get_object_or_404(Users, pk=user_id)
    context = {'form': form}
    return render(request, 'taxes/request.html', context)

 