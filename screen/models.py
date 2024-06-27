from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ]

class Area(models.Model):
    name = models.CharField(_('area name'), max_length=255, unique=True)
    description = models.TextField(_('area description'), blank=True, null=True)
    location = models.CharField(_('area location'), max_length=255, null=True, blank=True)
    latitude = models.CharField(_('latitude'), max_length=255, null=True, blank=True)
    longitude = models.CharField(_('longitude'), max_length=255, null=True, blank=True)
    status = models.CharField(_('status'), max_length=10, choices=STATUS_CHOICES, default='active')
    created_on = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_on = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('area')    
        verbose_name_plural = _('areas')
        ordering = ['-created_on']

class Category(models.Model):
    name = models.CharField(_('category name'), max_length=255, unique=True)
    description = models.TextField( _('category description'), blank=True, null=True)
    status = models.CharField(_('status'), max_length=10, choices=STATUS_CHOICES, default='active')
    created_on = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_on = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['-created_on']

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(_('subcategory name'), max_length=255, unique=True)
    description = models.TextField( _('subcategory description'), blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(_('status'), max_length=10, choices=STATUS_CHOICES, default='active')
    created_on = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_on = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'
        ordering = ['-created_on']

    def __str__(self):
        return self.name    

class ScreenType(models.Model):
    name = models.CharField(_('screen type name'), max_length=100, unique=True)
    description = models.TextField( _('screen type description'), blank=True, null=True)
    status = models.CharField(_('status'), max_length=10, choices=STATUS_CHOICES, default='active')
    created_on = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_on = models.DateTimeField(_('updated at'), auto_now=True)


    class Meta:
        verbose_name = 'screen type'
        verbose_name_plural = 'screen types'
        ordering = ['-created_on']

    def __str__(self):
        return self.name
    
class TShirtSize(models.Model):
    name = models.CharField(_('t-shirt size name'), max_length=100, unique=True)
    description = models.TextField( _('t-shirt size description'), blank=True, null=True)
    status = models.CharField(_('status'), max_length=10, choices=STATUS_CHOICES, default='active')
    created_on = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_on = models.DateTimeField(_('updated at'), auto_now=True)


    class Meta:
        verbose_name = 't-shirt size'
        verbose_name_plural = 't-shirt sizes'
        ordering = ['-created_on']

    def __str__(self):
        return self.name
    

class Catalog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,null=True,blank=True)
    reference_id = models.CharField(_('reference id'), max_length=50, blank=True, null=True)
    description = models.CharField(_( 'description'), max_length=50)
    marketing_description = models.TextField(_('marketing description'),max_length=500)
    screen_type = models.ForeignKey(ScreenType, on_delete=models.CASCADE)
    size = models.CharField(_('size'), max_length=20)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    location = models.CharField(_('location'), max_length=100)
    landmark = models.CharField(_('landmark'), max_length=200)
    avg_monthly_price = models.DecimalField(_('average monthly price'), max_digits=10, decimal_places=2)
    hide_price_to_buyer = models.BooleanField(_('hide price to buyer'), default=False)
    tshirt_size = models.ForeignKey(TShirtSize, on_delete=models.CASCADE)
    vender = models.CharField(max_length=100,blank=True, null=True)
    gps_latitude = models.DecimalField(_('gps latitude'), max_digits=9, decimal_places=6)
    gps_longitude = models.DecimalField(_('gps longitude'), max_digits=9, decimal_places=6)
    thumbnail = models.ImageField(_('thumbnail'),upload_to='thumbnails/',blank=True, null=True)
    image1 = models.ImageField(upload_to='images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    available_from = models.DateField(_('available from'),blank=True, null=True)
    available_to = models.DateField(_('available to'),blank=True, null=True)
    visibility = models.CharField(max_length=50,blank=True, null=True)
    illumination = models.CharField(max_length=50,blank=True, null=True)
    benefits_and_cta = models.CharField(max_length=200,blank=True, null=True)
    average_weekly_impressions = models.CharField(max_length=50,blank=True, null=True)



    class Meta:
        verbose_name = 'catalog'
        verbose_name_plural = 'catalogs'

    def __str__(self):
        return self.category
    
class Enquiry(models.Model):
    subject = models.CharField(_('subject'), max_length=255,blank=True, null=True)
    message = models.TextField(_('message'), blank=True, null=True)
    vender = models.CharField(max_length=100,blank=True, null=True)
    received_date = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'
        ordering = ['-received_date']
