


from http.client import HTTPResponse
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# from .models import *
from django.shortcuts import render, redirect
import cx_Oracle

from dbapp.home.forms import *
from dbapp.home.models import * 
from django.db import connection
from django.db.models import Q



@login_required(login_url="/login/")
def hotels(request):
    cursor = connection.cursor()
    cursor.execute('SELECT h.hotel_id, h.hotel_name,h.hotel_photo ,h.hotel_price, c.city_name, h.description FROM Hotels h,City c WHERE h.city_id = c.city_id')
    list = cursor.fetchall()
    # form=[]
    # for i in list:
    #     form.append(Card.objects.get(card_id = i[0]))
    return render(request, "home/hotels.html", {'form': list})
    # form = Hotels.objects.all() 
    # print(form)
    # return render(request, 'home/hotels.html', {'form': form})


    

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    # except:
    #     html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))





# CHANGE
@login_required(login_url="/login/")
def upload(request):
          upload = CardCreate()
          if request.method == "POST":
                    upload= CardCreate(request.POST, request.FILES)
                    if upload.is_valid():
                            obj = upload.save()
                            obj.user = request.user
                            obj.save()
                            return redirect('home')
                    else:
                              return HTTPResponse("""ERROR""")
          else:
                    return render(request, "home/add-card.html", {'form': upload})





# @login_required(login_url="/login/")
# def card(request):
#     form = Card.objects.all() 
#     return render(request, 'home/card.html', {'form': form})



#DONE
@login_required(login_url="/login/")       
def update(request, card_id):
    card_id = int(card_id)
    try:
        sel = Card.objects.get(card_id = card_id)
    except Card.DoesNotExist:
        return redirect('card')
    form = CardCreate(request.POST or None, instance = sel)
    if form.is_valid():
       form.save()
       return redirect('card')
    return render(request, 'home/add-card.html', {'form':form})

#DONE
@login_required(login_url="/login/")
def delete(request, card_id):
    card_id = int(card_id)
    try:
        sel = Card.objects.get(card_id = card_id)
    except Card.DoesNotExist:
        return redirect('card')
    sel.delete()
    return redirect('card')
        
   

#HOTEL ORDER
# @login_required(login_url="/login/")
# def hotel_order(request, hotel_id):
#           upload = HotelOrderCreate(hotel_id, )   
#           if request.method == "POST":
#                     upload = HotelOrderCreate(request.POST, request.FILES)
#                     if upload.is_valid():
#                               upload.save()
#                               return redirect('hotel_order')
#                     else:
#                               return HTTPResponse("""ERROR""")
#           else:
#                     return render(request, "home/hotel_orders.html", {'form': upload})
    # hotel_id = int(hotel_id)
    # try:
    #     sel = Hotels.objects.get(hotel_id = hotel_id)
    # except Hotels.DoesNotExist:
    #     return redirect('hotels')
    # form = HotelOrderCreate(request.POST or None, instance = sel)
    # if form.is_valid():
    #    form.save()
    #    return redirect('hotels')
    # return render(request, 'home/add-card.html', {'form':form})


#HOTEL ORDER


#DONE
@login_required(login_url="/login/")
def hotel_order(request, hotel_id):
    try:

        sel = Hotels.objects.get(hotel_id = hotel_id)
        # hotel_name = sel._meta.get_field('hotel_name')
        hotel_name = sel._meta.get_field('hotel_name').value_from_object(sel)
        balance = sel._meta.get_field('hotel_price').value_from_object(sel)
        # con = cx_Oracle.connect('c##dbuser/password/localhost/orcl')
        cursor = connection.cursor()
        # print("YOUR DATA-----------------------")
        # print(hotel_id , balance)
        cursor.callproc('inserthotelorder', [hotel_id, balance, request.user.id])
        # return self.fn_generic(cursor)
    except Hotels.DoesNotExist:
        return redirect('hotels')
    return redirect('hotels')


#DONE
@login_required(login_url="/login/")
def tours(request):
    cursor = connection.cursor()
    # form = Tour.objects.all() 
    cursor.execute('SELECT h.tour_id, h.tour_name,h.tour_photo ,h.tour_price, c.city_name, h.tour_description FROM Tour h,City c WHERE h.city_id = c.city_id')
    list = cursor.fetchall()
    # print(type(form))
    # print(form)
    return render(request, 'home/tours.html', {'form': list})

#DONE
@login_required(login_url="/login/")
def tour_order(request, tour_id):
    try:
        sel = Tour.objects.get(tour_id = tour_id)
        tour = sel._meta.get_field('tour_id').value_from_object(sel)
        balance = sel._meta.get_field('tour_price').value_from_object(sel)
        cursor = connection.cursor()
        cursor.callproc('inserttourorder', [tour, balance, request.user.id])
    except Tour.DoesNotExist:
        return redirect('tours')
    return redirect('tours')


