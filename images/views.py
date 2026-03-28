from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm



# Create your views here.
@login_required
def image_create(request):
    if request.method == 'POST':
        # form sent
        form=ImageCreateForm(request.POST)
        if form.is_valid():
            # form data valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            #assign current user to item
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image Loaded Successfully') 
            return redirect(new_item.get_absolute_url())
            #redirect to new created item detail view
    else:
        #build form with data provided by the book markelet  via ge
        form=ImageCreateForm(data=request.get)

    return render(request, 'images/image/create.html', {'section':'images','form':form})
                   



