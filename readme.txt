為什麼用pipenv

0.pipenv，不需要再分別使用 pip 跟virtualenv 。
1.自動產生與更新Pipfile and Pipfile.lock 解決了維護 requirements.txt 的問題。
2.透過套件的 Hash 安全性檢查確認 （當安裝套件 hash 值不同時，跳出錯誤，防止惡意套件侵入）
3.可以透過.env 自動載入不同環境變數。
4.相較 pip 是按順序安裝， pipenv 是使用並行（parallel）同步安裝套件，能夠提升安裝套件的速度，且Pipfile預設也區分了 development 與 production 環境。

$ pip3 install pipenv
$ pipenv shell
Pipenv 會自動產生一個 Pipfile，用來記錄所安裝的套件。

------------------MTV-設計概念------------------------------------
Django 的設計模式，也就是 MTV
Model : 定義一些資料庫的東西 ( ORM )，這層通常是直接和資料有關。

Template : 使用者基本上就是看到這層，也就是最後所呈現的 Template ( html )。

View : 可以將這層看做是中間層，它主要負責 Model 和 Template 之間的業務邏輯。
------------------------------------------------------------------

開始 <說明> 不用複製
1.安裝django
$ pipenv install django djangorestframework django-rest-knox<django rest auth 的驗證模組>
如果遇到locking failed  參考:https://towardsdatascience.com/common-errors-and-how-to-solve-them-why-wont-it-lock-8f5e57111f23
通常是模組名稱錯誤

建立 Django Project
$ django-admin startproject manager
會看到manager資料夾
測試server:
$ python manage.py runserver 

建立 Django App
先建立一個觀念，在 Django 中，通常我們會依照 "功能" 去建立 App ， 例如 musics ，代表他是 管理音樂 的部份。
$ python manage.py startapp leads
可以在manager下面看到leads資料夾
建立完請記得要將 App 加入設定檔
到manager >> settings.py 裡面的 INSTALLED_APPS 加入 leads (也就是你自己建立的 App 名稱) 和rest_framwork

預設的資料庫為sqlite3 可以到setting 下的 DATABASES 看到。

定義出資料庫中的結構（schema），並且透過 Django 中的指令去建立資料庫。

到leads >> models.py 建立(資料自動儲存設定)
------------------------------------------------------------------
class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
------------------------------------------------------------------
default : 代表默認值，也就是如果你沒有指定的話會用默認值。
auto_now_add : 新增時會幚你自動加上建立時間。
auto_now : 資料有更新時會幚你自動加上更新的時間。
更多可以參考 Django fields


Django REST序列化器
什麼是Django REST序列化器？序列化是將對象轉換為另一種數據格式的動作。轉換對像後，我們可以將其保存到文件或通過網絡發送。
為什麼需要序列化？考慮一下Django模型：他是Python類。
使用Django REST序列化，將python類別的檔案轉成json發送給瀏覽器
在leads底下建立一個serializers.py檔
內容:
------------------------------------------------------------------
from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
------------------------------------------------------------------

建立veiwset api，在leads底下建立api.py
內容:
------------------------------------------------------------------
from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

class LeadViewSet(viewssets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
------------------------------------------------------------------

建立urls配對
在manage底下urls.py
內容:
------------------------------------------------------------------
from django.urls import path, include

urlpatterns = [
    path('', include('leads.urls')),
]
------------------------------------------------------------------
接下來
到leads建立url.py
內容:
------------------------------------------------------------------
from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter
router.register('api/leads',LeadViewSet,'leads')

urlpatterns =router.urls
------------------------------------------------------------------
這樣就建立好了一個基本的註冊流程api