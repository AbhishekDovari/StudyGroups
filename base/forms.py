from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User
# from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.username.lower()
        if commit:
            user.save()
        return user

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']