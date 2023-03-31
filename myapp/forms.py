from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(
        label="titulo de tarea", 
        max_length=200,
    )
    description = forms.CharField( 
        label = "descripcion de la tarea",  
        widget=forms.Textarea
    )
class SignUp(forms.Form):
    name =  forms.CharField(
        label="name", 
        max_length=50,
    )
    lastname =  forms.CharField(
        label="lastname", 
        max_length=50,
    )
    email = forms.CharField(
        label="email", 
        max_length=80,
    )

    password = forms.CharField(widget=forms.PasswordInput())
    
    password2 = forms.CharField(widget=forms.PasswordInput())