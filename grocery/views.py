from django.shortcuts import render, redirect, get_object_or_404
from .models import GroceryItem

# -------------------------------
# Display all items and edit mode
# -------------------------------
def index(request):
    """
    Display all grocery items.
    If ?edit=<id> is in URL, highlight the item for inline edit.
    """
    items = GroceryItem.objects.all()
    edit_id = request.GET.get('edit')
    edit_item = None

    if edit_id:
        edit_item = get_object_or_404(GroceryItem, id=edit_id)

    context = {
        'items': items,
        'edit_item': edit_item,
    }
    return render(request, 'grocery/index.html', context)


# -------------------------------
# Add new item
# -------------------------------
def add_item(request):
    """
    Add a new grocery item
    """
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            GroceryItem.objects.create(name=name)
    return redirect('grocery:index')


# -------------------------------
# Toggle completed status
# -------------------------------
def toggle_completed(request, item_id):
    """
    Toggle the completed status of a grocery item
    """
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, id=item_id)
        item.completed = not item.completed
        item.save()
    return redirect('grocery:index')

def delete_item(request, item_id):
    """
    Delete a grocery item
    """
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, id=item_id)
        item.delete()
    return redirect('grocery:index')



def edit_item(request, item_id):
    """
    Redirect to index with ?edit=<id> to enable inline editing
    """
    return redirect(f"/?edit={item_id}")

def update_item(request, item_id):
    """
    Update the name of an existing grocery item
    """
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, id=item_id)
        name = request.POST.get('name', '').strip()
        if name:
            item.name = name
            item.save()
    return redirect('grocery:index')