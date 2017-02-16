from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
# Create your views here.

from .forms import ManageStudentForm

def index(request):
	template_name='index.html'
	return render(request, template_name, {})


class ManageStudentView(CreateView):
	form_class = ManageStudentForm
	initial = {'key': 'value'}
	template_name = 'student-add.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		print('not save')
		if form.is_valid():
			print('save')
			form.save()
			return HttpResponseRedirect('/success/')
		return render(request, self.template_name, {'form': form})
