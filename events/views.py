from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
import datetime

dt = datetime.datetime.now()

def home(request , year = dt.year , month = dt.strftime("%B")):
    month_number = list(calendar.month_name).index(month)
    month = month.capitalize()
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year , month_number)

    return render(request , 'events/home.html' , {
        "cal": cal
    })