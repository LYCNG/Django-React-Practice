建立前端應用frontend

$ django-admin startapp frontend

會看到frontend folder
在底下建立目錄並存放React components和靜態文件

$ mkdir -p .\frontend\src\components
$ mkdir -p .\frontend\{static,templates}\frontend

完成後到根目錄初始化環境>> npm init -y
現在安裝webpack tool
什麼是webpack?
那些EJS、Pug、Sass、ES6 等等的預處理器或需要編譯的內容，webpack 主要就是將他們轉換成瀏覽器看得懂的語言。
依照官網安裝 webpack 與 webpack-cli，至於這邊的 --save 是將套件儲存至 package.json，而 -dev 則是開發環境使用的意思。

$ npm i webpack webpack-cli --save-dev

並安裝babel套件和webpack一起使用

$npm i -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties

1.babel-loader ：webpack要去讀取任何檔案格式都需要靠loader這個工具去做判讀，然後再去做轉換，所以我們就會需要webpack掛載這個babel-loader。
2.@babel/core： 程式需要調用Babel的API進行編譯。
3.@babel/preset-env：可以使用最新版本的JavaScript然後去編譯，不用去理會哪些語法需要轉換。
然後安裝react

$ npm i react react-dom prop-types

安裝完後再跟目錄建立.babelrc檔案，他是Babel轉譯器
在.babelrc配置檔案中，主要是對預設（presets）和外掛（plugins）進行配置，因此不同的轉譯器作用不同的配置項，大致可分為以下三項：
1.語法轉義器。主要對javascript最新的語法糖進行編譯，並不負責轉譯javascript新增的api和全域性物件。
2.補丁轉義器。主要負責轉譯javascript新增的api和全域性物件，例如babel-plugin-transform-runtime這個外掛能夠編譯Object.assign,同時也可以引入babel-polyfill進一步對includes這類用法保證在瀏覽器的相容性。
3.jsx和flow外掛，這類轉譯器用來轉譯JSX語法和移除型別宣告的，使用Rect的時候你將用到它，轉譯器名稱為babel-preset-react
在.babelrc裡面:
建立預設(presets):
-----------------------------------------------------------------------------
{
  "presets":["@babel/preset-env","@babel/preset-react",
  "plugins":["transform-class-properties"]
}
-----------------------------------------------------------------------------
然後再跟目錄建立webpack.config.js
內容:
-----------------------------------------------------------------------------
module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};
-----------------------------------------------------------------------------
現在打開package.json並配置兩個腳本，一個用於生產，一個用於開發：
-----------------------------------------------------------------------------
"scripts": {
  "dev": "webpack --mode development ./manager/frontend/src/index.js --output ./manager/frontend/static/frontend/main.js",
  "build": "webpack --mode production ./manager/frontend/src/index.js --output ./manager/frontend/static/frontend/main.js"
}
-----------------------------------------------------------------------------
使用React的Django REST：準備前端應用
先到manager/frontend/src建立index.js
內容:
-----------------------------------------------------------------------------
import App from ./components/App
-----------------------------------------------------------------------------
再來到components建立App.js
內容:
-----------------------------------------------------------------------------
import React,{Component} from "react"
import ReactDOM from "react-dom"

class App extends Conponents {
  render(){
    return <h1>React App</h1>
  }
}

ReactDOM.render(<App />,document.getElementById('app'))
-----------------------------------------------------------------------------
然後到templates/frontend建立index.html
內容:
-----------------------------------------------------------------------------
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Django REST with React</title>
</head>
<body>
  <div id="app">
      <!-- React will load here -->
  </div>
  {% load static %}
  <script src="{% static "frontend/main.js" %}"></script>
</body>
</html>
-----------------------------------------------------------------------------
再來就配置css和js，可以到bootstrap去copy cdn到script src
然後到manager/setting.py裡面的installed_apps內增加frontend

接下來到/frontend/views.py設定:
-----------------------------------------------------------------------------
from django.shortcuts import render

def index(request):
    return render(request, 'frontend/index.html')
-----------------------------------------------------------------------------
接下來創建一個新文件/frontend/urls.py：
-----------------------------------------------------------------------------
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
]
-----------------------------------------------------------------------------
然後到manager底下的urls.py，在urlpatterns裡新增
-----------------------------------------------------------------------------
path('', include('frontend.urls'))
-----------------------------------------------------------------------------

此時，可以在http://127.0.0.1:8000/（仍在運行Django開發服務器上）上試一試。
currnet progress


https://www.youtube.com/watch?v=GieYIzvdt2U
