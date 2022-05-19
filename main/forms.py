from django import forms

# create user sign up form 
class UserForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    tel = forms.CharField(max_length=200)
    id_number = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    confirm_password = forms.CharField(max_length=200)
    

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
