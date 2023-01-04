from django.contrib import admin
from django.urls    import path
from Show           import views as viewShow
from User           import views as viewUser

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    # Páginas de Registro
    path('login/', viewUser.loginUser, name="login"),
    path('logout/', viewUser.logoutUser, name="logout"),
    path('register/', viewUser.registerUser, name="register"),
    # Páginas de Acesso
    path('', viewShow.index, name="main"),
    # Update e Delete Usuário
    path('updateUser/<int:id_User>', viewUser.updateUser, name="uUser"),
    path('deleteUser/<int:id_User>', viewUser.deleteUser, name="dUser"),
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
    # CRUD Assistido
    path('createAssistido', viewUser.createAssistido, name="cAssistido"),
    path('updateAssistido/<int:id_Assistido>', viewUser.updateAssistido, name="uAssistido"),
    path('deleteAssistido/<int:id_Assistido>', viewUser.deleteAssistido, name="dAssistido"),
    # CRUD Produção
    path('createReview', viewUser.createReview, name="cReview"),
    path('updateReview/<int:id_Review>', viewUser.updateReview, name="uReview"),
    path('deleteReview/<int:id_Review>', viewUser.deleteReview, name="dReview"),
]
