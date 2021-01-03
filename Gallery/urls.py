from django.urls import path
from .views import Gallery_List, Gallery_Detail_Def


app_name = "gallery"
urlpatterns = [
    path('', Gallery_List, name="gallery_list"),
    path('detail/<pk>', Gallery_Detail_Def, name="gallery_detail"),
]