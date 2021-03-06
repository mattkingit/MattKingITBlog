from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january":"This is January",
    "february":"This is February",
    "march":"This is March",
    "april":"This is Apriil",
    "may":"This is May",
    "june":"This is June",
    "july":"This is July",
    "august":"This is August",
    "september":"This is September",
    "october":"This is October",
    "november":"This is November",
    "december":"This is December"
}

def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html",{
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    try:
        if month > len(months):
            return HttpResponseNotFound("Invalid month")
            
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404()

# Create your views here.
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html",{
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
    