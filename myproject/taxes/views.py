from django.shortcuts import render,get_object_or_404
from .models import Users,Taxes
from django.contrib.auth.decorators import login_required


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