from django import forms

from . models import Trainers, DistrictChoices

from batches.models import Batches

from courses.models import  Courses

from trainers.models import Trainers

class TrainersRegisterForm(forms.ModelForm):

    class Meta:

        model = Trainers 

        # fields = ['first_name','last_name','photo','email','contact_num','house_name',
        #       'post_office','district','pincode','course','batch','batch_date','trainer_name']
        
        # if all fields in the models used

        # fields = '_all_'

        exclude = ['employee_id','uuid','active_status','profile']

        widgets = {'first_name' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                         'placeholder' : 'Enter first name', 
                                                         'required' :'required'}),
                    'last_name' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter last name', 
                                                                    'required' :'required'}),
                    'photo' : forms.FileInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    }),
                    'email' : forms.EmailInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter email', 
                                                                    'required' :'required'}),
                    'contact' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter contact number', 
                                                                    'required' :'required'}),
                    'house_name' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter house name', 
                                                                    'required' :'required'}),
                    'post_office' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter post office', 
                                                                    'required' :'required'}),
                    'pincode' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter pincode', 
                                                                    'required' :'required'}),
                    'qualification' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter qualification', 
                                                                    'required' :'required'}),
                    'stream' : forms.TextInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                    'placeholder' : 'Enter stream', 
                                                                    'required' :'required'}),
                    'id_proof' : forms.FileInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                                   'required' :'required'}),

                    # 'batch_date' : forms.DateInput(attrs={'class' : 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                    #                                                 'placeholder' : 'Enter batch date', 
                    #                                                 'type':'date',
                    #                                                 'required' :'required'}),
                                                                    }
        
    district = forms.ChoiceField(choices=DistrictChoices.choices,widget=forms.Select(attrs={
                                                                                    'class' : 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                    'required' : 'required'}))
    
    course = forms.ModelChoiceField(queryset=Courses.objects.all(),widget=forms.Select(attrs={
                                                                                         'class' : 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                         'required' : 'required'}))

    # batch = forms.ChoiceField(choices=BatchChoices.choices,widget=forms.Select(attrs={
    #                                                                                 'class' : 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #                                                                                 'required' : 'required'}))

    # batch = forms.ModelChoiceField(queryset=Batches.objects.all(),widget=forms.Select(attrs={
    #                                                                                      'class' : 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #                                                                                      'required' : 'required'}))

    # trainer_name = forms.ChoiceField(choices=TrainerChoices.choices,widget=forms.Select(attrs={
    #                                                                                 'class' : 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #                                                                                 'required' : 'required'}))

    # trainer = forms.ModelChoiceField(queryset=Trainers.objects.all(),widget=forms.Select(attrs={
    #                                                                                      'class' : 'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
    #                                                                                      'required' : 'required'}))
    
    def clean(self):

        cleaned_data = super().clean()

        pincode = cleaned_data.get('pincode')

        email = cleaned_data.get('email')

        # if Trainers.objects.filter(profile__username = email).exists():

        #     self.add_error('email','This email is already registered. Please change email')

        if len(pincode) < 6:

            self.add_error('pincode','pincode must be 6 digits')

        return cleaned_data
    
    def _init_(self,args,*kwargs):

        super(TrainersRegisterForm,self)._init_(args,*kwargs)

        if not self.instance:

            self.fields.get('photo').widget.attrs['required'] = 'required'