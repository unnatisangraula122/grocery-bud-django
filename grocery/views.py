from django.shortcuts import render, redirect, get_object_or_404
from .models import GroceryItem

def index(request):
    """Display items and handle inline edit"""
    items = GroceryItem.objects.all()
    edit_id = request.GET.get('edit')
    edit_item = None
    if edit_id:
        edit_item = get_object_or_404(GroceryItem, id=edit_id)
    return render(request, 'grocery/index.html', {'items': items, 'edit_item': edit_item})


def add_item(request):
    """Add new item"""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            GroceryItem.objects.create(name=name)
    return redirect('grocery:index')


def toggle_completed(request, item_id):
    """Toggle completed status"""
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, id=item_id)
        item.completed = not item.completed
        item.save()
    return redirect('grocery:index')


def delete_item(request, item_id):
    """Delete item"""
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, id=item_id)
        item.delete()
    return redirect('grocery:index')


def edit_item(request, item_id):
    """Redirect to index with edit parameter"""
    return redirect(f"/?edit={item_id}")


def update_item(request, item_id):
    """Update item name"""
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, id=item_id)
        name = request.POST.get('name', '').strip()
        if name:
            item.name = name
            item.save()
    return redirect('grocery:index')