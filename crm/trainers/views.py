from django.shortcuts import render,redirect


from trainers.models import Trainers

from .forms import TrainerRegisterForm

from django.views.generic import View

from django.db.models import Q

from django.utils.decorators import method_decorator

from authentication.permissions import permission_roles

from django.db import transaction

from .utility import get_trainer_id,get_password

from authentication.models import Profile

# Create your views here.

# @method_decorator(login_required(login_url="login"),name="dispatch")
@method_decorator(permission_roles(roles=["Admin","Sales"]),name="dispatch")
class TrainersListView(View):
     
     def get(self,request,args,*kwargs):

          query = request.GET.get("query")

          role = request.user.role


          if role in ["Trainer"]:

               trainers = Trainers.objects.filter(active_status=True,trainer__profile = request.user)

               if query:

                    trainers = Trainers.objects.filter(Q(active_status = True)&
                                                       Q(trainer__profile=request.user)&
                                                       (Q(first_name__icontains=query)|
                                                        Q(last_name__icontains=query)|
                                                        Q(house_name__icontains=query)|
                                                        Q(district__icontains=query)|
                                                        Q(contact_num__icontains=query)|
                                                        Q(adm_number__icontains=query)|
                                                        Q(email__exact=query)|
                                                        Q(pincode__icontains=query)|
                                                        Q(course_name_icontains=query)|
                                                        Q(trainer_first_name_icontains=query)|
                                                        Q(trainer_last_name_icontains=query)|
                                                        Q(batch_name_icontains=query)
                                                        )
                                                        )
                    
          elif role in ["Academic Counsellor"]:

               trainers = Trainers.objects.filter(active_status = True,batch_academic_counsellor_profile = request.user)

               if query:

                    trainers = Trainers.objects.filter(Q(active_status = True)&
                                                       Q(batch_academic_counsellor_profile =request.user)&
                                                       (Q(first_name__icontains=query)|
                                                        Q(last_name__icontains=query)|
                                                        Q(house_name__icontains=query)|
                                                        Q(district__icontains=query)|
                                                        Q(contact_num__icontains=query)|
                                                        Q(adm_number__icontains=query)|
                                                        Q(email__exact=query)|
                                                        Q(pincode__icontains=query)|
                                                        Q(course_name_icontains=query)|
                                                        Q(trainer_first_name_icontains=query)|
                                                        Q(trainer_last_name_icontains=query)|
                                                        Q(batch_name_icontains=query)
                                                        )
                                                        )
               
          else:

               trainers = Trainers.objects.filter(active_status = True)  

               if query:

                    trainers = Trainers.objects.filter(Q(active_status = True)&(Q(first_name_icontains=query)|Q(last_nameicontains=query)|Q(house_nameicontains=query)|Q(districticontains=query)|Q(contact_numicontains=query)|Q(adm_numbericontains=query)|Q(emailexact=query)|Q(pincodeicontains=query)|Q(coursenameicontains=query)|Q(trainerfirst_nameicontains=query)|Q(trainerlast_nameicontains=query)|Q(batchname_icontains=query)))


          print(query)

          # students  = Students.objects.all()

          

          print(trainers)

          data = {"trainers":trainers,"query":query}

          # for student in students:

          #      print(student.first_name)
          
          return render(request,"trainers/trainer-list.html",context=data)
     


@method_decorator(permission_roles(roles=["Admin","Sales"]),name="dispatch")    
class RegisterView(View):
     
     def get(self,request,args,*kwargs):

          form = TrainerRegisterForm()

          # data = {"districts":DistrictChoices,"batches":BatchChoices,"trainers":TrainerChoices,"courses":CourseChoices,"form":form}

          data = {"form":form}


          
          return render(request,"trainers/register.html",context=data)
     

     def post(self,request,args,*kwargs):

          form = TrainerRegisterForm(request.POST,request.FILES)

          if form.is_valid():

               with transaction.atomic():

                    trainer =  form.save(commit=False)

                    trainer.trainer_id = get_trainer_id()

                    # student.join_date = "2025-02-05"

                    username = trainer.email

                    password = get_password()

                    print(password)

                    profile = Profile.objects.create_user(username=username,password=password,role="Trainer")

                    trainer.profile = profile


                    trainer.save()

               return redirect("trainers-list")
          
          else:

               data = {"form":form}

               return render(request,"trainers/register.html",context=data)