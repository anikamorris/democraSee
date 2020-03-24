"""democraSee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from candidates.views import IndexView

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    #Quiz app
    path('quiz/', include('quiz.urls')),

    # Candidates app
    path('candidates/', include('candidates.urls')),

     # Authentication
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    # Home page
    path('', IndexView.as_view(), name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
