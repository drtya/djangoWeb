from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Corporations


# получение данных из бд
def index(request):
    corps = Corporations.objects.order_by('-id')
    return render(request, "main/index.html", {"corps": corps})
def edit(request):
    return render(request, "main/edit.html")


# сохранение данных в бд
def create(request):

    if request.method == "POST":
        corp = Corporations()
        corp.title = request.POST.get("title")
        corp.image = request.POST.get("image")
        corp.descr = request.POST.get("descr")
        corp.ovner = request.POST.get("ovner")
        corp.age = request.POST.get("age")
        corp.save()
        return HttpResponseRedirect("/")


#
# # изменение данных в бд
# def edit(request, id):
#     try:
#         corp = Corporations.objects.get(id=id)
#
#         if request.method == "POST":
#             corp.title = request.POST.get("title")
#             corp.image = request.POST.get("image")
#             corp.descr = request.POST.get("descr")
#             corp.ovner = request.POST.get("ovner")
#             corp.age = request.POST.get("age")
#             corp.save()
#             return HttpResponseRedirect("/")
#         else:
#             return render(request, "edit.html", {"corp": corp})
#     except Corporations.DoesNotExist:
#         return HttpResponseNotFound("<h2>Person not found</h2>")
#

# удаление данных из бд
def delete(request, id):
    try:
        corp = Corporations.objects.get(id=id)
        corp.delete()
        return HttpResponseRedirect("/")
    except Corporations.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")