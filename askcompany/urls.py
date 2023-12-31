from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView,RedirectView
from django.contrib.auth.decorators import login_required
from django_pydenticon.views import image as pydenticon_image


urlpatterns = [
    path('admin/', admin.site.urls),
    path('identicon/image/<path:data>/', pydenticon_image, name='pydenticon_image'),
    # path('', login_required(TemplateView.as_view(template_name='root.html')), name='root'),
    path('accounts/', include('accounts.urls')),
    path('instagram/', include('instagram.urls')),
    path('', RedirectView.as_view(pattern_name='instagram:index'), name='root'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns +=[
        path('__debug__/', include(debug_toolbar.urls)),
        
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)