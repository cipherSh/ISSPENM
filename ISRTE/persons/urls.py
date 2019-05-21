from django.urls import path
from . import views
from access.views import GroupAccessCreate, PersonalAccessCreate
from law.views import CriminalConvictionAddView, CriminalCriminalCaseAddView, CriminalManhuntAddView

urlpatterns = [
    path('', views.criminals_list, name="record"),

    path('criminals/', views.criminals_page, name="criminals_page_url"),
    path('criminals/list', views.criminals_list, name="criminals_list"),
    path('criminals/my_docs', views.criminal_my_docs, name="criminals_my_docs"),
    path('criminals/uncheck_docs', views.criminal_uncheck_docs, name="criminals_uncheck_docs"),


    path('criminals/single/<int:pk>', views.criminal_single, name="criminal_single_url"),

    path('criminals/single/<int:pk>/access/group/create/', GroupAccessCreate.as_view(), name="group_access_create_url"),
    path('criminals/single/<int:pk>/access/personal/create/', PersonalAccessCreate.as_view(),
         name="personal_access_create_url"),

    path('criminals/single/<int:pk>/access/change/close', views.criminal_close_change,
         name="criminal_close_change_url"),
    path('criminals/single/<int:pk>/check', views.criminal_check,
         name="criminal_check_url"),

    path('criminals/create/', views.CriminalCreate.as_view(), name='criminal_create_url'),
    path('criminals/single/<int:pk>/update/', views.CriminalUpdate.as_view(), name="criminal_update_url"),
    path('criminals/single/<int:pk>/delete/', views.CriminalDelete.as_view(), name="criminal_delete_url"),
    path('criminals/single/<int:pk>/update/owner/', views.CriminalOwnerChangeView.as_view(),
         name="criminal_change_owner_url"),
    path('criminals/single/<int:pk>/update/confident/', views.CriminalConfidentChangeView.as_view(),
         name="criminal_confident_change_url"),


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
