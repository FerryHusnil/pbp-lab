from django.urls import path
from wishlist.views import (
    show_wishlist,
    show_xml,
    show_json,
    register,
    login_user,
    logout_user,
    show_wishlist_ajax,
    add_wishlist_ajax
)

app_name = "wishlist"

urlpatterns = [
    path("", show_wishlist, name="show_wishlist"),
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("ajax/", show_wishlist_ajax, name="show_wishlist_ajax"),
    path("ajax/post/", add_wishlist_ajax, name="add_wishlist_ajax")
]
