from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUsuario


class CustomUsuarioCreationForm(UserCreationForm):

    class Meta:
        model = CustomUsuario  # qual é a classe modelo?
        fields = ('first_name', 'last_name', 'fone')  # Quais são os campos que esse objeto precisa ter?
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')
