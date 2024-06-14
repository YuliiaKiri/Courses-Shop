from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


# Create your models here.


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        excludes = ['created_at']
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()
        # fields = ['category_id', 'category', 'title',
        #           'category', 'price', 'students_qty']

    def hydrate(self, bundle):  # данные от клиента серверу
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    def dehydrate(self, bundle):  # ответ от сервера - клиенту
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        bundle.data['title'] = bundle.obj.title.upper()
        bundle.data['price'] = bundle.obj.price
        bundle.data['students_qty'] = bundle.obj.students_qty
        return bundle

    # def dehydrate(self, bundle):
    #     return bundle.data['title'].upper()
