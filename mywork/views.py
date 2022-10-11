
from unicodedata import name
from django import views
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.conf import settings
from django.contrib import messages
from mywork.models import testimonial,profile,payment1,wallet,investment,withdraw,Contact,investors_depo,investors_payed,percentage
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Value 
from django.core.mail import EmailMultiAlternatives
from django.core.mail.message import EmailMessage
from email.mime.image import MIMEImage
from django.core import mail
from django.template import loader
import os
from decimal import Decimal
import decimal

# Create your views here.
def index(request):
    # code= str(kwargs.get('ref_code'))
    # try:
    #     Profile=profile.objects.get(code=code)
    #     request.session['ref_profile']= Profile.id
    #     print('id', Profile.id)
    # except:
    #     pass    
    
    test = testimonial.objects.all()
    i_depo = investors_depo.objects.all()
    i_payed = investors_payed.objects.all()

    context = {
        'test':test,
        'i_depo':i_depo,
        'i_payed':i_payed,}


    return render(request, 'index.html',context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
          auth.login(request,user)
          template=loader.get_template('login_info.text')
                
          var={
            'user':user
                } 
          message = template.render(var)  
          email =EmailMultiAlternatives(
                'Login Notice', message, 'Bestfuturetrade',
                [request.user.email]
                )
          email.content_subtype='html'
          email.mixed_subtype='related'   
          email.send()
          return redirect('dash')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')    
    else:
       return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url='login')
