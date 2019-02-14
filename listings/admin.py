from django.contrib import admin


from .models import Listing
# Register your models here.
# Now register the Listing app to the admin site

class ListingAdminTable(admin.ModelAdmin):
    # Now define the property about how they should displayed
    list_display = ('id','title','is_published','price','list_date','realtors')
    list_display_links = ('id','title')
    list_filter = ('realtors',)
    list_editable = ('is_published',)
    search_fields = ('title','description','address','city','state',
                     'zipcode','price')
    list_per_page = 25


admin.site.register(Listing,ListingAdminTable)