from django.urls import path
from adminapp import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register("event",views.EventView,basename="events")
router.register("student",views.StudentsView,basename="students")
router.register("college",views.CollegeView,basename="colleges")
router.register("sponsor",views.SponsorView,basename="sponsors")
router.register("winner",views.WinnerView,basename="winners")



urlpatterns = [

] +router.urls
