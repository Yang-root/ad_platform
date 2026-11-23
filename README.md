# 广告投放平台（Ad Platform）

软件工程课程第 5 组实验三工程骨架：把实验二的设计落成“能跑、能协作、可追溯”的开发舞台。

当前阶段只包含可运行的工程骨架与联调探针接口，业务功能从实验四开始开发。

## 技术栈

| 层次 | 技术 |
|---|---|
| 后端 | Python 3.13、Django 5.0、Django REST Framework 3.15 |
| 前端 | Node.js 24、Vue 3、Vite 5、Axios |
| 数据库 | MySQL 8.0（utf8mb4） |
| 跨域 | django-cors-headers |

## 目录结构

```
ad-platform/
├─ backend/                 Django 后端
│  ├─ adplatform/           项目配置（settings / urls / wsgi / asgi）
│  ├─ api/                  接口应用（当前提供 /api/hello）
│  ├─ manage.py
│  └─ .env                  本地数据库配置（不提交到仓库）
├─ frontend/                Vue 3 前端
│  ├─ src/                  页面、接口封装
│  ├─ index.html
│  └─ vite.config.mjs       开发服务器与 /api 代理配置
└─ .gitignore
```

## 环境要求

- Python 3.13
- Node.js 24
- MySQL 8.0
- 后端依赖：Django、djangorestframework、django-cors-headers、PyMySQL、python-dotenv

## 快速启动

### 1. 启动 MySQL

以管理员身份打开 PowerShell：

```powershell
net start MySQL80
```

### 2. 配置数据库

在 `backend/.env` 中填写连接信息：

```
DB_NAME=ad_platform
DB_USER=root
DB_PASSWORD=你的密码
DB_HOST=127.0.0.1
DB_PORT=3306
```

首次运行需建库并执行迁移：

```powershell
cd F:\dev\ad-platform\backend
$env:PYTHONPATH="F:\dev\django_packages"
python manage.py migrate
```

### 3. 启动后端

```powershell
cd F:\dev\ad-platform\backend
$env:PYTHONPATH="F:\dev\django_packages"
python manage.py runserver 127.0.0.1:8000
```

### 4. 启动前端

```powershell
cd F:\dev\ad-platform\frontend
npm run dev
```

浏览器访问 <http://127.0.0.1:5173>，页面显示“已连接 / Hello World”即联调成功。

## 接口说明

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/api/hello` | 联调探针，返回问候语与服务器时间 |

返回示例：

```json
{
  "code": 0,
  "message": "Hello World",
  "data": {
    "service": "ad-platform-backend",
    "server_time": "2026-11-23 19:55:09"
  }
}
```

## 数据库说明

当前 `ad_platform` 库中只有 Django 自带的 10 张系统表（用户、权限、会话、迁移记录等），业务表将在实验四按设计文档建模后通过迁移生成。

## 协作约定

分支策略、提交信息规范与评审流程见《Git 协作规范》；配置项与基线说明见《配置项清单与基线说明》。
