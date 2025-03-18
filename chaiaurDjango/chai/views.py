from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404

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
