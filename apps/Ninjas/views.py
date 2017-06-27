# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	return render(request,'Ninjas/index.html')

def ninjas(request):
	return render(request,"Ninjas/ninjas.html")

def hues(request,color):
	if color == "blue":
		return render(request, "Ninjas/blue.html")
	if color == "orange":
		return render(request, "Ninjas/orange.html")
	if color == "red":
		return render(request, "Ninjas/red.html")
	if color == "purple":
		return render(request, "Ninjas/purple.html")
	return render(request, "Ninjas/notapril.html")

