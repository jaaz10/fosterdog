from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Dog
from .forms import DogForm, QuickUploadForm

def home(request):
    if request.method == 'POST':
        form = QuickUploadForm(request.POST, request.FILES)
        if form.is_valid():
            dog = form.save()
            messages.success(request, f'Thank you! {dog.name} has been added successfully!')
            return redirect('home')
    else:
        form = QuickUploadForm()
    
    recent_dogs = Dog.objects.filter(needs_foster=True)[:6]
    return render(request, 'dogs/home.html', {'form': form, 'recent_dogs': recent_dogs})

def dog_list(request):
    dogs = Dog.objects.filter(needs_foster=True)
    return render(request, 'dogs/dog_list.html', {'dogs': dogs})

@login_required
def add_dog(request):
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            dog = form.save()
            messages.success(request, f'{dog.name} has been added successfully!')
            return redirect('dogs:dog_list')
    else:
        form = DogForm()
    return render(request, 'dogs/dog_form.html', {'form': form, 'title': 'Add New Dog'})

@login_required
def edit_dog(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES, instance=dog)
        if form.is_valid():
            dog = form.save()
            messages.success(request, f'{dog.name} has been updated successfully!')
            return redirect('dogs:dog_list')
    else:
        form = DogForm(instance=dog)
    return render(request, 'dogs/dog_form.html', {'form': form, 'title': f'Edit {dog.name}'})
