from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import blog.views

urlpatterns = [
    #path('erichua/secure/secure/secure/admin', admin.site.urls),
    #path("",jobs.views.home,name='home'),
    #path("blog/", include('blog.urls')),
    path("", blog.views.optimizewin10, name='home'),
    path("step_1", blog.views.step_1, name='step_1'),
    path("step_2", blog.views.step_2, name='step_2'),
    path("step_3", blog.views.step_3, name='step_3'),
    #path("win10optimize/step_4", blog.views.step_4, name='step_4'),
    #path("win10optimize/step_5", blog.views.step_5, name='step_5'),
    path("step3_1", blog.views.step3_1, name='step3_1'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
