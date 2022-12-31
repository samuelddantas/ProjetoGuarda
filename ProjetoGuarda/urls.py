from django.contrib import admin
from django.urls import path
from Show        import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    # CRUD MIDIA
    path('createMidia', views.createMidia, name="cMidia"),
    path('updateMidia/<int:id_midia>', views.updateMidia, name="uMidia"),
    path('deleteMidia/<int:id_midia>', views.deleteMidia, name="dMidia"),
    # CRUD GÊNERO
    path('createGenero', views.createGenero, name="cGenero"),
    path('updateGenero/<int:id_genero>', views.updateGenero, name="uGenero"),
    path('deleteGenero/<int:id_genero>', views.deleteGenero, name="dGenero"),
    # CRUD OBRA
    path('createObra', views.createObra, name="cObra"),
    path('updateObra/<int:id_Obra>', views.updateObra, name="uObra"),
    path('deleteObra/<int:id_Obra>', views.deleteObra, name="dObra"),
]
