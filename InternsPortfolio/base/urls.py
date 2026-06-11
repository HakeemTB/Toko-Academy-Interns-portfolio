from django.urls import path
# from .  import  views
from .views  import index_view

urlpatterns = [
    path('', index_view, name='index'),

    # path('',  views.home,  name=home)


]

# app_name = 'base'

# urlpatterns = [
#  # post views
#  path('', views.index_view, name='index_view'),
#  path('<int:id>/', views.index_view, name='index_view'),
# ]