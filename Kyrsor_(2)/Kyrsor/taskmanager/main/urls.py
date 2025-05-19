from django.urls import path
from . import views



urlpatterns = [
    # path('',views.index, name='home'),
    # path('vuz',views.vuz_bootstrap, name='Vuz'),


    # path('',views.VuzView.as_view(), name='home'),
    # path('filter/',views.FilterVusView.as_view(), name="filter"),
    path('search/',views.Search.as_view(), name="search"),
    # path('<int:pk>/',views.VusDetailView.as_view(), name="vuz_detail"),
    path('<int:pk>/info', views.VuzDetailView.as_view(template_name='main/vuz_1_detail.html'), name='vuz_detail'),
    path('<int:pk>/programs', views.VuzDetailView.as_view(template_name='main/vuz_1_detail_1.html'), name='vuz_detail_1'),
    path('<int:pk>/reviews', views.VuzDetailView.as_view(template_name='main/vuz_1_detail_2.html'), name='vuz_detail_2'),

    path('<int:pk>/xxx', views.VuzDetailView.as_view(template_name='main/vuz_1_detail_2_1.html'), name='vuz_detail_2_1'),
    # path('otz',views.neural_network_form, name='otz'),
    # path('otzz/',views.neural_network_process, name='neural_network_process'),
    path('', views.VuzView.as_view(), name='home'),
    # path('page_2/', views.VuzView.as_view(), name='otz'),
    path('otz', views.comments, name='otz'),
    path('success', views.otz_bootstrap, name='success'),
    path('get_vuz_options/', views.get_vuz_options, name='get_vuz_options'),



]

