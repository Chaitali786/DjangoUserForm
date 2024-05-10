from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserForm

def index(request):
    return render (request , 'index.html')

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to success page after form submission
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')
