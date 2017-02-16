from django import forms

from .models import ManageStudent

class ManageStudentForm(forms.ModelForm):
	class Meta:
		model = ManageStudent
		fields = '__all__'