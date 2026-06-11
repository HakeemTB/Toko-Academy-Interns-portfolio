# from django import forms

# class  ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'placeholder': 'Your Full Name'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email Address'}))
#     phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Your Phone Number (Optional)'}))
#     subject = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder': 'Subject (Optional)'}))
#     messages  = forms.Textarea( widget=forms.Textarea(attrs={'placeholder': 'Your Message'}))



#     # def clean_email(self):
#     #     email = self.cleaned_data.get('email')
#     #     if not email.endswith('@example.com'):
#     #         raise forms.ValidationError("Please use an email address from the example.com domain.")
#     #     return email



# base/forms.py
from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Alex Alexus',
            'class': 'w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3.5 text-sm text-white placeholder-gray-600 focus:outline-none focus:border-blue-500/50 focus:ring-1 focus:ring-blue-500/30 transition-all',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'alex@company.com',
            'class': 'w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3.5 text-sm text-white placeholder-gray-600 focus:outline-none focus:border-purple-500/50 focus:ring-1 focus:ring-purple-500/30 transition-all',
        })
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '+1 (234) 90-2834',
            'class': 'w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3.5 text-sm text-white placeholder-gray-600 focus:outline-none focus:border-blue-500/50 focus:ring-1 focus:ring-blue-500/30 transition-all',
        })
    )
    subject = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Partnership / Project Inquiry',
            'class': 'w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3.5 text-sm text-white placeholder-gray-600 focus:outline-none focus:border-purple-500/50 focus:ring-1 focus:ring-purple-500/30 transition-all',
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 6,
            'placeholder': 'Tell us how we can collaborate/contribute...',
            'class': 'w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3.5 text-sm text-white placeholder-gray-600 focus:outline-none focus:border-blue-500/50 focus:ring-1 focus:ring-blue-500/30 transition-all resize-none',
        })
    )

    def clean_full_name(self):
        name = self.cleaned_data.get('full_name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError('Please enter your full name.')
        return name

    def clean_message(self):
        message = self.cleaned_data.get('message', '').strip()
        if len(message) < 10:
            raise forms.ValidationError('Message is too short. Please give us a bit more detail.')
        return message

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        if phone:
            digits = ''.join(filter(str.isdigit, phone))
            if len(digits) < 7:
                raise forms.ValidationError('Please enter a valid phone number.')
        return phone