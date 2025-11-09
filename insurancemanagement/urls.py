
from django.contrib import admin
from django.urls import path, re_path
from insurance import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),


    path('customer/',include('customer.urls')),
    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='insurance/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),

    
    path('adminlogin', LoginView.as_view(template_name='insurance/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-view-customer', views.admin_view_customer_view,name='admin-view-customer'),
    path('admin-view-pending-customers', views.admin_view_pending_customers_view,name='admin-view-pending-customers'),
    re_path(r'^approve-customer/(?P<pk>[0-9]+)/', views.approve_customer_view,name='approve-customer'),
    re_path(r'^update-customer/(?P<pk>[0-9]+)/', views.update_customer_view,name='update-customer'),
    re_path(r'^delete-customer/(?P<pk>[0-9]+)/', views.delete_customer_view,name='delete-customer'),

    path('admin-category', views.admin_category_view,name='admin-category'),
    path('admin-view-category', views.admin_view_category_view,name='admin-view-category'),
    path('admin-update-category', views.admin_update_category_view,name='admin-update-category'),
    re_path(r'^update-category/(?P<pk>[0-9]+)/', views.update_category_view,name='update-category'),
    path('admin-add-category', views.admin_add_category_view,name='admin-add-category'),
    path('admin-delete-category', views.admin_delete_category_view,name='admin-delete-category'),
    re_path(r'^delete-category/(?P<pk>[0-9]+)/', views.delete_category_view,name='delete-category'),


    path('admin-policy', views.admin_policy_view,name='admin-policy'),
    path('admin-add-policy', views.admin_add_policy_view,name='admin-add-policy'),
    path('admin-view-policy', views.admin_view_policy_view,name='admin-view-policy'),
    path('admin-update-policy', views.admin_update_policy_view,name='admin-update-policy'),
    re_path(r'^update-policy/(?P<pk>[0-9]+)/', views.update_policy_view,name='update-policy'),
    path('admin-delete-policy', views.admin_delete_policy_view,name='admin-delete-policy'),
    re_path(r'^delete-policy/(?P<pk>[0-9]+)/', views.delete_policy_view,name='delete-policy'),

    path('admin-view-policy-holder', views.admin_view_policy_holder_view,name='admin-view-policy-holder'),
    path('admin-view-approved-policy-holder', views.admin_view_approved_policy_holder_view,name='admin-view-approved-policy-holder'),
    path('admin-view-disapproved-policy-holder', views.admin_view_disapproved_policy_holder_view,name='admin-view-disapproved-policy-holder'),
    path('admin-view-waiting-policy-holder', views.admin_view_waiting_policy_holder_view,name='admin-view-waiting-policy-holder'),
    re_path(r'^approve-request/(?P<pk>[0-9]+)/', views.approve_request_view,name='approve-request'),
    re_path(r'^reject-request/(?P<pk>[0-9]+)/', views.disapprove_request_view,name='reject-request'),
    re_path(r'^terminate-policy/(?P<pk>[0-9]+)/', views.terminate_policy_view,name='terminate-policy'),

    path('admin-question', views.admin_question_view,name='admin-question'),
    re_path(r'^update-question/(?P<pk>[0-9]+)/', views.update_question_view,name='update-question'),

]
