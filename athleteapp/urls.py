from django.urls import path
from athleteapp import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register("event",views.EventView,basename="events")
router.register("sponsor",views.SponsorshipView,basename="sponsorship")
router.register("winner",views.WinnerView,basename="winners")



urlpatterns = [
    path("profile/",views.profileView.as_view(),name="profile"),
    path("partevent/<int:event_id>/",views.ParticipateEventView.as_view(),name="partevet"),
    path("parteventget/",views.ParticipateEventViewGET.as_view(),name="partevent"),
    path("mywinsdistrict/",views.MyWinsDistrict.as_view(),name="windist"),
    path("mywinsstate/",views.MyWinsState.as_view(),name="winstate"),
] + router.urls
