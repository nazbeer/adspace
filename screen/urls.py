from django.urls import path, include
from . views import *

urlpatterns = [
  path('screen_type/', ScreenTypeCreateListAPIView.as_view(), name='screen_type'),
  path('screen_type/update/<int:pk>/', ScreenTypeDetailAPIView.as_view(), name='screen_type_update_delete'),

  
  path('area/',AreaListCreateAPIView.as_view(), name='area_list_create'),
  path('area/update/<int:pk>/',AreaDetailAPIView.as_view(), name='area_update_delete'),

  path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
  path('categories/update/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),

  path('subcategories/', SubCategoryListCreateAPIView.as_view(), name='subcategory-list-create'),
  path('subcategories/update/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='subcategory-detail'), 

  path('tshirt_size/', TShirtSizeListCreateAPIView.as_view(), name='tshirt_size_list_create'),
  path('tshirt_size/update/<int:pk>/', TShirtSizeDetailAPIView.as_view(), name='tshirt_size_update_delete'),

  path('catalog/', CatalogListCreateAPIView.as_view(), name='catalog_list_create'),
  path('catalog/update/<int:pk>/', CatalogDetailAPIView.as_view(), name='catalog_update_delete'),

  #temp urls
    path('screen_types/', screen_type_list, name='screen_type_list'),
    path('screen_types/<int:pk>/', screen_type_detail, name='screen_type_detail'),
    path('screen_types/create/', screen_type_create, name='screen_type_create'),
    
  
]