#DONE
@login_required(login_url="/login/")
def card(request):
    cursor = connection.cursor()
    # cursor.execute('')
    cursor.execute('SELECT first_name, last_name , card_id, card_number, card_cvv,card_month, card_year FROM Card c, Auth_User a WHERE a.id = c.user_id and c.user_id = %s', [request.user.id])
    list = cursor.fetchall()
    cursor.execute('select sum(balance) from Card where Card.user_id = %s', [request.user.id])
    bal = cursor.fetchone()
    # cursor.execute('select first_name, last_name from Auth_User a where  a.id = %s', [request.user.id])
    # css = cursor.fetchall()
    # print(css)
    # print('----------------------------------------------------')
    # print(request.user.username)
    # print(bal)
    # form=[]
    # for i in list:
    #     form.append(Card.objects.get(card_id = i[0]))
    return render(request, "home/card.html", {'form': list , 'bal': bal})

#DONE
@login_required(login_url="/login/")
def gethotel_order(request):
    cursor = connection.cursor()
    cursor.execute('SELECT o.order_id, h.hotel_name, h.hotel_price FROM Hotels h, Hotel_orders o WHERE h.hotel_id = o.hotel_id  and  o.user_id = %s', [request.user.id])
    list = cursor.fetchall()
    n_pct = cursor.var(cx_Oracle.NUMBER)
    print(type(cursor.var(cx_Oracle.NUMBER)))
    cursor.execute('select sum(total_balance) from Hotel_orders o where o.user_id = %s', [request.user.id])
    sum = cursor.fetchone()
    print('SUM------------------------------' , sum)
    # form=[]
    # for i in list:
    #     form.append(Card.objects.get(card_id = i[0]))
    return render(request, "home/orders.html", {'form': list, 'sum':sum})

@login_required(login_url="/login/")
def gettour_order(request):
    cursor = connection.cursor()
    # sel = Hotels.objects.get(tour_id = tour)
        # hotel_name = sel._meta.get_field('hotel_name')
    # hotel_name = sel._meta.get_field('hotel_name').value_from_object(sel)
    # balance = sel._meta.get_field('hotel_price').value_from_object(sel)
    # cursor.execute('')
    cursor.execute('SELECT c.order_id, t.tour_name , a.city_name , t.tour_price from Tour_orders c, Tour t, City a WHERE c.tour_id = t.tour_id and t.city_id = a.city_id and c.user_id = %s', [request.user.id])
    # cursor.execute('SELECT order_id FROM Tour_orders c WHERE c.user_id = %s', [request.user.id])
    list = cursor.fetchall()
    cursor.execute('select sum(total_balance) from Tour_orders o where o.user_id = %s', [request.user.id])
    sum = cursor.fetchone()
    # form=[]
    # print(list)
    # for i in list:
    #     form.append(TourOrders.objects.get(order_id = i[0]))
    #     form.append(Tour.objects.get(tour_id = i[0]))
    return render(request, "home/tour-orders.html", {'form': list, 'sum':sum})

@login_required(login_url="/login/")
def deletetour_order(request, order_id):
    order_id = int(order_id)
    try:
        sel = TourOrders.objects.get(order_id = order_id)
    except TourOrders.DoesNotExist:
        return redirect('gettour_order')
    sel.delete()
    return redirect('gettour_order')


@login_required(login_url="/login/")
def deletehotel_order(request, order_id):
    order_id = int(order_id)
    try:
        sel = HotelOrders.objects.get(order_id = order_id)
    except HotelOrders.DoesNotExist:
        return redirect('gethotel_order')
    sel.delete()
    return redirect('gethotel_order')

def search(request):
    return render(request, "home/search.html")

def gethotel_search(request): 
    query = request.GET.get("q")
    object_list = Hotels.objects.filter(
        Q(hotel_name__icontains=query) | Q(description__icontains=query) | Q(hotel_price__icontains=query) | Q(hotel_photo__icontains=query) | Q(hotel_id__icontains=query)
    )
    print('===============================')
    print(object_list)
    return render(request, "home/results.html", {'object_list': object_list})

def gettour_search(request): 
    query = request.GET.get("q")
    object_list = Tour.objects.filter(
        Q(tour_name__icontains=query) | Q(tour_description__icontains=query) | Q(tour_price__icontains=query) 
        | Q(tour_photo__icontains=query) | Q(tour_id__icontains=query)
    )
    print('===============================')
    print(object_list)
    return render(request, "home/tourresults.html", {'object_list': object_list})


@login_required(login_url="/login/")
def about_us(request):
    

    return render(request, "home/page-about-us.html")






 