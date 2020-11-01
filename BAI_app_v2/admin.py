from django.contrib import admin
from BAI_app_v2.models import ParticipantInfo, Speed, SafetynWellfare, Others, Economy, Project_info, Quality

# Register your models here.
admin.site.register(ParticipantInfo)
admin.site.register(Speed)

admin.site.register(SafetynWellfare)
admin.site.register(Others)
admin.site.register(Economy)

admin.site.register(Project_info)
admin.site.register(Quality)