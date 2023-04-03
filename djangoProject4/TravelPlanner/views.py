from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from TravelPlanner.models import Destination, PackingList, PackingItem, TravelPlan, Photo
from TravelPlanner.forms import TravelPlanForm, PhotoForm

def homepage_view(request):
    return render(request, 'TravelPlanner/homepage.html')



#wyświetli listę wszystkich destynacji

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, "TravelPlanner/destination_list.html", {'destinations': destinations})

#widok szczegółów destynacji, który wyświetli informacje o jednej destynacji

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'TravelPlanner/destination_detail.html', {'destination': destination})

#wyświetli formularz i zapisze nową destynację w bazie danych

@login_required
def destination_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.save()
            return redirect('destination_detail', pk=destination.pk)
    else:
        form = DestinationForm()
    return render(request, 'TravelPlanner/destination_create.html', {'form': form})

#Ten widok wyświetla listę wszystkich planów podróży użytkownika.
# Używa filtru filter na modelu TravelPlan, aby uzyskać tylko te plany podróży, które należą do zalogowanego użytkownika.
# Następnie zwraca szablon travel_plan_list.html z listą planów podróży.

@login_required
def travel_plan_list(request):
    travel_plans = TravelPlan.objects.filter(user=request.user)
    return render(request, 'TravelPlanner/travel_plan_list.html', {'travel_plans': travel_plans})



#wyświetli formularz i zapisze nowy plan podróży w bazie danych

@login_required
def travel_plan_add(request):
    if request.method == 'POST':
        form = TravelPlanForm(request.POST)
        if form.is_valid():
            travel_plan = form.save(commit=False)
            travel_plan.user = request.user
            travel_plan.save()
            return redirect('travel_plan_detail', pk=travel_plan.pk)
    else:
        form = TravelPlanForm()
    return render(request, 'TravelPlanner/travel_plan_add.html', {'form': form})

#wyświetla szczegóły planu podróży,

def travel_plan_detail(request, pk):
    travel_plan = get_object_or_404(TravelPlan, pk=pk)
    if travel_plan.user != request.user:
        return HttpResponseForbidden()
    context = {'travel_plan': travel_plan}
    return render(request, 'TravelPlanner/travel_plan_detail.html', context)

#pozwala użytkownikowi na dodanie nowego planu podróży

@login_required
def travel_plan_create(request):
    if request.method == 'POST':
        form = TravelPlanForm(request.POST)
        if form.is_valid():
            travel_plan = form.save(commit=False)
            travel_plan.user = request.user
            travel_plan.save()
            return redirect('travel_plan_detail', pk=travel_plan.pk)
    else:
        form = TravelPlanForm()
    context = {'form': form}
    return render(request, 'TravelPlanner/travel_plan_create.html', context)

#wyświetli formularz i zapisze nową listę pakowania w bazie danych

@login_required
def packing_list_add(request):
    if request.method == 'POST':
        form = PackingListForm(request.POST)
        if form.is_valid():
            packing_list = form.save(commit=False)
            packing_list.user = request.user
            packing_list.save()
            return redirect('packing_list_detail', pk=packing_list.pk)
    else:
        form = PackingListForm()
    return render(request, 'TravelPlanner/packing_list_add.html', {'form': form})

#widok dodawania nowego elementu listy pakowania, który wyświetli formularz i zapisze nowy element listy pakowania w bazie danych

@login_required
def packing_item_add(request):
    if request.method == 'POST':
        form = PackingItemForm(request.POST)
        if form.is_valid():
            packing_item = form.save(commit=False)




#umożliwia użytkownikowi dodanie zdjęcia do danego planu podróży

@login_required
def photo_upload(request, pk):
    travel_plan = get_object_or_404(TravelPlan, pk=pk)
    if travel_plan.user != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.travel_plan = travel_plan
            photo.save()
            return redirect('travel_plan_detail', pk=travel_plan.pk)
    else:
        form = PhotoForm()
    context = {'form': form, 'travel_plan': travel_plan}
    return render(request, 'TravelPlanner/photo_upload.html', context)


