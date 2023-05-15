from django.urls import path
from ecmsapp import views
from .Code import Accounts,Cleaning,Enviroments,Houses,Logs,Payments,Renter,Transactions


urlpatterns = [
    path('', views.user_login, name='user_login'),
    path("logout_view/",Accounts.logout_view, name="logout_view"),
    path('index/', views.index, name='index'),

    path('adduser/', Accounts.addUser, name='adduser'),
    path('activeAccount/', Accounts.activeAccount, name='activeAccount'),
    path('disableAccount/', Accounts.disableAccount, name='disableAccount'),
    path("myprofile/",Accounts.myprofile, name="myprofile"),    
    path("changepassword/",Accounts.changepassword, name="changepassword"),
    path('Empolyee/', Accounts.staffs, name='Empolyee'),

    path('fetch_data/',Houses.fetch_data, name='fetch_data'),


    #region Environment

    path('house/', Houses.house, name='house'),
    path('createHouse/', Houses.createHouse, name='createHouse'),
    path('updateHouse/', Houses.update_house, name='updateHouse'),
    path('deleteHouse/', Houses.delete_house, name='deleteHouse'),




    path('Renter/', Renter.renter, name='Renter'),
    path('createRenter/', Renter.createRenter, name='createRenter'),
    path('updateRenter/', Renter.update_renter, name='updateRenter'),
    path('deleteRenter/', Renter.delete_renter, name='deleteRenter'),


    path('Enviroment/', Enviroments.enviroment, name='Enviroment'),
    path('createEnviroment/', Enviroments.createEnviroment, name='createEnviroment'),
    path('getEnviroment/', Enviroments.get_environment, name='getEnviroment'),

    #endregion





    path('cleaning/', Cleaning.cleaning, name='cleaning'),
    
    path('Transaction/', Transactions.transaction, name='Transaction'),
    path('makepayment/', Transactions.makePayment, name='makepayment'),





    # path('reports/', Logs.reports, name='reports'),
    path('Payment_Method/', Payments.Payment_Method, name='Payment_Method'),
    path('auditlogs/', Logs.AuditLogs, name='auditlogs'),
]