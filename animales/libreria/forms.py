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





class registroUzu(forms.Form):


    usuario= forms.CharField(max_length=60)
    email= forms.EmailInput()
    contraseña= forms.PasswordInput()
    repetircontraseña= forms.PasswordInput()

