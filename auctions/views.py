from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .models import *




def index(request):
    all_listings = Create_listing.objects.all().values()
    return render(request, "auctions/listings.html", {
                "all_listings" : all_listings
             })
    


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
 

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create(request):
    if request.method == "POST":
        form = Listing_Form(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)   
            listing.user = request.user
            listing.save()
            return render(request, "auctions/listings.html", {
                "form" : form,  
                "name" : listing.user
             })
    else:
        form = Listing_Form()
        return render(request, "auctions/create.html", {
                "form" : form,   
             })

def my_listings(request):
    my_listings = Create_listing.objects.filter(user=request.user).values()
    return render(request, "auctions/mylistings.html", {
                "my_listings" : my_listings,
             })



    
   

    
