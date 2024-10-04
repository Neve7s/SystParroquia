from django.contrib import admin
from django.urls import path

from webapp import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name="home"),

    # Login, Sigup and Logout
    path('loginapp/', views.loginapp, name="loginapp"),
    path('registerapp/', views.registerapp, name="registerapp"),
    path('logoutapp/', views.logoutapp, name="logoutapp"),

    # Confirmaciones
    path('confirmacion/', views.confirm, name="confirm"),
    path('addConfirm/', views.addConfirm, name="addConfirm"),
    path('printConfirm/<int:id>', views.printConfirm, name="printConfirm"),
    path('delConfirm/<int:id>', views.delConfirm, name="delConfirm"),
    path('listar_confirmacion/', views.listar_confirmacion, name='listar_confirmacion'),

    # Bautizos
    path('bautizo/', views.bautizo, name="bautizo"),
    path('addBautizo/', views.addBautizo, name="addBautizo"),
    path('printBautizo/<int:id>', views.printBautizo, name="printBautizo"),
    path('delBautizo/<int:id>', views.delBautizo, name="delBautizo"),
    path('listar_bautizos/', views.listar_bautizos, name='listar_bautizos'),

    # Matrimonios
    path('matrimonio/', views.matrimonio, name="matrimonio"),
    path('addMatrimonio/', views.addMatrimonio, name="addMatrimonio"),
    path('printMatrimonio/<int:id>', views.printMatrimonio, name="printMatrimonio"),
    path('delMatrimonio/<int:id>', views.delMatrimonio, name="delMatrimonio"),
    path('listar_matrimonios/', views.listar_matrimonios, name='listar_matrimonios'),

    # Primera Comunión
    path('pricomunion/', views.pricomunion, name="pricomunion"),
    path('addComunion/', views.addComunion, name="addComunion"),
    path('printComunion/<int:id>', views.printComunion, name="printComunion"),
    path('delComunion/<int:id>', views.delComunion, name="delComunion"),
    path('listar_comunion/', views.listar_comunion, name='listar_comunion'),

    path('otros/', views.otros, name="otros"),
    path('export_db/', views.export_db, name='export_db'),
]
