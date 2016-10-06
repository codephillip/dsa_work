from django.contrib import admin

from myapp.models import Topic, SubTopic, Member

admin.site.register(Topic)
admin.site.register(SubTopic)
admin.site.register(Member)