def dash(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)
    balance= payment1.objects.filter(user=request.user,bol='True').aggregate(total=Sum('amt1'))['total'] or Decimal()
    inv_balance= investment.objects.filter(user=request.user,bol='False').aggregate(total=Sum('amt1'))['total'] or Decimal()
    wtd_balance= withdraw.objects.filter(user=request.user).aggregate(total=Sum('amt'))['total'] or Decimal()
    bonus= percentage.objects.filter(user=request.user).aggregate(total=Sum('amt'))['total'] or Decimal()

    acc= balance + bonus - inv_balance 
    acc_balance = acc - wtd_balance 

     
    
    
    
    context={
        'user_profile':user_profile,
        'acc_balance':acc_balance,
        'inv_balance':inv_balance,
    }


    
    return render(request, 'dash.html',context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()

                # log user in and redirect to settings page
                # user_login = auth.authenticate(username=username, password=password)
                # auth.login(request, user_login)


                user_model = User.objects.get(username=username)
                new_profile = profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()

                
                return redirect('login')
        else:
            messages.info(request,'passwords not match')
            return redirect('register')

    else:
      return render(request,'register.html')

@login_required(login_url='login')
def deposit(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)
    if request.method =='POST':
        if request.POST.get('amt1','coin1'):
            depo1=payment1()
            depo1.amt1=request.POST.get('amt1')
            depo1.coin1=request.POST.get('coin1')
            depo1.user =request.user
            depo1.save()


            if depo1.coin1=='BTC':
                template=loader.get_template('deposit_info1.text')
                
                var={
                    'user':request.user,
                   'amt':depo1.amt1,
                   'coin':depo1.coin1,
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                        'Deposit Request', message, 'Bestfuturetrade',
                        [request.user.email]
                        )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()
                return redirect('pay1')

            elif depo1.coin1=='ETH':
                template=loader.get_template('deposit_info2.text')
                
                var={
                    'user':request.user,
                   'amt':depo1.amt1,
                   'coin':depo1.coin1,
                   
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                        'Deposit Request', message, 'Bestfuturetrade',
                        [request.user.email]
                        )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()
                return redirect('pay2')

            elif depo1.coin1=='LTC':
                template=loader.get_template('deposit_info3.text')
                
                var={
                    'user':request.user,
                   'amt':depo1.amt1,
                   'coin':depo1.coin1,
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                        'Deposit Request', message, 'Bestfuturetrade',
                        [request.user.email]
                        )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()
                return redirect('pay3')

            elif depo1.coin1=='TRC':
                template=loader.get_template('deposit_info4.text')
                
                var={
                    'user':request.user,
                   'amt':depo1.amt1,
                   'coin':depo1.coin1,
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                        'Deposit Request', message, 'Bestfuturetrade',
                        [request.user.email]
                        )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()
                return redirect('pay4')

            elif depo1.coin1=='BNB':
                template=loader.get_template('deposit_info5.text')
                
                var={
                    'user':request.user,
                   'amt':depo1.amt1,
                   'coin':depo1.coin1,
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                        'Deposit Request', message, 'Bestfuturetrade',
                        [request.user.email]
                        )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()
                return redirect('pay5') 

            elif depo1.coin1=='BCH':
                template=loader.get_template('deposit_info6.text')
                
                var={
                    'user':request.user,
                   'amt':depo1.amt1,
                   'coin':depo1.coin1,
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                        'Deposit Request', message, 'Bestfuturetrade',
                        [request.user.email]
                        )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()
                return redirect('pay6')   

            elif depo1.coin1=='ZEC':
                template=loader.get_template('deposit_info7.text')
                
                var={
                    'user':request.user,
                   'amt':depo1.amt1,
                   'coin':depo1.coin1,
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                        'Deposit Request', message, 'Bestfuturetrade',
                        [request.user.email]
                        )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()
           

                return redirect('pay7')        
                   
                

   
   
    return render(request, 'deposit.html',{'user_profile': user_profile})


@login_required(login_url='login')
def invest(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)
    balance= payment1.objects.filter(user=request.user,bol='True').aggregate(total=Sum('amt1'))['total'] or Decimal()
    inv_balance= investment.objects.filter(user=request.user,bol='False').aggregate(total=Sum('amt1'))['total'] or Decimal()
    wtd_balance= withdraw.objects.filter(user=request.user).aggregate(total=Sum('amt'))['total'] or Decimal()
    bonus= percentage.objects.filter(user=request.user).aggregate(total=Sum('amt'))['total'] or Decimal()

    acc= balance + bonus - inv_balance 
    acc_balance = acc - wtd_balance 

   

    if request.method == 'POST':
        if request.POST.get('amt1','mine'):
            plans=investment()
            plans.plans =request.POST.get('mine')
            plans.amt1 =float(request.POST.get('amt1'))
            
            if plans.plans=='starter_plan' and (plans.amt1 <= acc_balance and plans.amt1 <= 5099): 
                messages.success(request,f'${plans.amt1} invested,{plans.plans} package activated')
                plans.user=request.user
                plans.save()
                template=loader.get_template('invest_info1.text')
                
                var={
                'user':request.user,
                'amt':plans.amt1,
                'plans':plans.plans
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                'Investment Notice', message, 'Bestfuturetrade',
                [request.user.email]
                )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()

            elif plans.plans=='starter_plan' and  plans.amt1 > 5099:
                messages.info(request,f' Sorry you cannot invest ${plans.amt1} in starter plan package ')


            elif plans.plans=='bronze_plan' and (plans.amt1 <= acc_balance and plans.amt1 >=5100 and plans.amt1 <=10099):
                messages.success(request,f'${plans.amt1} invested,{plans.plans} package activated')
                plans.user=request.user
                plans.save()
                template=loader.get_template('invest_info1.text')

                var={
                'user':request.user,
                'amt':plans.amt1,
                'plans':plans.plans
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                'Investment Notice', message, 'Bestfuturetrade',
                [request.user.email]
                )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()

            elif  plans.plans=='bronze_plan' and ( plans.amt1 < 5100 or plans.amt1 > 10099):
                messages.info(request,f'Sorry ${plans.amt1} is not bronze plan package') 

            elif plans.plans=='silver_plan' and (plans.amt1 <= acc_balance and plans.amt1 >=10100 and plans.amt1 <=20099):
                messages.success(request,f'${plans.amt1} invested, {plans.plans} package activated ')
                plans.user=request.user
                plans.save()
                template=loader.get_template('invest_info1.text')

                var={
                'user':request.user,
                'amt':plans.amt1,
                'plans':plans.plans
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                'Investment Notice', message, 'Bestfuturetrade',
                [request.user.email]
                )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()


            elif  plans.plans=='silver_plan' and (plans.amt1 < 10100 or plans.amt1 > 20099):
                messages.info(request,f'Sorry ${plans.amt1} is not silver plan package')
                
            elif plans.plans=='golden_plan' and (plans.amt1 <= acc_balance and plans.amt1 >=20100 and plans.amt1 <=30099):
                messages.success(request,f'${plans.amt1} invested,{plans.plans} package activated')
                plans.user=request.user
                plans.save()
                template=loader.get_template('invest_info1.text')

                var={
                'user':request.user,
                'amt':plans.amt1,
                'plans':plans.plans
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                'Investment Notice', message, 'Bestfuturetrade',
                [request.user.email]
                )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()


            elif  plans.plans=='golden_plan' and (plans.amt1 < 20100 or plans.amt1 > 30099):
                messages.info(request,f'Sorry ${plans.amt1} is not golden plan package ')

            elif plans.plans=='starter_mining' and (plans.amt1 <= acc_balance and plans.amt1 >=30100 and plans.amt1 <=40099):
                messages.success(request,f'${plans.amt1} invested,{plans.plans} package activated')
                plans.user=request.user
                plans.save()
                template=loader.get_template('invest_info1.text')

                var={
                'user':request.user,
                'amt':plans.amt1,
                'plans':plans.plans
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                'Investment Notice', message, 'Bestfuturetrade',
                [request.user.email]
                )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()


            elif  plans.plans=='starter_mining' and (plans.amt1 < 30100 or plans.amt1 > 40099):
                messages.info(request,f'Sorry ${plans.amt1} is not starter mining package')

            elif plans.plans=='bronze_mining' and (plans.amt1 <= acc_balance and plans.amt1 >=40100 and plans.amt1 <=50099):
                messages.success(request,f'${plans.amt1} invested,{plans.plans} package activated')
                plans.user=request.user
                plans.save()
                template=loader.get_template('invest_info1.text')

                var={
                'user':request.user,
                'amt':plans.amt1,
                'plans':plans.plans
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                'Investment Notice', message, 'Bestfuturetrade',
                [request.user.email]
                )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()


            elif  plans.plans=='bronze_mining' and (plans.amt1 < 40100 or plans.amt1 > 50099):
                messages.info(request,f'Sorry ${plans.amt1} is not bronze mining package')

            elif plans.plans=='silver_mining' and (plans.amt1 <= acc_balance and plans.amt1 >=50100 and plans.amt1 <=60099):
                messages.success(request,f'${plans.amt1} invested, {plans.plans} package activated')
                plans.user=request.user
                plans.save()
                template=loader.get_template('invest_info1.text')

                var={
                'user':request.user,
                'amt':plans.amt1,
                'plans':plans.plans
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                'Investment Notice', message, 'Bestfuturetrade',
                [request.user.email]
                )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()


            elif  plans.plans=='silver_mining' and (plans.amt1 < 50100 or plans.amt1 > 60099):
                messages.info(request,f'Sorry ${plans.amt1} is not silver mining package')

            elif plans.plans=='gold_mining' and (plans.amt1 <= acc_balance and plans.amt1 >=60100):
                messages.success(request,f'${plans.amt1} invested, {plans.plans} package activated')
                plans.user=request.user
                plans.save()
                template=loader.get_template('invest_info1.text')

                var={
                'user':request.user,
                'amt':plans.amt1,
                'plans':plans.plans
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                'Investment Notice', message, 'Bestfuturetrade',
                [request.user.email]
                )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()


            elif  plans.plans=='gold_mining' and plans.amt1 < 60099:
                messages.info(request,f'Sorry ${plans.amt1} is not gold mining package ')

  
                





            elif plans.amt1 > acc_balance:
                messages.info(request ,f'You do not have sufficient balance to activate {plans.plans} package')
                template=loader.get_template('invest_info2.text')

                var={
                    'user':request.user,
                    'amt':plans.amt1,
                    'plans':plans.plans
                        } 
                message = template.render(var)  
                email =EmailMultiAlternatives(
                'Investment Notice', message, 'Bestfuturetrade',
                [request.user.email]
                )
                email.content_subtype='html'
                email.mixed_subtype='related'   
                email.send()


    context={
        'user_profile':user_profile,
        'acc_balance':acc_balance,
        'inv_balance':inv_balance,
    }

        
   

    return render(request, 'invest.html',context)

@login_required(login_url='login')
def walleth(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)
    
        
    if request.method =='POST':
        if request.POST.get('wallet_ad','coin'):
            wad=wallet()
            wad.wallet_ad=request.POST.get('wallet_ad')
            wad.coin=request.POST.get('coin')
            wad.user =request.user
            wad.save()
            template=loader.get_template('wallet_info.text')
                    
            var={
                'user':wad.user,
            'wad':wad,        } 
            message = template.render(var)  
            email =EmailMultiAlternatives(
                    'Wallet Update', message, 'Bestfuturetrade',
                    [request.user.email]
                    )
            email.content_subtype='html'
            email.mixed_subtype='related'   
            email.send()

    wad = wallet.objects.filter(user=request.user)

    return render(request, 'walleth.html',{'user_profile': user_profile,'wad':wad})



@login_required(login_url='login')
def withdrawal(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)
    wad=wallet.objects.filter(user=request.user)
    
    balance= payment1.objects.filter(user=request.user,bol='True').aggregate(total=Sum('amt1'))['total'] or Decimal()
    inv_balance= investment.objects.filter(user=request.user,bol='False').aggregate(total=Sum('amt1'))['total'] or Decimal()
    wtd_balance= withdraw.objects.filter(user=request.user).aggregate(total=Sum('amt'))['total'] or Decimal()
    bonus= percentage.objects.filter(user=request.user).aggregate(total=Sum('amt'))['total'] or Decimal()


    acc= balance + bonus - inv_balance
    acc_balance = acc - wtd_balance
    try:
        if request.method=='POST':
                if request.POST.get('wallet','amount'):
                    w =withdraw()
                    w.wallet_ad =request.POST.get('wallet')
                    w.amt =int(request.POST.get('amount'))
                    if w.amt <= acc_balance:
                        w.user = request.user
                        w.save()
                        messages.success(request,'withdrawal successful')

                        template=loader.get_template('withdraw_success.text')
                        
                        var={
                        'amt':w.amt,
                        'wallet':w.wallet_ad,
                        'user':w.user,
                        'wad':wad,
                                } 
                        message = template.render(var)  
                        email =EmailMultiAlternatives(
                                'Withdrawal Notice', message, 'Bestfuturetrade',
                                [request.user.email]
                                )
                        email.content_subtype='html'
                        email.mixed_subtype='related'   
                        email.send()
                        return HttpResponseRedirect('withdrawal')

                    elif w.amt > acc_balance:
                        w.user=request.user
                        messages.info(request,'insufficient balance')

                        template=loader.get_template('withdraw_insufficient.text')
                        
                        var={
                        'amt':w.amt,
                        'wallet':w.wallet_ad,
                        'user':w.user,
                        'coin':wad,
                                } 
                        message = template.render(var)  
                        email =EmailMultiAlternatives(
                                'Withdrawal Notice', message, 'Bestfuturetrade',
                                [request.user.email]
                                )
                        email.content_subtype='html'
                        email.mixed_subtype='related'   
                        email.send()
                        return HttpResponseRedirect('withdrawal')
    except:
        
            messages.info(request,f'Dear {request.user} add your wallet address for withdrawal ')
            return redirect('walleth')
                    
           
             
  
    context={
        'user_profile':user_profile,
        'acc_balance':acc_balance,
        'inv_balance':inv_balance,
        'wad':wad,
    }

  
    return render(request,'withdrawal.html',context)    


@login_required(login_url='login')
def kyc(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)
    if request.method=='POST':
        a = request.POST['dob']
        b =request.POST['zip']
        c =request.POST['phone']
        d =request.POST['state']
        e =request.POST['country']
        g =request.POST['pop']
        f =request.POST['doc']
        messages.info(request,f'Dear {request.user} your request for KYC update is has been sent succesfully ')
        return redirect('kyc')

    return render(request,'kyc.html',{'user_profile': user_profile})

@login_required(login_url='login')
def transaction(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)
    
    depo1 =payment1.objects.filter(user=request.user)
    
    
    context = {
        'user_profile':user_profile,
        'depo1':depo1,

    }
   
    return render(request, 'transaction.html',context)    

def contact(request):   
    return render(request, 'contact.html')

def send_mail(request):
    if request.method=='POST':
        name = request.POST['name']
        email =request.POST['email']
        msg =request.POST['message']
        subject =request.POST['subject']
        query =Contact(name=name,email=email,message=msg,subject=subject)
        query.save()
    temp=loader.get_template('contact_form.text')
    context={
        'name':name,
        'email':email,
        'msg':msg,
        'subject':subject,
    } 
    message =temp.render(context)  
    em =EmailMultiAlternatives(
      'Bestfuturecoin', message, 'Response from bestfuturecoin',
      ['bestfuturecoin@gmail.com',email]
    )
    em.content_subtype='html'
    em.mixed_subtype='related'
    em.send()
    messages.success(request,'Thanks For Reaching Us! We will get back to you soon.....')
    return HttpResponseRedirect('contact')

@login_required(login_url='login')
def prof(request):

    user_profile = profile.objects.get(user=request.user)
  
    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            fullname = request.POST['fullname']
            job=request.POST['job']
            address=request.POST['address']
            mobile=request.POST['mobile']
            location = request.POST['location']


            user_profile.profileimg = image
            user_profile.fullname = fullname
            user_profile.location = location
            user_profile.job = job
            user_profile.address = address
            user_profile.mobile = mobile
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            fullname = request.POST['fullname']
            job=request.POST['job']
            address=request.POST['address']
            mobile=request.POST['mobile']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.fullname = fullname
            user_profile.location = location
            user_profile.job = job
            user_profile.address = address
            user_profile.mobile = mobile

            user_profile.save()
    return render(request,'prof.html', {'user_profile':user_profile})    



def plan(request):
    return render(request,'plan.html')    


def policy(request):
    return render(request, 'policy.html')

@login_required(login_url='login')
def pay1(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)

    depo1 = payment1.objects.last()

    context = {
        'user_profile':user_profile,
        'depo1':depo1,

    }

     
    return render(request,'pay1.html',context)


@login_required(login_url='login')
def pay2(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)

    depo1= payment1.objects.last()

    context = {
        'user_profile':user_profile,
        'depo1':depo1,

    }

     
    return render(request,'pay2.html',context)


@login_required(login_url='login')
def pay3(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)

    depo1 = payment1.objects.last()

    context = {
        'user_profile':user_profile,
        'depo1':depo1,

    }
 
     
    return render(request,'pay3.html',context)



@login_required(login_url='login')
def pay4(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)

    depo1 = payment1.objects.last()

    context = {
        'user_profile':user_profile,
        'depo1':depo1,

    }

     
    return render(request,'pay4.html',context)

@login_required(login_url='login')
def pay5(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)

    depo1 = payment1.objects.last()

    context = {
        'user_profile':user_profile,
        'depo1':depo1,

    }

     
    return render(request,'pay5.html',context)

@login_required(login_url='login')
def pay6(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)

    depo1 = payment1.objects.last()

    context = {
        'user_profile':user_profile,
        'depo1':depo1,

    }

     
    return render(request,'pay6.html',context)

@login_required(login_url='login')
def pay7(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)

    depo1 = payment1.objects.last()

    context = {
        'user_profile':user_profile,
        'depo1':depo1,

    }

     
    return render(request,'pay7.html',context)

@login_required(login_url='login')
def i_history(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)
    
    depo1 =investment.objects.filter(user=request.user)
    
    
    context = {
        'user_profile':user_profile,
        'depo1':depo1,

    }

    return render(request,'i_history.html',context)


@login_required(login_url='login')
def w_history(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = profile.objects.get(user=user_object)
    
    depo1 =withdraw.objects.filter(user=request.user)
    
    
    context = {
        'user_profile':user_profile,
        'depo1':depo1,

    }

    return render(request,'w_history.html',context)




