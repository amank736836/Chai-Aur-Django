from django.shortcuts import render
from .models import ChaiVarity, ChaiStore
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm

# Create your views here.


def all_chai(request):
    chais = ChaiVarity.objects.all()
    context = {
        "chais": chais,
    }
    return render(request, "chai/all_chai.html", context)


def chai_detail(request, id):
    chai = get_object_or_404(ChaiVarity, id=id)
    context = {
        "chai": chai,
    }
    return render(request, "chai/chai_detail.html", context)


def chai_store_view(request):
    stores = None
    if request.method == "POST":
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_varity = form.cleaned_data["chai_varity"]
            stores = ChaiStore.objects.filter(chai_varieties=chai_varity)
    else:
        form = ChaiVarityForm()

    return render(request, "chai/chai_stores.html", {"stores": stores, "form": form})
