from django import forms
from .models import *

class ScreenTypeForm(forms.ModelForm):
    class Meta:
        model = ScreenType
        fields = ['name', 'description', 'status']


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'description', 'location', 'latitude', 'longitude', 'status']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'status']
        labels = {
            'name': 'Category Name',
            'description': 'Category Description',
            'status': 'Status'
        }

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'description', 'category', 'status']
        labels = {
            'name': 'Subcategory Name',
            'description': 'Subcategory Description',
            'category': 'Category',
            'status': 'Status'
        }

class TShirtSizeForm(forms.ModelForm):
    class Meta:
        model = TShirtSize
        fields = ['name', 'description', 'status']
        labels = {
            'name': 'T-Shirt Size Name',
            'description': 'T-Shirt Size Description',
            'status': 'Status'
        }

class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ['category', 'subcategory', 'reference_id', 'description', 'marketing_description',
                  'screen_type', 'size', 'area', 'location', 'landmark', 'avg_monthly_price',
                  'hide_price_to_buyer', 'tshirt_size', 'vender', 'gps_latitude', 'gps_longitude',
                  'thumbnail', 'image1', 'image2', 'image3', 'available_from', 'available_to',
                  'visibility', 'illumination', 'benefits_and_cta', 'average_weekly_impressions']
        labels = {
            'reference_id': 'Reference ID',
            'description': 'Description',
            'marketing_description': 'Marketing Description',
            'screen_type': 'Screen Type',
            'size': 'Size',
            'area': 'Area',
            'location': 'Location',
            'landmark': 'Landmark',
            'avg_monthly_price': 'Average Monthly Price',
            'hide_price_to_buyer': 'Hide Price to Buyer',
            'tshirt_size': 'T-Shirt Size',
            'vender': 'Vendor',
            'gps_latitude': 'GPS Latitude',
            'gps_longitude': 'GPS Longitude',
            'thumbnail': 'Thumbnail',
            'image1': 'Image 1',
            'image2': 'Image 2',
            'image3': 'Image 3',
            'available_from': 'Available From',
            'available_to': 'Available To',
            'visibility': 'Visibility',
            'illumination': 'Illumination',
            'benefits_and_cta': 'Benefits and Call to Action',
            'average_weekly_impressions': 'Average Weekly Impressions'
        }

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['subject', 'message', 'vender', 'closed', 'closed_date', 'comments']
        labels = {
            'subject': 'Subject',
            'message': 'Message',
            'vender': 'Vendor',
            'closed': 'Closed',
            'closed_date': 'Closed Date',
            'comments': 'Comments'
        }