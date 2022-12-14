import datetime
from django.shortcuts import render, redirect
from wishlist.models import BarangWishlist
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/wishlist/login/")
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        "list_barang": data_barang_wishlist,
        "last_login": request.COOKIES.get("last_login"),
        "logged_in": request.user.is_authenticated,
    }
    return render(request, "wishlist.html", context)

@login_required(login_url="/wishlist/login/")
def show_wishlist_ajax(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        "list_barang": data_barang_wishlist,
        "last_login": request.COOKIES.get("last_login"),
        "logged_in": request.user.is_authenticated,
    }
    return render(request, "wishlist_ajax.html", context)

@login_required(login_url="/wishlist/login/")
def add_wishlist_ajax(request):
    if request.method == "POST":
        nama_barang = request.POST.get("nama_barang")
        harga_barang = request.POST.get("harga_barang")
        deskripsi = request.POST.get("deskripsi")
        barang = BarangWishlist(
            nama_barang=nama_barang,
            harga_barang=harga_barang,
            deskripsi=deskripsi,
        )
        barang.save()
        return redirect("wishlist:show_wishlist_ajax")
    else:
        return redirect("wishlist:show_wishlist_ajax")

def show_xml(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    data = serializers.serialize("xml", data_barang_wishlist)
    return HttpResponse(data, content_type="text/xml")


def show_json(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    data = serializers.serialize("json", data_barang_wishlist)
    return HttpResponse(data, content_type="application/json")


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun telah berhasil dibuat!")
            return redirect("wishlist:login")
        else:
            messages.error(request, 'Akun gagal dibuat!')

    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, "Username atau Password salah!")
    context = {}
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("wishlist:login"))
    response.delete_cookie("last_login")
    return redirect("wishlist:login")

