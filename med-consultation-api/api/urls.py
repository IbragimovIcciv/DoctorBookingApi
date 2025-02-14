from django.urls import path
from api.views import (
    RegisterApiView,
    LoginApiView,
    DoctorListApiView,
    DoctorDetailApiView,
    DoctorFilterView,
    NewsApiView,
    DoctorUpdateApiView,
    UserUpdateView,
    DoctorDateAPIView,
    BookingAPIView
)

urlpatterns = [
    # user routes
    path("register/", RegisterApiView.as_view(), name="register"),
    path("login/", LoginApiView.as_view(), name="login"),
    path("users/update/<int:pk>/", UserUpdateView.as_view(), name="users"),

    # Booking routes
    path("date/", DoctorDateAPIView.as_view(), name="doctors"),
    path("booking/<int:pk>/", BookingAPIView.as_view(), name="booking"),

    # Doctor routes
    path("doctors/", DoctorListApiView.as_view(), name="doctors-list"),
    path("doctors/<int:pk>/", DoctorDetailApiView.as_view(), name="doctors-detail"),
    path("doctors/update/<int:pk>/", DoctorUpdateApiView.as_view(), name="doctors-update"),

    # Doctor search route
    path("search/", DoctorFilterView.as_view(), name="doctor-search"),

    # News routes
    path("news/", NewsApiView.as_view(), name="news-list"),
    path("news/<int:pk>/", NewsApiView.as_view(), name="news-detail"),
]
