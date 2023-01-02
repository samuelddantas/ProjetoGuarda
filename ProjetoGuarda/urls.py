from django.contrib import admin
from django.urls    import path
from Show           import views as viewShow
from User           import views as viewUser

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('login/', viewUser.loginUser, name="login"),
    path('logout/', viewUser.logoutUser, name="logout"),
    path('register/', viewUser.registerUser, name="register"),
    # Páginas de Acesso
    path('', viewShow.index, name="main"),
    # CRUD Mídia
    path('createMidia', viewShow.createMidia, name="cMidia"),
    path('updateMidia/<int:id_midia>', viewShow.updateMidia, name="uMidia"),
    path('deleteMidia/<int:id_midia>', viewShow.deleteMidia, name="dMidia"),
    # CRUD Gênero
    path('createGenero', viewShow.createGenero, name="cGenero"),
    path('updateGenero/<int:id_genero>', viewShow.updateGenero, name="uGenero"),
    path('deleteGenero/<int:id_genero>', viewShow.deleteGenero, name="dGenero"),
    # CRUD Produção
    path('createObra', viewShow.createObra, name="cObra"),
    path('updateObra/<int:id_Obra>', viewShow.updateObra, name="uObra"),
    path('deleteObra/<int:id_Obra>', viewShow.deleteObra, name="dObra"),
    # CRUD Gênero da Obra
    path('createGenero_da_Obra', viewShow.createGenero_da_Obra, name="cGenero_da_Obra"),
    path('updateGenero_da_Obra/<int:id_Genero_da_Obra>', viewShow.updateGenero_da_Obra, name="uGenero_da_Obra"),
    path('deleteGenero_da_Obra/<int:id_Genero_da_Obra>', viewShow.deleteGenero_da_Obra, name="dGenero_da_Obra"),
    # CRUD Funcionário
    path('createFuncionario', viewShow.createFuncionario, name="cFuncionario"),
    path('updateFuncionario/<int:id_Funcionario>', viewShow.updateFuncionario, name="uFuncionario"),
    path('deleteFuncionario/<int:id_Funcionario>', viewShow.deleteFuncionario, name="dFuncionario"),
    # CRUD Função
    path('createFuncao', viewShow.createFuncao, name="cFuncao"),
    path('updateFuncao/<int:id_Funcao>', viewShow.updateFuncao, name="uFuncao"),
    path('deleteFuncao/<int:id_Funcao>', viewShow.deleteFuncao, name="dFuncao"),
    # CRUD Produção
    path('createProducao', viewShow.createProducao, name="cProducao"),
    path('updateProducao/<int:id_Producao>', viewShow.updateProducao, name="uProducao"),
    path('deleteProducao/<int:id_Producao>', viewShow.deleteProducao, name="dProducao"),
    # CRUD Assistido
    path('createAssistido', viewUser.createAssistido, name="cAssistido"),
    path('updateAssistido/<int:id_Assistido>', viewUser.updateAssistido, name="uAssistido"),
    path('deleteAssistido/<int:id_Assistido>', viewUser.deleteAssistido, name="dAssistido"),
    # CRUD Produção
    path('createReview', viewUser.createReview, name="cReview"),
    path('updateReview/<int:id_Review>', viewUser.updateReview, name="uReview"),
    path('deleteReview/<int:id_Review>', viewUser.deleteReview, name="dReview"),
]
