from django import forms
from .validators import validate_meaningful_response, validate_min_length, validate_no_excessive_punctuation, validate_no_patterns, validate_not_trivial, validate_no_repetitive_characters  
from .models import ValueModel, SignupModel, NoValueModel
from django.contrib.auth import authenticate
class NoValueForm(forms.ModelForm):
    signup_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)  # Add a hidden field for signup_id
    
    class Meta:
        model = NoValueModel
        fields = ['interests', 'form_value', 'format_importance', 'catchphrase']
        widgets = {
            'interests': forms.TextInput(attrs={'class': 'form-control'}),
            'form_value': forms.TextInput(attrs={'class': 'form-control'}),
            'format_importance': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'catchphrase': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['interests'].validators.append(validate_meaningful_response)
        self.fields['interests'].validators.append(validate_no_excessive_punctuation)
        self.fields['interests'].validators.append(validate_min_length)
        self.fields['interests'].validators.append(validate_no_patterns)
        self.fields['interests'].validators.append(validate_not_trivial)
        self.fields['interests'].validators.append(validate_no_repetitive_characters)
        
        
        self.fields['format_importance'].validators.append(validate_meaningful_response)
        self.fields['format_importance'].validators.append(validate_no_excessive_punctuation)
        self.fields['format_importance'].validators.append(validate_min_length)
        self.fields['format_importance'].validators.append(validate_no_patterns)
        self.fields['format_importance'].validators.append(validate_not_trivial)
        self.fields['format_importance'].validators.append(validate_no_repetitive_characters)
        

        self.fields['catchphrase'].validators.append(validate_meaningful_response)
        self.fields['catchphrase'].validators.append(validate_no_excessive_punctuation)
        self.fields['catchphrase'].validators.append(validate_min_length)
        self.fields['catchphrase'].validators.append(validate_no_patterns)
        self.fields['catchphrase'].validators.append(validate_not_trivial)
        self.fields['catchphrase'].validators.append(validate_no_repetitive_characters)
       



class LoginForm(forms.Form) :
    
    username = forms.CharField(max_length=26, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # password = forms.CharField(max_length=200, widget = forms.PasswordInput(), label="Enter your Prolific ID")

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        # password = cleaned_data.get('password')
        
        user = authenticate(username=username)
        print("user", user)
        # Confirms that the two password fields match
        if not user:
            raise forms.ValidationError("Invalid Prolific ID")
        # We must return the cleaned data we got from our parent.
        return cleaned_data


class ValueForm(forms.ModelForm):
    signup_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)  # Add a hidden field for signup_id
    
    class Meta:
        model = ValueModel
        fields = ['interests', 'form_value', 'value_importance', 'catchphrase']
        widgets = {
            'interests': forms.TextInput(attrs={'class': 'form-control'}),
            'form_value': forms.TextInput(attrs={'class': 'form-control'}),
            'value_importance': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'catchphrase': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['interests'].validators.append(validate_meaningful_response)
        self.fields['interests'].validators.append(validate_no_excessive_punctuation)
        self.fields['interests'].validators.append(validate_min_length)
        self.fields['interests'].validators.append(validate_no_patterns)
        self.fields['interests'].validators.append(validate_not_trivial)
        self.fields['interests'].validators.append(validate_no_repetitive_characters)
      
        self.fields['value_importance'].validators.append(validate_meaningful_response)
        self.fields['value_importance'].validators.append(validate_no_excessive_punctuation)
        self.fields['value_importance'].validators.append(validate_min_length)
        self.fields['value_importance'].validators.append(validate_no_patterns)
        self.fields['value_importance'].validators.append(validate_not_trivial)
        self.fields['value_importance'].validators.append(validate_no_repetitive_characters)
        

        self.fields['catchphrase'].validators.append(validate_meaningful_response)
        self.fields['catchphrase'].validators.append(validate_no_excessive_punctuation)
        self.fields['catchphrase'].validators.append(validate_min_length)
        self.fields['catchphrase'].validators.append(validate_no_patterns)
        self.fields['catchphrase'].validators.append(validate_not_trivial)
        self.fields['catchphrase'].validators.append(validate_no_repetitive_characters)
        
      
class SignupForm(forms.ModelForm):
    class Meta:
        model = SignupModel
        fields = ['form_username', 'form_password', 'form_confirm_password']

""" 
class WordleEntryForm(forms.ModelForm):
    signup_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)  # Add a hidden field for signup_id
    
    class Meta:
        model = WordleEntry
        fields = ['signup_id', 'letter_1', 'letter_2', 'letter_3', 'letter_4', 'letter_5', 'image_data']
        
        widgets = {
            'signup_id': forms.HiddenInput(),  # Ensure that the signup_id field is hidden in the form
            'letter_1': forms.TextInput(attrs={'class': 'form-control'}),
            'letter_2': forms.TextInput(attrs={'class': 'form-control'}),
            'letter_3': forms.TextInput(attrs={'class': 'form-control'}),
            'letter_4': forms.TextInput(attrs={'class': 'form-control'}),
            'letter_5': forms.TextInput(attrs={'class': 'form-control'}),
            'image_data': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        } """