"""twitter_search URL Configuration

The `urlpatterns` list routes URLs to templates. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function templates
    1. Add an import:  from my_app import templates
    2. Add a URL to urlpatterns:  path('', templates.home, name='home')
Class-based templates
    1. Add an import:  from other_app.templates import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#
from controller import controller

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', controller.test, name="Hello World !!"),
    path('search', controller.search, name="Hello"),
    path('stemmed_document', controller.stemmed_document, name="stemmed_document"),
    path('raw_document', controller.raw_document, name="raw_document"),
    path('relevant_tweet', controller.relevant_data, name="relevant_tweet"),
    path('irrelavant_tweet', controller.irelevant_data, name="irelevant_data"),

]
urlpatterns += staticfiles_urlpatterns()

