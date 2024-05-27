from django.urls import path
from sponsorapp import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register("event",views.EventView,basename="events")
router.register("student",views.StudentsView,basename="students")
router.register("college",views.CollegeView,basename="colleges")
router.register("sponsorship",views.MysponsorshipView,basename="sponsors")
router.register("winner",views.WinnerView,basename="winners")



urlpatterns = [
    path("profile/",views.profileView.as_view(),name="profile"),
    
] +router.urls
