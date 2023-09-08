import uuid
from django.contrib import admin
from rentstate.models import RentState


class RentStateAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner',  'title', 'description',
                    'max_size', 'status', 'invitation_code')
    search_fields = ('title', 'description')
    readonly_fields = ('invitation_code', 'max_size')
    fieldsets = (
        ('Group', {
            'fields': ('title', 'description', 'max_size',
                       'status', 'invitation_code')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
            obj.invitation_code = str(uuid.uuid4())[:6].upper()
        return super().save_model(request, obj, form, change)


admin.site.register(RentState, RentStateAdmin)
