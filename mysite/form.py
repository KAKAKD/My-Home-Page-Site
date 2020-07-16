from django import forms
from django.conf import settings 
from django.core.mail import BadHeaderError, send_mail , EmailMessage
from django.http import HttpResponse 
from django.shortcuts import redirect


class ContactForm(forms.Form):
    name = forms.CharField(
        label='名前',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-name', 
            'placeholder':"Name",
        }),
    )

    email = forms.EmailField(
        label = 'メールアドレス',
        widget=forms.EmailInput(attrs={
            'class':'form-email',
            'placeholder': 'Email',
        }),
    )
    
    message = forms.CharField(
        label='メッセージ',
        widget=forms.Textarea(attrs={
            'class': 'form-message',
            'placeholder': 'Message',
        }),
    )   

    def send_email(self):
        subject = "お問い合わせ"
        message = self.cleaned_data["message"]
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]

        from_email = "{name} <{email}>".format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER,]  
        try:
            send_mail(subject, message, from_email, recipient_list )
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")

