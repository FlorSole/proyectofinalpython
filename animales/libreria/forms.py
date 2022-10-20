from django import forms






class usuarioform(forms.Form):

    nombre = forms.CharField(max_length=60)
    edad = forms.IntegerField()
    email= forms.EmailInput()
    
    


class animalform(forms.Form):

    nombre = forms.CharField(max_length=60)
    raza = forms.CharField(max_length=60)
    sexo = forms.CharField(max_length=60)
    edad = forms.IntegerField()
    foto= forms.ImageField()