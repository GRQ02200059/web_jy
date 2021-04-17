from django.shortcuts import render


def index(request):
  print("gggggggggggggggggggg")
  return   render(request,"index.html")
def timeline(request):
  return  render(request,"timeline.html")
def detail(request,book):

  the_book=request.POST.get("book")
  print("=" * 30)
  print(the_book)
  return render(request,"timeline.html")
