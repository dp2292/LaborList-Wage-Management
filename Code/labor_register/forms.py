from django import forms
from labor_register.models import Labor
from labor_register.models import Supervisor

class LaborForm(forms.ModelForm):
    class Meta:
        model = Labor
        fields = '__all__'
        labels = {
            'Supervisor_ID' : 'Supervisor ID',
            'Rating' : 'Rating',
            'City_ID':'City ID',
            'Full Name':'Full Name','Work_type':'Work Type'
        }
    def __init__(self,*args, **kwargs)  :
        super(LaborForm,self).__init__(*args, **kwargs)
        self.fields['Supervisor_ID'].empty_label="Select"
        self.fields['City_ID'].empty_label= "Select"
        self.fields['Rating'].required=False

class SupervisorForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = '__all__'

    def __init__(self,*args, **kwargs)  :
        super(SupervisorForm,self).__init__(*args, **kwargs)
        self.fields['Rating'].required=False

