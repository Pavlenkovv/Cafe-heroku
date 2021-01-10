from django.shortcuts import render, redirect
from contact_info.models import UserMessages

def home(request):
    messages = UserMessages.objects.filter(is_processed=False).order_by('send_date')
    return render(request, 'messages.html', context={'items': messages})

def update_messages(request, pk):
    UserMessages.objects.filter(pk=pk).update(is_processed=True)
    return redirect('/messages/')
