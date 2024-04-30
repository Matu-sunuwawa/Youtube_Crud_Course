from django.shortcuts import render, redirect
from .models import NoteApp
from .forms import NoteForm

# Create your views here.

def home(request):
    return render(request, 'app/lists.html')

def lists(request):
    lists = NoteApp.objects.all()

    ctx = {'lists':lists}
    return render(request, 'app/lists.html', ctx)

def addlist(request):
    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lists')
    else:
        form = NoteForm()
    ctx = {'form':form}
    return render(request, 'app/add_list.html', ctx)

def updatelist(request, pk):
    list = NoteApp.objects.get(id=pk)
    form = NoteForm(instance=list)

    if request.method=='POST':
        form = NoteForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('lists')
    else:
        form = NoteForm(instance=list)

    ctx = {'form':form, 'list':list}
    return render(request, 'app/update_list.html', ctx)

def deletelist(request, pk):
    list = NoteApp.objects.get(id=pk)

    if request.method=='POST':
        list.delete()
        return redirect('lists')
    
    ctx = {'list':list}
    return render(request, 'app/delete_list.html', ctx)