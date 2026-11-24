<div align="center">

简体中文 ｜ 课程作业

# 广告投放平台

**一个面向广告主与运营的互联网广告投放平台**

把实验二的设计落成能跑、能协作、可追溯的开发舞台。

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Vue](https://img.shields.io/badge/Vue-3.5-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white)](https://vuejs.org/)
[![Vite](https://img.shields.io/badge/Vite-5.4-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)

[![Stars](https://img.shields.io/github/stars/Yang-root/ad_platform?style=for-the-badge&logo=github&label=Stars)](https://github.com/Yang-root/ad_platform/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/Yang-root/ad_platform?style=for-the-badge&logo=git&label=Last%20commit)](https://github.com/Yang-root/ad_platform/commits)
[![Stage](https://img.shields.io/badge/阶段-实验三-2ea44f?style=for-the-badge)](https://github.com/Yang-root/ad_platform)

[快速开始](#quickstart) · [项目结构](#structure) · [接口说明](#api) · [分支与协作](#git) · [文档](#docs)

<a href="https://github.com/Yang-root/ad_platform"><img src="https://img.shields.io/badge/Star_这个仓库-0969DA?style=for-the-badge&logo=github&logoColor=white" alt="Star"></a>

</div>

> 当前阶段为实验三工程骨架，只包含可运行的开发环境与联调探针接口，业务功能从实验四开始开发。

<a name="quickstart"></a>
## 🚀 快速开始

**环境要求**：Python 3.13、Node.js 24、MySQL 8.0；后端依赖 Django 5.0、Django REST Framework 3.15、django-cors-headers、PyMySQL、python-dotenv。

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

<a name="structure"></a>
## 📁 项目结构

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

<a name="api"></a>
## 🔌 接口说明

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

## 🗄 数据库说明

当前 `ad_platform` 库中只有 Django 自带的 10 张系统表（用户、权限、会话、迁移记录等），业务表将在实验四按设计文档建模后通过迁移生成。

<a name="git"></a>
## 🌿 分支与协作

| 分支 | 用途 |
|---|---|
| `main` | 稳定基线，只放可运行、可验收的版本 |
| `develop` | 集成分支，功能评审通过后合入 |
| `feature/*` | 功能分支，一人一任务，完成后经 PR 合回 `develop` |

提交信息统一采用 `type(scope): subject` 格式，合并前须经至少 1 名组员评审。详细规则见《Git 协作规范》。

<a name="docs"></a>
## 📚 文档

| 文档 | 内容 |
|---|---|
| 第五组实验三Git协作规范 | 分支模型、提交规范、PR 评审流程 |
| 第五组实验三广告平台软件配置项清单 | 21 项配置项与责任人 |
| 第五组实验三本阶段基线说明 | 基线 BL-E3-01、验证结果与变更控制 |

## ✅ 当前进度

- [x] Django + Vue3 + MySQL 环境搭建
- [x] Hello World 前后端联调
- [x] Git 远程仓库与 main / develop / feature 分支
- [x] 协作规范、配置项清单与基线说明

## 👥 团队成员

| 成员 | 分工 |
|---|---|
| 杨正平 | 架构总体、后端骨架、统稿 |
| 卢伟浩 | 前端页面、工程配置 |
| 肖伟群 | 数据模型、数据库 |
| 林润泉 | 接口开发、接口文档 |
| 黄伟槟 | 联调测试、文档校核 |

<div align="center">

**软件工程 · 第 5 组 · 2026**

</div>
