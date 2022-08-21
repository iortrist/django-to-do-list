from django.shortcuts import render, redirect
from .models import Item
from django.contrib import messages

# Create your views here.


def home(request):
    items = Item.objects.all()

    if request.method == 'POST':
        item = request.POST.get('item')
        form = Item()
        form.item = item
        form.save()
        return redirect('home')

    context = {'items': items}
    return render(request, 'base/home.html', context)


def removeItem(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    messages.success(request, 'Item has been removed successfully.')
    return redirect('home')


def editItem(request, pk):
    item = Item.objects.get(id=pk)

    if request.method == 'POST':
        item = request.POST.get('item')

        form = Item.objects.get(id=pk)
        form.item = item
        form.save()

        return redirect('home')

    context = {'item': item}
    return render(request, 'base/edit-item.html', context)
