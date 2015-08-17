import sys
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()

#  Update the users in this list.
#  Each tuple represents the username, password, and email of a user.
users = [
    (   "user121"   ,   "cezGdMrQB3"    ,   "carrie@ttbutton.com"   ,   )   ,
(   "user122"   ,   "JVVkmaHG4K"    ,   "dorothycmy@yahoo.com.hk"   ,   )   ,
(   "user123"   ,   "g8120934"  ,   ""  ,   )   ,
(   "user124"   ,   "r079655"   ,   ""  ,   )   ,
(   "user125"   ,   "qmm77APzAn"    ,   "kk_phet@yahoo.com.hk"  ,   )   ,
(   "user126"   ,   "p1749041"  ,   ""  ,   )   ,
(   "user128"   ,   "QsA5Bj2Xf4"    ,   "bbqbbq33@ymail.com"    ,   )   ,
(   "user130"   ,   "e793051"   ,   ""  ,   )   ,
(   "user131"   ,   "e7236216"  ,   ""  ,   )   ,
(   "user132"   ,   "wQl4FKpNEM"    ,   "shumchuiyan@yahoo.com.hk"  ,   )   ,
(   "user133"   ,   "g531916"   ,   ""  ,   )   ,
(   "user134"   ,   "anrbFie5TX"    ,   "mahauling1210@gmail.com"   ,   )   ,
(   "user135"   ,   "ymRd9WQZ6c"    ,   "marina@live.hk"    ,   )   ,
(   "user136"   ,   "r3646776"  ,   ""  ,   )   ,
(   "user137"   ,   "g6720764"  ,   ""  ,   )   ,
(   "user138"   ,   "VxuvxEamrR"    ,   "ewmfong@yahoo.com" ,   )   ,
(   "user139"   ,   "cd8QV8jmkU"    ,   ""  ,   )   ,
(   "user140"   ,   "c491950"   ,   ""  ,   )   ,
(   "user141"   ,   "d425900a"  ,   ""  ,   )   ,
(   "user142"   ,   "g2219912"  ,   ""  ,   )   ,
(   "user143"   ,   "h3751173"  ,   ""  ,   )   ,
(   "user144"   ,   "p4483786"  ,   ""  ,   )   ,
(   "user145"   ,   "y9144208"  ,   ""  ,   )   ,
(   "user146"   ,   "y8648245"  ,   ""  ,   )   ,
(   "user208"   ,   "g6314391"  ,   ""  ,   )   ,
(   "user209"   ,   "k0812374"  ,   ""  ,   )   ,
(   "user210"   ,   "c6323853"  ,   ""  ,   )   ,
(   "user211"   ,   "r387311a"  ,   ""  ,   )   ,
(   "user212"   ,   "pPYcbcPnuY"    ,   "seliasze6101@hotmail.com"  ,   )   ,
(   "user213"   ,   "k2936828"  ,   ""  ,   )   ,
(   "user214"   ,   "g5053276"  ,   ""  ,   )   ,
(   "user215"   ,   "p0677837"  ,   ""  ,   )   ,
(   "user216"   ,   "p9949538"  ,   ""  ,   )   ,
(   "user217"   ,   "L1plFVgSxv"    ,   ""  ,   )   ,
(   "user218"   ,   "r6741044"  ,   ""  ,   )   ,
(   "user219"   ,   "cc6UafagiQ"    ,   "wfai70@yahoo.com"  ,   )   ,
(   "user220"   ,   "r0966893"  ,   ""  ,   )   ,
(   "user221"   ,   "g6272028"  ,   ""  ,   )   ,

]

for username, password, email in users:
    try:
        print 'Creating user {0}.'.format(username)
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()

        assert authenticate(username=username, password=password)
        print 'User {0} successfully created.'.format(username)

    except:
        print 'There was a problem creating the user: {0}.  Error: {1}.' \
            .format(username, sys.exc_info()[1])