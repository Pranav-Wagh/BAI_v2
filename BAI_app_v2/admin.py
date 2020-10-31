from django.contrib import admin
from BAI_app_v2.models import ParticipantInfo, Speed, SafetynWellfare, Others, Economy

# Register your models here.
admin.site.register(ParticipantInfo)
admin.site.register(Speed)

admin.site.register(SafetynWellfare)
admin.site.register(Others)
admin.site.register(Economy)