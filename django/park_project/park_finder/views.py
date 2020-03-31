from django.shortcuts import render, redirect
from django.contrib import messages
import re
import bcrypt
from .models import *

# Create your views here.
# ?? RENDER FUNCTIONS
def index(request):
    return render(request,'index.html')

def dashboard(request):
    user = User.objects.get(email = request.session['email'])
    context = {
        "user": user,
        "places_to_visit": Visit.objects.filter(user_id = user.id).filter(has_visited=False),
        "visited_places": Visit.objects.filter(has_visited=True),
    }
    print("dashboard context: ", context)
    return render(request, 'dashboard.html', context)

def park_search(request):
    #renders park search page
    context = {
        "parks": Park.objects.all(),
    }
    return render(request, 'park_search.html', context)

def add_park(request):
    #renders add a park page
    return render(request, 'add_park.html')

def search_results(request):
    #renders search results page with info from search_db
    context = {
        #search results
    }
    return render(request, 'search_results.html', context)

def user_profile(request, user_id):
    #renders user's profile
    user = User.objects.get(id = user_id)
    visits = Visit.objects.get(user_id = user_id)
    context = {
        "user": user,
        "visits": visits,
    }
    return render(request, 'user_profile.html', context)

def memory_log(request, visit_id):
    #renders user's memory log for specific visit
    user_visit = Visit.objects.get(id = visit_id)
    adults=user_visit.hiking_group_at_visit_time[0]
    kids=user_visit.hiking_group_at_visit_time[1]
    people_with_disabilities=user_visit.hiking_group_at_visit_time[2]
    pets=user_visit.hiking_group_at_visit_time[3]
    context = {
        "user_visit": user_visit,
    }
    return render(request, 'memory_log.html', context)

def add_trail_report(request, park_id):
    print("loading trail report page for park_id: ", park_id)
    #render's trail report template
    user = User.objects.get(email=request.session['email'])
    park = Park.objects.get(id=park_id)
    context = {
        "user": user,
        "park": park,
    }
    return render(request, 'add_trail_report.html', context)

def park_profile(request, park_id):
    #renders park profile page
    user = User.objects.get(email = request.session['email'])
    park = Park.objects.get(id=park_id)
    visits = Visit.objects.filter(park_id=park_id).order_by("-created_at")
    visits_count = len(visits)
    activities = park.permitted_activities.split(',')
    natural_features = park.natural_features.split(',')
    memory_log_id = None
    def visit_check(visits, user_id): 
        for visit in visits: 
            if visit.user_id == user_id and visit.has_visited==False:
                return "remove_from_list"
            elif visit.user_id==user_id and visit.has_visited==True:
                memory_log_id = visit.id
                return "memory_log", memory_log_id
            else: 
                return "add_to_list"
    context = {
        "user": user,
        "park" : park,
        "visits" : visits,
        "visits_count": visits_count,
        "activities": activities,
        "natural_features": natural_features,
        "list_action": visit_check(visits, user.id),
        "memory_log_id": memory_log_id,
    }
    print("Context: ", context)
    return render(request, 'park_profile.html', context)


# ? REDIRECT FUNCTIONS
def register(request):
    #validate potential new user
    errors = User.objects.registration_validator(request.POST)
    #fail = redirect to index with messages
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    #succeed = create user, add user to session **hash password**, redirect to success
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        # dob = request.POST['dob'],
        email = request.POST['email'],
        password = bcrypt.hashpw((request.POST['password']).encode(), bcrypt.gensalt()).decode(),
    )
    request.session['email'] = request.POST['email']
    print("creating new user...")
    return redirect('/dashboard')

def login(request):
    #validate login info: if email in db, if pw matches
    errors = User.objects.login_validator(request.POST)
    #fail = redirect to index with messages
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    #succeed = redirect to user's wall 
    request.session['email'] = request.POST['email']
    print("logging in user...")
    return redirect('/dashboard')

def logout(request):
    #clear session 
    request.session.clear()
    #redirect to index
    return redirect('/')

def search_db(request):
    #uses park_search filters to search db for matching parks
    return redirect('/search_results')

def create_park(request):
    #uses add_park info to create new park in db
    return redirect('/dashboard')

def create_report(request, park_id):
    print("creating a new trail report with: ", request.POST)
    #uses add_trail_report form info to create new Visit
    if len(Visit.objects.filter(user_id=User.objects.get(email=request.session['email']).id))>0:
        # update existing visit & switch has_visited to True
        visit = Visit.objects.get(user_id=User.objects.get(email=request.session['email']).id)
        visit.has_visited = True
        visit.date_visited = request.POST['date_visited']
        visit.public_notes = request.POST['public_notes']
        visit.private_notes = request.POST['private_notes']
        visit.hiking_group_at_visit_time = (f"{request.POST['hg_adults']}, {request.POST['hg_kids']}, {request.POST['hg_ppl_w_dis']}, {request.POST['hg_pets']}")
        visit.rating = request.POST['rating']
        visit.save()
    else: #create new Visit & set has_visited = True
        Visit.objects.create(
            has_visited = True,
            date_visited = request.POST['date_visited'],
            public_notes = request.POST['public_notes'],
            private_notes = request.POST['private_notes'],
            hiking_group_at_visit_time = (f"{request.POST['hg_adults']}, {request.POST['hg_kids']}, {request.POST['hg_ppl_w_dis']}, {request.POST['hg_pets']}"),
            rating = request.POST['rating'],
            user_id = User.objects.get(email = request.session['email']).id,
            park_id = park_id,
        )
    return redirect('/dashboard')

def add_visit_from_results(request, park_id):
    #creates visit with logged-in user's id && park id 
    #leave all defaults (esp has_visited=False)
    #? where to redirect? 
    #want to stay on search results and keep filtered search
    pass

def add_visit_from_park_profile(request, park_id):
    #same as above, but different routing
    Visit.objects.create(
        user = User.objects.get(email=request.session['email']),
        park = Park.objects.get(id=park_id),
    )
    return redirect('/park_profile/'+str(park_id))

def remove_park_from_list(request, park_id):
    #remove unvisited park from user's to-go list
    user = User.objects.get(email=request.session['email'])
    visit = Visit.filter(user_id = user.id).get(park_id=park_id)
    visit.delete()
    return redirect('/park/profile/'+str(park_id))