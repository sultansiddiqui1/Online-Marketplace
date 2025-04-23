from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Item,category
from .form import NewItemForm, EditItemForm
from django.db.models import Q

# Create your views here.

def items(request):
    query= request.GET.get('query','')
    categories= category.objects.all()
    category_id=request.GET.get('category',0)
    items= Item.objects.filter(isSold=False)
    
    if category_id:
        items=items.filter(category_id=category_id)
    
    if query:
        items=items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    return render(request,'item/items.html',{
        'items':items,
         'query':query,
         'categories':categories,
         'category_id':int(category_id)
         
    })

def detail(request,pk):
    item= get_object_or_404(Item,pk=pk)
    related_items=Item.objects.filter(category=item.category,isSold=False).exclude(pk=pk)[0:3]
    
    return render(request, 'item/detail.html',{
        'item':item,
        'related_items':related_items,
    })

@login_required
def new(request):
    if request.method=='POST':
        form=NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item= form.save(commit=False)
            # making sure only commiting after adding the created_by field.
            item.createdBy=request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:     
        form=NewItemForm()
   
    return render(request,'item/form.html',{
        'form':form,
        'title':'New Item'
        
    })
    
@login_required
def delete(request,pk):
    item= get_object_or_404(Item, pk=pk,createdBy=request.user)
    item.delete()
    
    return redirect('dashboard:index')


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, createdBy=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            print("form valid")
            form.save()
            return redirect('item:detail', pk=item.id)
        else:
            print("form invalid")
            print(form.errors) 
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Item'
    })
    
    