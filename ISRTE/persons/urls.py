from django.urls import path
from . import views
from access.views import GroupAccessCreate, PersonalAccessCreate
from law.views import CriminalConvictionAddView, CriminalCriminalCaseAddView, CriminalManhuntAddView

urlpatterns = [
    path('', views.criminals_list, name="record"),
    path('criminals/', views.criminals_list, name="list_criminals"),

    path('criminals/single/<int:pk>', views.criminal_single, name="criminal_single_url"),

    path('criminals/single/<int:pk>/access/group/create/', GroupAccessCreate.as_view(), name="group_access_create_url"),
    path('criminals/single/<int:pk>/access/personal/create/', PersonalAccessCreate.as_view(),
         name="personal_access_create_url"),

    path('criminals/create/', views.CriminalCreate.as_view(), name='criminal_create_url'),
    path('criminals/single/<int:pk>/update/', views.CriminalUpdate.as_view(), name="criminal_update_url"),
    path('criminals/single/<int:pk>/delete/', views.CriminalDelete.as_view(), name="criminal_delete_url"),

    path('criminals/single/<int:pk>/relatives/add', views.CriminalAddRelative.as_view(), name="relative_add_url"),
    path('criminals/single/<int:pk>/contact-persons/add', views.CriminalAddContactPersonView.as_view(),
         name="contact_person_add_url"),

    path('criminals/single/<int:pk>/address/add', views.CriminalAddressAdd.as_view(), name="address_add_url"),
    path('criminals/single/<int:pk>/contacts/add', views.CriminalContactDetailAddView.as_view(),
         name="contact-detail_add_url"),

    path('criminals/single/<int:pk>/conviction/add', CriminalConvictionAddView.as_view(),
         name="conviction_add_url"),
    path('criminals/single/<int:pk>/criminal-case/add', CriminalCriminalCaseAddView.as_view(),
         name="criminal_case_add_url"),
    path('criminals/single/<int:pk>/manhunt/add', CriminalManhuntAddView.as_view(),
         name="manhunt_add_url"),

    path('search-form/', views.search_form, name='search-form'),
    path('search/', views.search),
]
