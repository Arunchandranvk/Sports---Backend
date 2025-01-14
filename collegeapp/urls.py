from django.urls import path
from collegeapp import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register("event",views.EventView,basename="events")
router.register("student",views.StudentsView,basename="students")
router.register("sponsors",views.SponsorshipView,basename="sponsors")
router.register("sponsorstu",views.SponsorshipStuView,basename="sponsorstu")




urlpatterns = [
    path("profile/",views.profileView.as_view(),name="profile"),
    path("studregister/",views.StudentRegistrationView.as_view(),name="studsignup"),
    path("participatedstudents/",views.EventParticipatedStudentsView.as_view(),name="studsignup"),
   
    
] +router.urls 
