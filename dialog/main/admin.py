from django.contrib import admin
from .models import Device, DeviceModel


class DeviceAdmin(admin.ModelAdmin):
    fields = ['address', 'name', 'ip_address', 'author', 'device_model', 'comments']
    list_display = ['name', 'ip_address', 'author', 'device_model']

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "address":
            kwargs['widget'] = YourCustomAddressWidget()  # Вам нужно создать виджет для работы с DaData.
        return super().formfield_for_dbfield(db_field, request, **kwargs)


admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceModel)
