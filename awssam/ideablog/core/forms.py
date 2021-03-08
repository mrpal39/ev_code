from django import forms

from .models import  Products






class productForm(forms.ModelForm):
	class Meta:
		model=Products
		fields=['title','description','price']