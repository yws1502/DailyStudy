from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('users.urls')),
]

# 임시적으로 웹페이지에 이미지파일을 보고싶을 때 적용한다.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)