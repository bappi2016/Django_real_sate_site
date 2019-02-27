from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdminTable(admin.ModelAdmin):

    list_display = ('id','name','listing','email','contact_date')
    list_display_links = ('id','name')
    list_per_page =25
    search_fields = ('name','email','listing')




admin.site.register(Contact, ContactAdminTable)