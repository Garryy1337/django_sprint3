from django.contrib import admin
from django.urls import include, path
import debug_toolbar


urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]