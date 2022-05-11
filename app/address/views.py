from django.shortcuts import render, HttpResponse
from .forms import AddressModelForm


# Create your views here.
def add(request):
    form = AddressModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        obj = form.save(commit=False)
        obj.save()
        print("Saved successfully.")
    context = {'form': form}
    return render(request, 'add.html', context)
