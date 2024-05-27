from django.urls import path
from athleteapp import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register("event",views.EventView,basename="events")
router.register("sponsor",views.SponsorshipView,basename="sponsorship")
router.register("winner",views.WinnerView,basename="winners")



urlpatterns = [
    path("profile/",views.profileView.as_view(),name="profile"),
] +router.urls
