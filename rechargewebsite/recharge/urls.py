from django.urls import path
from . import views

urlpatterns = [
    path("recharge/plan-created/",views.create_plan,name='create_plan'),
    path("view_plans/",views.plan_list,name='plan_list'),
    path("recharge/",views.recharge,name='recharge'),

]
