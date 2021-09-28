from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

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

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
        
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

# Create your views here.
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)


