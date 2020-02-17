from django.shortcuts import render,redirect
from .models import Pet
from .form import PetForm

def available_list (request):
    list = Pet.objects.all()
    list2 = [x for x in list if x.available]

    context = {
        "available_pets":list2,
    }
    return render(request, 'home.html', context)

def pets_detail(request, pet_id):
    context = {
        "pets":Pet.objects.get(id=pet_id),
    }
    return render(request, 'detail.html', context)


def pet_create(request):
    form = PetForm()
    if request.method == "POST":
        form = PetForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Availables')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def pet_update(request,pet_id):
    obj =Pet.objects.get(id=pet_id)
    form=PetForm(instance=obj)
    if request.method=="POST":
        form=PetForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("Availables")
    context = {
        "obj":obj,
        "form":form
    }

    return render(request, 'update.html', context)

def pet_delete(request,pet_id):
    Pet.objects.get(id=pet_id).delete()
    return redirect('Availables')
