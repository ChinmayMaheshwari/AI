from django.shortcuts import render
from django.views.generic import FormView,View
from .forms import FolderUpload
from django.http import HttpResponse,FileResponse
# Create your views here.

from .face_rec import classify
import os
import shutil

class IndexView(FormView):
	form_class=FolderUpload
	template_name='index.html'
	success_url='/result/'

	def post(self,request,*args,**kwargs):
		def handle_uploaded_file(f,i):
			with open('images/'+str(i),'wb+') as destination:
				for chunk in f.chunks():
					destination.write(chunk)
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		file=request.FILES.getlist('file')
		#print(request.FILES,kwargs)
		if form.is_valid():
			base=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
			if os.path.exists('images')==True:
				shutil.rmtree(base+'/images')
			if os.path.exists('Allimages')==True:
				shutil.rmtree(base+'/Allimages')
			if os.path.exists('People')==True:
				shutil.rmtree(base+'/People')


			os.mkdir('images')
			os.mkdir('People')
			os.mkdir('Allimages')
			for f in file:
				#print(f._get_name())
				handle_uploaded_file(f,f._get_name())
			classify()
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
		


class Results(View):
	response_template='result.html'

	def get(self,request,*args,**kwargs):
		base=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		files=os.path.join(base,'People')
		shutil.make_archive('results/photos', 'zip', files)
		result_path=os.path.join(base,'results')
		zip_file = open(result_path+'/photos.zip', 'rb')


		return FileResponse(zip_file)




