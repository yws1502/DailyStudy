from os import name
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('users.urls')),
    path('study_groups/', include('study_groups.urls')),

    path('reset_password/', auth_views.PasswordResetView.\
        as_view(template_name='reset_password.html'), name='reset_password',),
    
    path('reset_password_sent/', auth_views.PasswordResetDoneView.\
        as_view(template_name='reset_password_sent.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.\
        as_view(template_name='reset.html'), name='password_reset_confirm'),
    
    path('reset_password_complate/', auth_views.PasswordResetCompleteView.\
        as_view(template_name='reset_password_complete.html'), name='password_reset_complete'),
    
]

# 임시적으로 웹페이지에 이미지파일을 보고싶을 때 적용한다.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)