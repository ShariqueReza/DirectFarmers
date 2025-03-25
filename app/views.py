from django.shortcuts import render,redirect
from app.forms import Contact_UsForm
# Create your views here.
def index_page(request):
    context={}
    return render(request,'app/index.html',context)

def contact_page(request):
    form=Contact_UsForm()
    if request.method == 'POST':
        form = Contact_UsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = Contact_UsForm()
    context={'form':form}
    return render(request,'app/contact.html',context)
