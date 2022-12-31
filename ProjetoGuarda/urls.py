from django.contrib import admin
from django.urls import path
from Show        import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    # CRUD Mídia
    path('createMidia', views.createMidia, name="cMidia"),
    path('updateMidia/<int:id_midia>', views.updateMidia, name="uMidia"),
    path('deleteMidia/<int:id_midia>', views.deleteMidia, name="dMidia"),
    # CRUD Gênero
    path('createGenero', views.createGenero, name="cGenero"),
    path('updateGenero/<int:id_genero>', views.updateGenero, name="uGenero"),
    path('deleteGenero/<int:id_genero>', views.deleteGenero, name="dGenero"),
    # CRUD Produção
    path('createObra', views.createObra, name="cObra"),
    path('updateObra/<int:id_Obra>', views.updateObra, name="uObra"),
    path('deleteObra/<int:id_Obra>', views.deleteObra, name="dObra"),
    # CRUD Gênero da Obra
    path('createGenero_da_Obra', views.createGenero_da_Obra, name="cGenero_da_Obra"),
    path('updateGenero_da_Obra/<int:id_Genero_da_Obra>', views.updateGenero_da_Obra, name="uGenero_da_Obra"),
    path('deleteGenero_da_Obra/<int:id_Genero_da_Obra>', views.deleteGenero_da_Obra, name="dGenero_da_Obra"),
    # CRUD Funcionário
    path('createFuncionario', views.createFuncionario, name="cFuncionario"),
    path('updateFuncionario/<int:id_Funcionario>', views.updateFuncionario, name="uFuncionario"),
    path('deleteFuncionario/<int:id_Funcionario>', views.deleteFuncionario, name="dFuncionario"),
    # CRUD Função
    path('createFuncao', views.createFuncao, name="cFuncao"),
    path('updateFuncao/<int:id_Funcao>', views.updateFuncao, name="uFuncao"),
    path('deleteFuncao/<int:id_Funcao>', views.deleteFuncao, name="dFuncao"),
    # CRUD Produção
    path('createProducao', views.createProducao, name="cProducao"),
    path('updateProducao/<int:id_Producao>', views.updateProducao, name="uProducao"),
    path('deleteProducao/<int:id_Producao>', views.deleteProducao, name="dProducao"),
]
