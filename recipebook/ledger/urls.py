# <appname>/urls.py
from django.contrib import admin
from django.urls import include, path

from recipebook.ledger import views

urlpatterns = [
    path('ledger/', include('ledger.urls', namespace="ledger")),
    path('recipe/1/', views.recipe1, name='recipe1'),
    path('recipe/2/', views.recipe2, name='recipe2'),
    path('admin/', admin.site.urls),
]
# This might be needed, depending on your Django version
app_name = "ledger"

