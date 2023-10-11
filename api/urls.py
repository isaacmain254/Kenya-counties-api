from django.urls import path
from .views import CountyList, CountyDetail, SubcountyList, SubcountyDetails

urlpatterns = [
    path('county/', CountyList.as_view(), name='county'),
    path('county/<str:county_name>/', CountyDetail.as_view(), name='county-detail'),
    path('county/<str:county_name>/subcounties/', SubcountyList.as_view(), name='subcounties'),
    path('county/<str:county_name>/subcounties/<str:subcounty_name>/',
          SubcountyDetails.as_view(),
            name='subcounty_details'),
]
