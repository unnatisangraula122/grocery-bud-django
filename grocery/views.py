from django.shortcuts import render, redirect, get_object_or_404
from .models import GroceryItem


def index(request):
    items = GroceryItem.objects.all()
    return render(request, 'grocery/index.html', {'items': items})


def toggle_completed(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, id=item_id)
        item.completed = not item.completed
        item.save()
    return redirect('grocery:index')


def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, id=item_id)
        item.delete()
    return redirect('grocery:index')


def edit_item(request, item_id):
    item = get_object_or_404(GroceryItem, id=item_id)

    if request.method == "POST":
        item.name = request.POST.get("name")
        item.save()
        return redirect("grocery:index")

    return render(request, "grocery/edit.html", {"item": item})

def add_item(request):
    """Add a new grocery item"""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()

        if name:
            GroceryItem.objects.create(name=name)

    return redirect('grocery:index')