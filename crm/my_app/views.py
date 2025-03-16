from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from django.views.generic import View

from.models import Students

from.models import DistrictChoices

from.models import CourseChoices

from.models import BatchChoices

from.models import TrainerChoices

from.forms import StudentRegistartionForm

from django.db.models import Q

from .utility import get_admission_number,get_password,send_email

from authentication.models import Profile

from django.db import transaction

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import permission_roles

#threading

import threading

import datetime

from payments.models import Payment

# class HomeView(View):

#     def get(self,request,*args,**kwargs):

#         return render(request,'my_app/home.html')

class GetStudentObject:

    def get_student(self,request,uuid):

         try:

           student= Students.objects.get(uuid=uuid)

           return student
         
         except:

            return render(request,'errorpages/error-404.html')

# @method_decorator(login_required(login_url='login'),name='dispatch')

@method_decorator(permission_roles(roles=['admin','sales']),name='dispatch')

class DashboardView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'my_app/dashboard.html')
    
@method_decorator(permission_roles(roles=['admin','sales','trainer','academic councellor']),name='dispatch')

class StudentsListView(View):

    def get(self,request,*args,**kwargs):

        query = request.GET.get('query')

        role = request.user.role

        if role in ['trainer']:

            students= Students.objects.filter(active_status=True,trainer__profile=request.user)

            
        if query:

            students= Students.objects.filter(Q(active_status=True)&Q(trainer__profile=request.user)(Q(first_name__icontains = query)|Q(last_name__icontains=query))|
                                              Q(email__icontains=query)|Q(contact__icontains=query)|Q(house_name__icontains=query)|Q(post_office__icontains=query)|
                                              Q(adm_number__icontains=query)|Q(course__code__icontains=query)|Q(batch__name__icontains=query)|
                                              Q(trainer__first_name__icontains=query)|Q(trainer__last_name__icontains=query))


        else:

            students=Students.objects.filter(active_status=True)


            if query:

                students= Students.objects.filter(Q(active_status=True)&(Q(first_name__icontains = query)|Q(last_name__icontains=query))|
                                                Q(email__icontains=query)|Q(contact_num__icontains=query)|Q(house_name__icontains=query)|Q(post_office__icontains=query)|
                                                Q(adm_number__icontains=query)|Q(course__code__icontains=query)|Q(batch__name__icontains=query)|
                                                Q(trainer__first_name__icontains=query)|Q(trainer__last_name__icontains=query))

        # students= Students.objects.all()

        # students=Students.objects.filter(active_status=True)

        print(students)

        # for student in students:

        #     print(student.first_name)

        #     print(student.last_name)

        data= {'students':students,'query':query}

        return render(request,'my_app/students.html',context=data)  
    
@method_decorator(permission_roles(roles=['admin','sales',]),name='dispatch')

class StudentRegisterView(View):
     
     def get(self,request,*args,**kwargs):

        form= StudentRegistartionForm()
        

        # data = {'districts':DistrictChoices,'courses':CourseChoices,'batches': BatchChoices,'trainers' :TrainerChoices,'form':form }
        data={'form':form}

        return render(request,'my_app/register.html',context=data)

     def post(self,request,*args,**kwargs):

        form = StudentRegistartionForm(request.POST,request.FILES)

       

        # form.cleaned_data.get('first_name')

        # for error in form.errors:

        #     print(error)


        if form.is_valid():

            with transaction.atomic():

            
                student= form.save(commit=False)

                student.adm_number= get_admission_number()

            # student.join_date='2025-02-05'

                username = student.email

                password = get_password()

                print(password)

                profile = Profile.objects.create_user(username=username,password=password,role='student')

                student.profile = profile

                student.save()

                # payment section

                fee = student.course.offer_fee if student.course.offer_fee else student.course.fee

                Payment.objects.create(student=student,amount=fee )

                #sending login credentials to student through whatsapp

                subject ='login credentials'

                # sender = settings.EMAIL_HOST_USER

                recepients = [student.email]

                template ='email/login-credentials.html'

                join_date = student.join_date

                date_after_10_days = join_date + datetime.timedelta(days=10)

                print(date_after_10_days)

                context = {'name':f"{student.first_name} {student.last_name}",'username': username, 'password':password,'date_after_10_days':date_after_10_days}

                send_email(subject,recepients,template,context)

                # thread = threading.Thread(target=send_email,args=(subject,recepients,template,context))

                # thread.start()


            return redirect('students-list')
        
        else:

            data={'form':form}

            return render(request,'my_app/register.html',context=data)
        
@method_decorator(permission_roles(roles=['admin','sales','trainer','academic councellor']),name='dispatch')
       
class StudentDetailView(View):

    def get(self,request,*args,**kwargs):

        uuid= kwargs.get('uuid')

        # student=get_object_or_404(student,pk=pk)

        student= GetStudentObject().get_student(request,uuid)

        # try:
            
        #     student=Students.objects.get(pk=pk)

        #     print(student)

        # except:

        #     return redirect('error-404')

        data={'student':student}

        return render(request,'my_app/student-detail.html',context=data)
    
# class Error404View(View):

#     def get(self,request,*args,**kwargs):

#         return render(request,'my_app/error-404.html').

@method_decorator(permission_roles(roles=['admin','sales']),name='dispatch')
    
class DeleteView(View):

    def get(self,request,*args,**kwargs):

        uuid= kwargs.get('uuid')

        # try:

        #    student= Students.objects.get(pk=pk)

        # except:

        #     return redirect('error-404')
        
        student= GetStudentObject().get_student(request,uuid)
        
        # student.delete()
        student.active_status=False

        student.save()

        return redirect('students-list')
    
@method_decorator(permission_roles(roles=['admin','sales']),name='dispatch')

class StudentUpdateView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        student = GetStudentObject().get_student(request,uuid)

        form = StudentRegistartionForm(instance=student)

        data= {'form':form}
 
        return render(request,'my_app/student-update.html',context=data)
    
    def post(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        student= GetStudentObject().get_student(request,uuid)

        form = StudentRegistartionForm(request.POST,request.FILES,instance=student)

        if form.is_valid():

            form.save()
            
            #sending login credentials to student through whatsapp

            return redirect('students-list')
        
        else:
            
            data ={'form':form}
            
            return render(request,'my_app/student-update.html',context=data)