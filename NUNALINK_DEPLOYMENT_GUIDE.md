# Nunalink.com 部署指南

## 概述

本指南将帮助您将集运管理系统部署到 Render 云端，并使用 `nunalink.com` 作为自定义域名。

## 前置要求

1. **Git** - 用于版本控制
   - 下载地址: https://git-scm.com/downloads
   
2. **GitHub 账号** - 用于代码托管
   - 注册地址: https://github.com
   
3. **Render 账号** - 用于云端部署
   - 注册地址: https://render.com
   
4. **域名 nunalink.com** - 需要您拥有此域名的控制权
   - 确保您可以在域名注册商处修改 DNS 设置

## 快速部署

### 方法一：使用批处理文件（推荐）

1. 双击运行 `deploy_nunalink.bat`
2. 按照脚本提示完成部署

### 方法二：手动运行脚本

```bash
python deploy/deploy_nunalink.py
```

## 详细部署步骤

### 第一步：准备代码

1. 确保您的项目代码已更新
2. 配置文件已更新为使用 `nunalink.com` 域名

### 第二步：创建 GitHub 仓库

1. 访问 https://github.com/new
2. 仓库名称：`order-management-system`
3. 选择 Public（公开）
4. 点击 "Create repository"
5. 复制仓库地址

### 第三步：部署到 Render

1. 访问 https://render.com/
2. 使用 GitHub 账号登录
3. 点击 "New +" → "Web Service"
4. 选择您刚创建的 GitHub 仓库
5. 配置信息：
   - **Name**: `order-management-system`
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python run_app.py`
6. 点击 "Create Web Service"
7. 等待部署完成（5-10分钟）

### 第四步：配置自定义域名

1. 在 Render 控制台找到您的 Web Service
2. 点击 "Settings" 标签
3. 找到 "Custom Domains" 部分
4. 点击 "Add Domain"
5. 输入：`nunalink.com`
6. 点击 "Add"

### 第五步：配置 DNS

Render 会提供 DNS 记录，您需要在域名注册商处配置：

1. 登录您的域名注册商（如 GoDaddy、Namecheap 等）
2. 找到 `nunalink.com` 的 DNS 管理
3. 添加以下 DNS 记录：
   - **类型**: CNAME
   - **名称**: @ 或留空
   - **值**: [Render 提供的 CNAME 值]
4. 保存 DNS 设置
5. 等待 DNS 传播（几分钟到几小时）

## 环境变量配置

确保以下环境变量在 Render 中正确设置：

```env
PYTHON_VERSION=3.11.5
FLASK_ENV=production
FLASK_DEBUG=false
SECRET_KEY=f7e3f65dcf0d3e6da4b96b75e686aeffd9db86f5acd41c3ecfcca25239e57b61
SQLALCHEMY_TRACK_MODIFICATIONS=false
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USE_SSL=false
MAIL_USERNAME=nunalinks@gmail.com
MAIL_PASSWORD=davh hlya mout oosq
BASE_URL=https://nunalink.com
ITEMS_PER_PAGE=20
MAX_CONTENT_LENGTH=16777216
WTF_CSRF_ENABLED=true
WTF_CSRF_SECRET_KEY=a764d876752e9cb4e962f07aa6616cf0c293ba1fe26966df35a3de992d1c2b97
LOG_LEVEL=INFO
LOG_TO_STDOUT=true
```

## 验证部署

部署完成后，您可以通过以下链接访问：

1. **Render 默认链接**: https://order-management-system.onrender.com
2. **自定义域名**: https://nunalink.com

## 故障排除

### 常见问题

1. **构建失败**
   - 检查 `requirements.txt` 文件是否存在
   - 查看 Render 控制台的构建日志

2. **应用无法启动**
   - 检查环境变量是否正确设置
   - 查看应用日志

3. **域名无法访问**
   - 确认 DNS 记录已正确配置
   - 等待 DNS 传播完成
   - 检查域名是否已在 Render 中正确添加

4. **邮件功能异常**
   - 检查 Gmail 应用密码是否正确
   - 确认 Gmail 账户已启用两步验证

### 获取帮助

如果遇到问题：

1. 查看 Render 控制台的日志
2. 检查 GitHub 仓库的代码
3. 确认所有配置步骤已完成

## 维护

### 更新应用

1. 修改本地代码
2. 提交到 GitHub
3. Render 会自动重新部署

### 监控

- 在 Render 控制台监控应用状态
- 查看访问日志和错误日志
- 监控数据库使用情况

## 成本

- **Render Free Tier**: 免费（每月 750 小时）
- **域名**: 需要您自己购买和维护
- **数据库**: Render PostgreSQL 免费版

## 安全建议

1. 定期更新依赖包
2. 使用强密码
3. 启用 HTTPS（Render 自动提供）
4. 定期备份数据

---

部署完成后，您的集运管理系统将通过 `https://nunalink.com` 访问，享受 24/7 的云端服务！ 