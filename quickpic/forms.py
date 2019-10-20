from django import forms

class FolderUpload(forms.Form):
	file=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))