from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {"list_barang": data_barang_wishlist, "nama": "Kak Cinoy"}
    return render(request, "wishlist.html", context)

def show_xml(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    data = serializers.serialize("xml", data_barang_wishlist)
    return HttpResponse(data, content_type="text/xml")

def show_json(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    data = serializers.serialize("json", data_barang_wishlist)
    return HttpResponse(data, content_type="application/json")