from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#funcion para rellenar los campos establecidos en la BD auth_user por django
class RegistroForm(UserCreationForm):
	class Meta:
		model=User
		fields =['username','first_name','last_name','email',
		#fields="__all__"


		]
		labels={'username':'Nombre de usuario',
		'first_name':'Tipo de Documento',
		'last_name':'Apellidos',
		'email':'correo',
				}
			
	
