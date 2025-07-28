# 🚀 集运管理系统 - 部署工具包

这个文件夹包含了所有部署相关的工具和指南，帮助您将集运管理系统部署到云端。

## 📁 文件说明

### 🎯 **推荐部署方案**

#### **1. Render 云端部署（推荐）**
- `deploy_simple.bat` - **一键部署脚本**（双击运行）
- `deploy_render.py` - Render 部署脚本
- `快速部署指南.md` - 详细部署指南
- `render.yaml` - Render 配置文件
- `Procfile` - 启动配置文件

#### **2. Railway 云端部署**
- `railway_deploy.py` - Railway 部署脚本
- `railway_env.py` - Railway 环境变量配置
- `railway.json` - Railway 配置文件
- `deploy_cloud.bat` - Railway 部署批处理脚本

#### **3. ngrok 本地隧道**
- `deploy_ngrok.py` - ngrok 隧道部署脚本
- `start_public.bat` - ngrok 启动脚本

### 📚 **部署指南**
- `云端部署指南.md` - 完整的云端部署指南
- `部署指南.md` - 通用部署指南

## 🚀 **快速开始**

### **方法1：Render 部署（推荐）**
```bash
# 双击运行这个文件
deploy_simple.bat
```

### **方法2：Railway 部署**
```bash
# 双击运行这个文件
deploy_cloud.bat
```

### **方法3：ngrok 隧道**
```bash
# 双击运行这个文件
start_public.bat
```

## 🎯 **部署方案对比**

| 方案 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| **Render** | ✅ 完全免费<br>✅ 一键部署<br>✅ 24/7在线 | ❌ 需要GitHub账号 | 🎯 **推荐首选** |
| **Railway** | ✅ 完全免费<br>✅ 自动扩展 | ❌ 需要Node.js | 🎯 备选方案 |
| **ngrok** | ✅ 无需账号<br>✅ 即时可用 | ❌ 需要电脑运行<br>❌ 链接会变化 | 🎯 临时测试 |

## 📋 **部署前准备**

### **Render 部署（推荐）**
1. **GitHub 账号** - 注册：https://github.com/signup
2. **Render 账号** - 注册：https://render.com/
3. **Git** - 已安装（检查：`git --version`）

### **Railway 部署**
1. **GitHub 账号** - 注册：https://github.com/signup
2. **Railway 账号** - 注册：https://railway.app/
3. **Node.js** - 安装：https://nodejs.org/
4. **Git** - 已安装

### **ngrok 部署**
1. **无需账号** - 直接可用
2. **Python** - 已安装

## 🌐 **部署后效果**

### **云端部署（Render/Railway）**
- ✅ **24/7 在线** - 系统永远运行
- ✅ **全球访问** - 任何人都可以访问
- ✅ **固定链接** - 永久不变的网址
- ✅ **完全免费** - 每月免费额度足够使用
- ✅ **数据安全** - 云端备份，永不丢失
- ✅ **自动维护** - 无需手动管理

### **本地隧道（ngrok）**
- ✅ **即时可用** - 无需注册账号
- ❌ **需要电脑运行** - 关机后无法访问
- ❌ **链接会变化** - 每次重启都会改变

## 🎉 **推荐使用流程**

1. **选择 Render 部署**（推荐）
2. **双击运行** `deploy_simple.bat`
3. **按提示操作**：
   - 创建 GitHub 仓库
   - 在 Render 部署
   - 获取访问链接
4. **分享链接**给团队成员

## 📞 **技术支持**

如果遇到问题：
1. 查看对应的部署指南
2. 检查网络连接
3. 验证账号登录
4. 查看平台文档

**祝您部署成功！** 🚀 