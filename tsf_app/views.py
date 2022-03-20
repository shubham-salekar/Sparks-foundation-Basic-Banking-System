from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request,'tsf_app/index.html')
def customers(request):
    customers = CustomerDetail.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')
        semail = request.POST.get('semail')
        amt = request.POST.get('amt')
        try:
            amt = int(amt)
        except:
            # print("enter amount")
            redirect('customers')
        for customer in customers:
            if customer.email == email:
                j = customer
                id = customer.id
                break
        for customer in customers:
            # print(customer.email,customer.available_balance,semail)

            if customer.email==semail and amt< int(customer.available_balance) and amt>0 :
                available_balance = int(customer.available_balance) - amt
                available_balance2 = j.available_balance + amt
                try:
                    transaction_detail1 = TransactionDetail(name=customer.name, email=customer.email,
                                                debit_amount=amt ,credit_amount=0 , account_balance=available_balance)

                    customer_details = CustomerDetail(id=customer.id, available_balance=available_balance, email=customer.email
                                                    , name=customer.name)
                    transaction_details = TransactionDetail(name=j.name, email=j.email,
                                                debit_amount=0 ,credit_amount=amt , account_balance=available_balance2)
                    customer_detail = CustomerDetail(id=id, available_balance=available_balance2, email=j.email
                                                    , name=j.name)
                    customer_details.save()
                    transaction_detail1.save()
                    customer_detail.save()
                    transaction_details.save()
                    
                    return redirect('customers')

                except:
                    messages.error(request,'Transaction Failed')
                    break
        else:
            print("invalid data")
            messages.error(request,'Transaction Failed,Check Your Account Balance')

    trans = TransactionDetail.objects.all()
    context={
        'customers':customers,
        'trans':trans
    }
                
    return render(request,'tsf_app/customers_page.html',context)
