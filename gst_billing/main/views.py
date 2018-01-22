from django.shortcuts import render, HttpResponseRedirect
from main.forms import AddNewItemForm
from main.models import AddNewItemModel
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def inventory(request):
    return render(request, 'Inventory.html')


def add_new_item_form(request):
    if request.method == 'POST':
        form = AddNewItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form = AddNewItemForm()
            messages.success(request, 'Bill successfully created.')
    else:
        form = AddNewItemForm()
    return render(request, 'AddNewItem.html', {'form': form})


def Update_current_item(request):
    item_id = AddNewItemModel.objects.all()
    return render(request, 'UpdateCurrentItem.html', {'items': item_id})


def delete(request, id):
    item_id = AddNewItemModel.objects.get(id=id)
    item_id.delete()
    return HttpResponseRedirect('/updateItem/')


def edit(request, id):
    item = AddNewItemModel.objects.get(id=id)
    context = {"item": item}
    return render(request, 'Edit.html', context)


def update(request, id):
    item = AddNewItemModel.objects.get(id=id)
    item.id = request.POST['id']
    item.name = request.POST['name']
    item.quantity = request.POST['quantity']
    item.price_per_unit = request.POST['price_per_unit']
    item.gst = request.POST['gst']
    item.save()
    return HttpResponseRedirect('/updateItem/')
