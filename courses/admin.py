from django.contrib import admin
from .models import Course, Enrollment, Content

# Admin class for the Course model
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'status')
    list_filter = ('status', 'instructor')
    search_fields = ('title', 'instructor__email')
    ordering = ('-created_at',)
    actions = ['approve_courses']

    def approve_courses(self, request, queryset):
        """Action to approve selected courses."""
        queryset.update(status='Approved')
    approve_courses.short_description = "Approve selected courses"

# Admin class for the Enrollment model
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    list_filter = ('course', 'student')
    search_fields = ('student__email', 'course__title')

# Admin class for the Content model
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'content_type', 'file')
    list_filter = ('course', 'content_type')
    search_fields = ('title', 'course__title')

# Register the models and their respective admin classes
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Content, ContentAdmin)
