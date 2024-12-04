from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from datetime import datetime
from django.db.models import Q

from .models import Truck

def dashboard(request):
    return render(request, 'dashboard.html')

def all_trucks(request):
    """View for displaying all trucks."""
    search_query = request.GET.get('q', '')
    if 'day' not in request.GET:
        selected_day = datetime.now().strftime('%A')
    else:
        selected_day = request.GET['day']
    sort_order = request.GET.get('sort', 'asc')

    trucks = Truck.objects.all()

    if search_query:
        trucks = trucks.filter(
            Q(truck_number__icontains=search_query) |
            Q(truck_origin__icontains=search_query) |
            Q(truck_destination__icontains=search_query) |
            Q(truck_operator__icontains=search_query)
        )

    if selected_day and selected_day != 'All':
        trucks = trucks.filter(truck_day__icontains=selected_day)

    sort_field = '-truck_departure_time' if sort_order == 'desc' else 'truck_departure_time'
    trucks = trucks.order_by(sort_field)

    per_page_param = request.GET.get('per_page', 8)
    try:
        per_page = int(per_page_param)
    except ValueError:
        per_page = 8

    paginator = Paginator(trucks, per_page)
    page_number = request.GET.get('page', 1)
    trucks_paginated = paginator.get_page(page_number)

    return render(request, 'emp/alltrucks.html', {
        "trucks": trucks_paginated,
        "search_query": search_query,
        "selected_day": selected_day,
        "per_page": per_page,
        "sort_order": sort_order,
    })

def single_truck(request, empid):
    try:
        truck = Truck.objects.get(truck_id=empid)
        return render(request, 'emp/singletruck.html', {'singletruck': truck})
    except Truck.DoesNotExist:
        return render(request, 'emp/singletruck.html', {'error_message': 'Truck not found'})

def single_truck_company(request, empid):
    try:
        company = Truck.objects.get(truck_id=empid)
        return render(request, 'emp/singlecompanydetails.html', {'singletruck': company})
    except Truck.DoesNotExist:
        return render(request, 'emp/singlecompanydetails.html', {'error_message': 'Truck not found'})

def add_truck(request):
    if request.method == 'POST':
        truck_day = request.POST.get('truck_day')
        truck_departure_time = request.POST.get('truck_departure_time')
        truck_truck = request.POST.get('truck_truck')
        truck_number = request.POST.get('truck_number')
        truck_origin = request.POST.get('truck_origin')
        truck_destination = request.POST.get('truck_destination')
        truck_operator = request.POST.get('truck_operator')
        truck_coloader = request.POST.get('truck_coloader', '')
        truck_coolie = request.POST.get('truck_coolie', '')
        truck_adr = request.POST.get('truck_adr', '')
        truck_order_number = request.POST.get('truck_order_number', '')
        truck_street = request.POST.get('truck_street')
        truck_street_number = request.POST.get('truck_street_number')
        truck_postal_code = request.POST.get('truck_postal_code')
        truck_city = request.POST.get('truck_city')
        truck_country = request.POST.get('truck_country')
        
        phone_country_code = request.POST.get('phone_country_code')
        phone_area_code = request.POST.get('phone_area_code')
        phone_number = request.POST.get('phone_number')

        Truck.objects.create(
            truck_day=truck_day,
            truck_departure_time=truck_departure_time,
            truck_truck=truck_truck,
            truck_number=truck_number,
            truck_origin=truck_origin,
            truck_destination=truck_destination,
            truck_operator=truck_operator,
            truck_coloader=truck_coloader,
            truck_coolie=truck_coolie,
            truck_adr=truck_adr,
            truck_order_number=truck_order_number,
            truck_street=truck_street,
            truck_street_number=truck_street_number,
            truck_postal_code=truck_postal_code,
            truck_city=truck_city,
            truck_country=truck_country,
            phone_country_code=phone_country_code,
            phone_area_code=phone_area_code,
            phone_number=phone_number,
        )

        return redirect('/alltrucks')

    current_day = datetime.now().strftime('%A')
    return render(request, 'emp/addtruck.html', {'current_day': current_day})

def update_special(request, truck_id):
    truck = Truck.objects.get(truck_id=truck_id)
    if request.method == 'POST':
        truck_coloader = request.POST.get('truck_coloader', '')
        truck_coolie = request.POST.get('truck_coolie', '')
        truck_adr = request.POST.get('truck_adr', '')
        truck_order_number = request.POST.get('truck_order_number', '')

        # Update the truck with the new special attributes
        truck.truck_coloader = truck_coloader
        truck.truck_coolie = truck_coolie
        truck.truck_adr = truck_adr
        truck.truck_order_number = truck_order_number
        truck.save()

        return redirect('alltrucks')

    return render(request, 'emp/updatespecial.html', {"truck": truck})

def update_truck(request, truck_id):
    try:
        truck = Truck.objects.get(truck_id=truck_id)
    except Truck.DoesNotExist:
        return render(request, 'emp/updatetruck.html', {'error_message': 'Truck not found'})

    if request.method == 'POST':
        truck.truck_day = request.POST.get('truck_day')
        truck.truck_departure_time = request.POST.get('truck_departure_time')
        truck.truck_truck = request.POST.get('truck_truck')
        truck.truck_number = request.POST.get('truck_number')
        truck.truck_origin = request.POST.get('truck_origin')
        truck.truck_destination = request.POST.get('truck_destination')
        truck.truck_operator = request.POST.get('truck_operator')
        
        truck.save()
        return redirect('/alltrucks')

    return render(request, 'emp/updatetruck.html', {'singletruck': truck})


def delete_truck(request, truck_id):
    truck = Truck.objects.get(truck_id=truck_id)
    truck.delete()
    return redirect('/alltrucks')