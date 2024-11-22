from django import forms
from .models import Student,Registration
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError 

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            "name": _("Student Name"),
        }
        help_texts = {
            "name": _("Some useful help text."),
        }
        error_messages = {
            "name": {
                "max_length": _("This writer's name is too long."),
            },
        }


def start_with_d(value):
    if value[0] != 'd':
        raise forms.ValidationError("username should start with d")


# class UserRegistration(forms.Form):
#     # error_css_class = "error"
#     # required_css_class = "required"
#     # name = forms.CharField(label_suffix=" :", error_messages={"required":"Enter your name"})
#     # email = forms.EmailField()
#     # address = forms.CharField()
#     # userName = forms.CharField(validators=[start_with_d])
#     # password = forms.CharField(widget= forms.HiddenInput(), required=False)


#     # def clean_name(self):
#     #         name = self.cleaned_data['name']
#     #         print(name, "NAME")
#     #         if len(name) < 5:
#     #             raise forms.ValidationError("Enter more than 5 words")


#     def clean(self):
#         cleaned_data = super().clean()

#         name = cleaned_data.get("name")
#         email = cleaned_data.get("email")
#         address = cleaned_data.get("address")

#         if(name and len(name) < 5):
#             raise forms.ValidationError("name must be 5 character long")
#         if(address and len(address) < 8):
#             raise forms.ValidationError("Invalid Address")

#         return cleaned_data


class UserRegistration(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"

        widgets={"password":forms.PasswordInput,"name":forms.TextInput(attrs={'class':"my-field"})}

    def clean_userName(self):
        userName = self.cleaned_data.get('userName')
        if(userName[0] != "s"):
            raise forms.ValidationError("Should start with 'S'")
        return userName
 



#  Django Authentication forms

class SignupForm(UserCreationForm):
    # class Meta:
    #     model = User
    #     fields = ["username", "first_name", "last_name"]
    username = forms.CharField(label='username', min_length=5, max_length=150)  
    email = forms.EmailField(label='email')  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
  
    # def username_clean(self):  
    #     username = self.cleaned_data['username'].lower()  
    #     new = User.objects.filter(username = username)  
    #     if new.count():  
    #         raise ValidationError("User Already Exist")  
    #     return username  
  
    # def email_clean(self):  
    #     email = self.cleaned_data['email'].lower()  
    #     new = User.objects.filter(email=email)  
    #     if new.count():  
    #         raise ValidationError(" Email Already Exist")  
    #     return email  
  
    # def clean_password2(self):  
    #     password1 = self.cleaned_data['password1']  
    #     password2 = self.cleaned_data['password2']  
  
    #     if password1 and password2 and password1 != password2:  
    #         raise ValidationError("Password don't match")  
    #     return password2  
  
    # def save(self, commit = True):  
    #     user = User.objects.create_user(  
    #         self.cleaned_data['username'],  
    #         self.cleaned_data['email'],  
    #         self.cleaned_data['password1']  
    #     )  
    #     return user  