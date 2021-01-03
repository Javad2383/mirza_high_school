from django.shortcuts import render
from .models import Gallery_Main, Gallery_Detail


def Gallery_List(request):
    gallery = Gallery_Main.objects.all()
    context = {
        "gallery": gallery
    }
    return render(request, "Gallery/gallery_list.html", context)


def Gallery_Detail_Def(request, pk):
    gallery_image = Gallery_Detail.objects.filter(image_group_id=pk)
    context = {
        "images": gallery_image
    }
    return render(request, "Gallery/gallery-detail.html", context)
