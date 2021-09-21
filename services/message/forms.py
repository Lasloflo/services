from .models import Message
from django.forms import ModelForm, TextInput, Textarea

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['theme', 'name', 'email', 'phone', 'message']
        widgets = {'theme': TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Тема сообщения'}),
                   'name': TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Ваше имя'}),
                   'email': TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'E-mail'}),
                   'phone': TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Телефон'}),
                   'message': Textarea(attrs={'class': 'form-control',
                                            'id': 'message',
                                            'placeholder': 'Сообщение',
                                            'name': "", 'cols': "30", 'rows': "7"})
                   }