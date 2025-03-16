#cron to sent remainder email about payment

from payments.models import Payment,Transactions

from django.utils import timezone

import threading

from my_app.utility import send_email

from my_app.models import Students

from apscheduler.schedulers.background import BackgroundScheduler

def remainder_email():

    current_date = timezone.now().date()

    five_days_before_date = current_date-timezone.timedelta(days=5)

    pending_payments = Payment.objects.filter(status='pending',student__join_date__lte = five_days_before_date)

    if pending_payments.exists():

        for payment in pending_payments:
            
            subject ='payment remainder'

            recepients = [payment.student.email]

            template ='email/payment-remainder.html'

            context = {'name':f"{payment.student.first_name} {payment.student.last_name}"}

                # send_email(subject,recepients,template,context)

            thread = threading.Thread(target=send_email,args=(subject,recepients,template,context))

            thread.start()

#apscheduler

def scheduler_start():

    scheduler = BackgroundScheduler()

    scheduler.add_job(remainder_email,'cron',hour=10,minute=0)

    scheduler.start()



