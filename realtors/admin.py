from django.contrib import admin
from .models import Realtor
# Register your models here.
# Now lets create a class about how to showed the table data on admin page
class RealtorsAdminTable(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 25



# Now register the Listing app to the admin site
admin.site.register(Realtor,RealtorsAdminTable)