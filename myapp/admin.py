from django.contrib import admin

from myapp.models import Topic, SubTopic, Member, Student, Receipt


class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('id', 'name')


class ReceiptAdmin(admin.ModelAdmin):
    model = Receipt
    list_display = ('id', 'number')


admin.site.register(Topic)
admin.site.register(SubTopic)
admin.site.register(Member)
admin.site.register(Student, StudentAdmin)
admin.site.register(Receipt, ReceiptAdmin)
