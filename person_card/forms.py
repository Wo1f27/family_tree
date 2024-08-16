from django import forms

from .models import Person, Email, PhoneNumber


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'patronymic', 'last_name', 'date_of_birth', 'date_of_death', 'profile_avatar', 'notes']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date'
            }),
            'date_of_death': forms.DateInput(attrs={
                'type': 'date'
            })
        }
        labels = {
            'first_name': 'Имя',
            'patronymic': 'Отчество',
            'last_name': 'Фамилия',
            'date_of_birth': 'Дата рождения',
            'date_of_death': 'Дата смерти',
            'profile_avatar': 'Аватар',
            'notes': 'Заметки'
        }


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']
        labels = {
            'email': 'Электронная почта'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = False


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['phone_number']
        labels = {
            'phone_number': 'Номер телефона'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].required = False


class CombinedPersonCardForm(forms.Form):

    def __init__(self, data=None, files=None, *args, **kwargs):
        self.person_form = PersonForm(data=data, files=files)
        self.email_form = EmailForm(data=data, files=files)
        self.phone_number_form = PhoneNumberForm(data=data, files=files)
        super().__init__(*args, **kwargs)

    def is_valid(self):
        return (self.person_form.is_valid() and
                self.email_form.is_valid() and
                self.phone_number_form.is_valid())

    def save(self):
        person = self.person_form.save()
        if self.email_form.cleaned_data.get('email'):
            email = self.email_form.save(commit=False)
            email.person = person
            email.save()
        if self.phone_number_form.cleaned_data.get('phone_number'):
            phone_number = self.phone_number_form.save(commit=False)
            phone_number.person = person
            phone_number.save()


