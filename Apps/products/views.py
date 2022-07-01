from django.shortcuts import render

from Apps.products.models import Produit

# Create your views here.
def product_list(request):
    produits = Produit.objects.all()
    context = {
        'produits' : produits
    }
    return render(request,'produit/list.html',context)

def product_details(request,id):
    produit = Produit.objects.filter(id=id).first()
    context = {
        'produit' : produit
    }
    return render(request,'produit/détails.html',context)

def  new_product(request):
    return ''