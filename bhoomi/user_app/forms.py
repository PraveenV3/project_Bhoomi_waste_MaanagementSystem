from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    contact_number = forms.CharField(max_length=15, required=True)
    district = forms.ChoiceField(choices=UserProfile.DISTRICT_CHOICES, required=True)
    province = forms.ChoiceField(choices=UserProfile.PROVINCE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'contact_number', 'district', 'province')

    def save(self, commit=True):
        user = super().save(commit)
        contact_number = self.cleaned_data['contact_number']
        district = self.cleaned_data['district']
        province = self.cleaned_data['province']
        # Create or update user profile
        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.contact_number = contact_number
        profile.district = district
        profile.province = province
        if commit:
            profile.save()
        return user

class ProfileUpdateForm(forms.ModelForm):
    contact_number = forms.CharField(max_length=15, required=True)
    district = forms.ChoiceField(choices=UserProfile.DISTRICT_CHOICES, required=True)
    province = forms.ChoiceField(choices=UserProfile.PROVINCE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'contact_number', 'district', 'province')

    def __init__(self, *args, **kwargs):
        user = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if user:
            try:
                profile = user.userprofile
                self.fields['contact_number'].initial = profile.contact_number
                self.fields['district'].initial = profile.district
                self.fields['province'].initial = profile.province
            except UserProfile.DoesNotExist:
                pass
        # user_id is not editable, so not included in form fields

    def save(self, commit=True):
        user = super().save(commit)
        contact_number = self.cleaned_data['contact_number']
        district = self.cleaned_data['district']
        province = self.cleaned_data['province']
        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.contact_number = contact_number
        profile.district = district
        profile.province = province
        if commit:
            profile.save()
        return user
