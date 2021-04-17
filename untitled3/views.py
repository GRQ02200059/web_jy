from django.shortcuts import render


def index(request):
 print("gggggggggggggggggggg")
 return   render(request,"index.html")
def timeline(request):
 return  render(request,"timeline.html")