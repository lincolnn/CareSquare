from django.contrib import admin
from checkin.models import CareCoordinator, Member, Checkin

class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('member',)}
    list_display = ('lastname', 'firstname', 'rating')
    search_fields = ['lastname']

class CareCoordinatorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('firstname',)}

class CheckinAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('member',)}

admin.site.register(CareCoordinator)
admin.site.register(Member, CheckinAdmin)
admin.site.register(Checkin)
