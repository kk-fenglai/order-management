# Render部署检查清单

## ✅ 代码已上传到GitHub
- [x] 最新代码已推送到GitHub
- [x] 包含Gmail邮件配置
- [x] 包含Render部署文件

## 🚀 Render部署步骤

### 1. 登录Render控制台
- [ ] 访问 https://render.com
- [ ] 使用GitHub账户登录
- [ ] 进入控制台

### 2. 创建Web Service
- [ ] 点击"New +" → "Web Service"
- [ ] 连接GitHub仓库：`order-management-system`
- [ ] 选择分支：`master`

### 3. 配置应用设置
```
Name: order-management-system
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn render_app:app
```

### 4. 设置环境变量
在"Environment"标签页添加以下变量：

#### 基础配置
```
SECRET_KEY = nuna-links-2025-secret-key-12345
FLASK_DEBUG = false
```

#### Gmail邮件配置
```
MAIL_SERVER = smtp.gmail.com
MAIL_PORT = 587
MAIL_USE_TLS = true
MAIL_USE_SSL = false
MAIL_USERNAME = dengfenglai1210@gmail.com
MAIL_PASSWORD = fwpkjjgtfyqomqqa
```

#### 应用配置（部署后更新）
```
BASE_URL = https://your-app-name.onrender.com
```

### 5. 选择计划
- [ ] 选择免费计划（测试用）
- [ ] 或选择付费计划（生产用）

### 6. 部署
- [ ] 点击"Create Web Service"
- [ ] 等待构建完成
- [ ] 检查部署状态

## 🔍 部署后检查

### 1. 检查应用状态
- [ ] 访问应用URL
- [ ] 确认页面正常加载
- [ ] 检查导航栏和功能

### 2. 测试核心功能
- [ ] 创建新包裹
- [ ] 查看包裹列表
- [ ] 测试搜索功能
- [ ] 查看统计页面

### 3. 测试邮件功能
- [ ] 创建测试包裹
- [ ] 发送深圳到达邮件
- [ ] 检查邮箱是否收到邮件
- [ ] 测试咖啡馆到达邮件

### 4. 测试二维码功能
- [ ] 访问二维码页面
- [ ] 确认二维码正常显示
- [ ] 测试移动端取件码页面

### 5. 更新BASE_URL
- [ ] 获取实际的Render应用URL
- [ ] 更新BASE_URL环境变量
- [ ] 重新部署应用

## 🛠️ 故障排除

### 如果部署失败：
1. 检查构建日志
2. 确认requirements.txt正确
3. 检查环境变量设置

### 如果邮件发送失败：
1. 检查Render日志
2. 确认Gmail配置正确
3. 验证应用专用密码

### 如果应用无法访问：
1. 检查部署状态
2. 确认URL正确
3. 查看错误日志

## 📞 获取帮助

如果遇到问题：
1. 查看Render文档
2. 检查应用日志
3. 提交GitHub Issue

---

**部署完成后，你的集运系统就可以在互联网上访问了！** 🎉 