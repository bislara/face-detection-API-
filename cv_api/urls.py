from django.urls import path,include
from django.contrib import admin
from face_detector.views import detect

urlpatterns = [
    path('face_detection/detect/', detect),
    path('admin/', admin.site.urls),
]
# urlpatterns = patterns('',
#     # Examples:

#     url(r'^face_detection/detect/$', 'face_detector.views.detect'),

#     # url(r'^$', 'cv_api.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# )
