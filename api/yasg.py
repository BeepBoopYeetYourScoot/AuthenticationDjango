from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Basic authentication API',
        default_version='v1',
        description='Continuation of test project',
        license=openapi.License(name='Alabuga SDD')
    )
)

urlpatterns = [
    path('documentation/', schema_view.with_ui('swagger'), name='documentation')
]
