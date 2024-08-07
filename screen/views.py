from django.shortcuts import HttpResponse    
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView
from django.urls import reverse
from rest_framework import status
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .serializers import *
from .forms import *
from rest_framework.exceptions import NotAuthenticated
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer

# Create your views here.

class ScreenTypeCreateListAPIView(APIView):
    # permission_classes = (IsAuthenticated,)
    template_name = 'screen_type.html'
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]

    def get(self, request, format=None):
        screens = ScreenType.objects.all()
        serializer = ScreenTypeSerializer(screens, many=True)
        return Response({"screens":serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = ScreenTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ScreenTypeDetailAPIView(APIView):
    # permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'update_screen_type.html'

    def get_object(self, pk):
        print("----------------------------------------",pk)
        try:
            return ScreenType.objects.get(pk=pk)
        except ScreenType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        screen = self.get_object(pk)
        serializer = ScreenTypeSerializer(screen)
        print(serializer.data)
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        screen = self.get_object(pk)
        serializer = ScreenTypeSerializer(screen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        screen = self.get_object(pk)
        screen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
class AreaListCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

        
    def get(self, request, format=None):
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    
    def post(self, request, format=None):
        serializer = AreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AreaDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Area.objects.get(pk=pk)
        except Area.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, pk, format=None):
        area = self.get_object(pk)
        serializer = AreaSerializer(area)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        area = self.get_object(pk)
        serializer = AreaSerializer(area, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        area = self.get_object(pk)
        area.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

class CategoryListCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   

class SubCategoryListCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        subcategories = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubCategoryDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return SubCategory.objects.get(pk=pk)
        except SubCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        subcategory = self.get_object(pk)
        serializer = SubCategorySerializer(subcategory)
        return Response(serializer.data, status=status.HTTP_200_OK)
   

    def put(self, request, pk, format=None):    
        subcategory = self.get_object(pk)
        serializer = SubCategorySerializer(subcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subcategory = self.get_object(pk)
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TShirtSizeListCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        tshirt_sizes = TShirtSize.objects.all()
        serializer = TShirtSizeSerializer(tshirt_sizes, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = TShirtSizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TShirtSizeDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return TShirtSize.objects.get(pk=pk)    
        except TShirtSize.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
       
        tshirt_size = self.get_object(pk)
        serializer = TShirtSizeSerializer(tshirt_size)  
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        tshirt_size = self.get_object(pk)
        serializer = TShirtSizeSerializer(tshirt_size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None): 
        tshirt_size = self.get_object(pk)
        tshirt_size.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CatalogListCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        catalogs = Catalog.objects.all()
        serializer = CatalogSerializer(catalogs, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = CatalogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CatalogDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Catalog.objects.get(pk=pk)    
        except Catalog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        catalog = self.get_object(pk)
        serializer = CatalogSerializer(catalog)  
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        catalog = self.get_object(pk)    
        serializer = CatalogSerializer(catalog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None): 
        catalog = self.get_object(pk)
        catalog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def screen_type_list(request):
    screen_types = ScreenType.objects.all()
    return render(request, 'screen_type_list.html', {'screen_types': screen_types})

def screen_type_detail(request, pk):
    screen_type = get_object_or_404(ScreenType, pk=pk)
    return render(request, 'screen_type_detail.html', {'screen_type': screen_type})

def screen_type_create(request):
    if request.method == 'POST':
        form = ScreenTypeForm(request.POST)
        if form.is_valid():
            screen_type = form.save()
            return redirect('screen_type_list', {'screen_type': screen_type})
    else:
        form = ScreenTypeForm()
    return render(request, 'screen_type_form.html', {'form': form})

def screen_type_update(request, pk):
    screen_type = get_object_or_404(ScreenType, pk=pk)
    if request.method == 'POST':
        form = ScreenTypeForm(request.POST, instance=screen_type)
        if form.is_valid():
            screen_type = form.save()
            return redirect('screen_type_detail', pk=screen_type.pk)
    else:
        form = ScreenTypeForm(instance=screen_type)
    return render(request, 'screen_type_form.html', {'form': form})

def screen_type_delete(request, pk):
    screen_type = get_object_or_404(ScreenType, pk=pk)
    if request.method == 'POST':
        screen_type.delete()
        return redirect('screen_type_list')
    return render(request, 'screen_type_confirm_delete.html', {'screen_type': screen_type})


# List all areas
def area_list(request):
    areas = Area.objects.all()
    return render(request, 'area_list.html', {'areas': areas})

# View details of a specific area
def area_detail(request, pk):
    area = get_object_or_404(Area, pk=pk)
    return render(request, 'area_detail.html', {'area': area})

# Create a new area
def area_create(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            area = form.save()  # Save the form data to create a new Area object
            return redirect(reverse('area_list', {'area': area}))  # Redirect to the detail view of the created area
    else:
        form = AreaForm()
    
    return render(request, 'area_create.html', {'form': form})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})



def subcategory_list(request):
    subcategories = SubCategory.objects.all()
    return render(request, 'subcategory_list.html', {'subcategories': subcategories})

def subcategory_create(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subcategory-list')
    else:
        form = SubCategoryForm()
    return render(request, 'subcategory_form.html', {'form': form})

def tshirtsize_list(request):
    sizes = TShirtSize.objects.all()
    return render(request, 'tshirtsize_list.html', {'sizes': sizes})

def tshirtsize_create(request):
    if request.method == 'POST':
        form = TShirtSizeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tshirtsize-list')
    else:
        form = TShirtSizeForm()
    return render(request, 'tshirtsize_form.html', {'form': form})

def enquiry_list(request):
    enquiries = Enquiry.objects.all()
    return render(request, 'enquiry_list.html', {'enquiries': enquiries})

def enquiry_create(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enquiry-list')
    else:
        form = EnquiryForm()
    return render(request, 'enquiry_form.html', {'form': form})

def catalog_list(request):
    catalogs = Catalog.objects.all()
    return render(request, 'catalog_list.html', {'catalogs': catalogs})

def catalog_create(request):
    if request.method == 'POST':
        form = CatalogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog-list')
    else:
        form = CatalogForm()
    return render(request, 'catalog_form.html', {'form': form})

