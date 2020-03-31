from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


# Create your views here.
def display_all(request):
    # render read_all.html
    context = {
        "shows": Show.objects.all()
    }
    return render(request, 'read_all.html', context)

def add_new(request):
    #render create.html
    return render(request, 'create.html')

def create(request):
    print("****---->>>>request.POST: ", request.POST)
    #validation
    errors = Show.objects.basic_validator(request.POST)
    print("views errors:   ", errors)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    
    new_show = Show.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['release_date'], desc = request.POST['desc'])
    return redirect('/shows/'+str(new_show.id))

def display_one(request, show_id):
    #render read_one.html
    context = {
        "show": Show.objects.get(id = show_id)
    }
    return render(request, 'read_one.html', context)

def edit(request, show_id):
    #render edit.html
    context = {
        "show": Show.objects.get(id = show_id)
    }
    return render(request, 'edit.html', context)

def update(request, show_id):
    #save edits, redirect to read_one.html
    print("update POST request: ",request.POST)
    #run validation:
    errors = Show.objects.basic_validator(request.POST)
    print("views errors:   ", errors)
    if len(errors)>0: #if errors exist, make message then redirect to update form
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str(show_id)+'/edit')

    else: #if no errors, save updated data to db
        show = Show.objects.get(id = show_id)
        #for each field, update value
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.desc = request.POST['desc']
        show.save()
        messages.success(request, "Show successfully updated!")
        return redirect('/shows/'+str(show_id))


def destroy(request, show_id):
    #delete show, redirect to read_all.html
    Show.objects.get(id = show_id).delete()
    return redirect('/shows')