"""
URL configuration for vermillion_player project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from graphql_jwt.middleware import JSONWebTokenMiddleware

from graphene_django.views import GraphQLView

class CustomGraphQLView(GraphQLView):
    def get_context(self, request):
        print("AUTH HEADER:", request.headers.get("Authorization"))
        return request

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", csrf_exempt(
        CustomGraphQLView.as_view(
            graphiql=True,
            middleware=[JSONWebTokenMiddleware()]
            )
        )
    ),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = 'Vermilion Player'
admin.site.site_header = 'Vermillion Player'
admin.site.index_title = 'Panel de adminsitración'
