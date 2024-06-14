from django.contrib import admin
from shop.models import Category, Course

# Register your models here.

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to the Courses area"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')


# класс для отражения курсов на стр категорий:
class CoursesInLine(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [CoursesInLine]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
