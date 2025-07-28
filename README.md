# NÜNA LINKS 集运管理系统

一个现代化的包裹管理系统，采用北欧风格设计，提供完整的集运业务流程管理。

## 🌟 功能特性

### 核心功能
- **包裹管理**：创建、编辑、删除包裹记录
- **状态跟踪**：深圳到达 → 咖啡馆到达 → 已取件
- **邮件通知**：自动发送深圳到达和咖啡馆到达通知邮件
- **取件码系统**：自动生成唯一取件码
- **二维码功能**：生成二维码供客户扫描查看取件码

### 批量操作
- **Excel导入**：支持批量导入包裹信息
- **批量邮件**：一键发送所有待发送邮件
- **批量删除**：按状态筛选批量删除包裹

### 移动端优化
- **移动端取件码**：专为手机优化的取件码查看界面
- **响应式设计**：适配各种屏幕尺寸
- **触摸友好**：优化的触摸交互体验

### 数据统计
- **实时统计**：包裹数量、状态分布、完成率
- **今日数据**：当日新增包裹统计
- **可视化展示**：直观的数据展示界面

## 🎨 设计特色

### 北欧风格UI
- **简洁明亮**：浅色背景，大量留白
- **自然色调**：柔和的蓝色、绿色、橙色
- **现代字体**：使用Inter字体提升可读性
- **圆角设计**：友好的圆角元素
- **渐变效果**：优雅的渐变色彩

### 用户体验
- **动画效果**：平滑的页面加载和交互动画
- **响应式布局**：完美适配桌面和移动设备
- **直观操作**：清晰的操作流程和反馈

## 🚀 快速开始

### 环境要求
- Python 3.7+
- Flask
- SQLite (开发环境)
- 邮件服务器配置

### 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/kk-fenglai/order-management-system.git
cd order-management-system
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **配置环境**
```bash
# 复制配置文件
cp config_local.py.example config_local.py
# 编辑配置文件，设置邮件服务器等信息
```

4. **初始化数据库**
```bash
python run_app.py
```

5. **访问系统**
```
http://localhost:5000
```

## 📧 邮件配置

在 `config_local.py` 中配置邮件服务器：

```python
# 邮件服务器配置
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'your-email@gmail.com'
MAIL_PASSWORD = 'your-app-password'
```

## 📱 使用指南

### 基本流程

1. **创建包裹**
   - 手动创建：点击"新建包裹"
   - 批量导入：使用Excel文件批量导入

2. **状态管理**
   - 深圳到达：包裹到达深圳仓库
   - 咖啡馆到达：包裹到达咖啡馆，发送取件码
   - 已取件：客户完成取件

3. **邮件通知**
   - 深圳到达邮件：通知客户包裹已到深圳
   - 咖啡馆到达邮件：发送取件码给客户

4. **取件码管理**
   - 自动生成唯一取件码
   - 二维码展示所有取件码
   - 移动端优化查看界面

### 批量操作

1. **Excel导入**
   - 下载导入模板
   - 填写客户信息
   - 上传Excel文件
   - 一键群发邮件

2. **批量邮件**
   - 发送所有待发送的深圳邮件
   - 发送所有待发送的咖啡馆邮件

## 🛠️ 技术栈

- **后端**：Flask + SQLAlchemy
- **前端**：Bootstrap 5 + Font Awesome
- **数据库**：SQLite (开发) / MySQL (生产)
- **邮件**：Flask-Mail
- **二维码**：qrcode
- **Excel处理**：pandas + openpyxl

## 📁 项目结构

```
order-management-system/
├── app.py                 # 主应用文件
├── models.py              # 数据模型
├── utils.py               # 工具函数
├── config.py              # 配置文件
├── config_local.py        # 本地配置
├── run_app.py             # 启动脚本
├── templates/             # HTML模板
│   ├── base.html          # 基础模板
│   ├── index.html         # 主页
│   ├── mobile_pickup.html # 移动端取件码
│   ├── qr_codes.html      # 二维码页面
│   └── email/             # 邮件模板
├── static/                # 静态文件
└── requirements.txt       # 依赖列表
```

## 🌍 时区支持

系统支持巴黎时区显示：
- 所有时间显示都转换为巴黎时间
- 自动计算最晚取件时间（7天后）
- 逾期状态自动判断

## 🔧 开发说明

### 运行开发服务器
```bash
python run_app.py
```

### 数据库迁移
```bash
# 创建新的迁移脚本
python migrate_add_qr_code.py
```

### 测试
```bash
# 运行测试脚本
python test_copyright.py
python test_paris_time.py
```

## 📄 许可证

© 2025 NÜNA LINKS 集运中心. 保留所有权利.

## 🤝 贡献

欢迎提交Issue和Pull Request来改进项目。

## 📞 支持

如有问题，请通过以下方式联系：
- 提交GitHub Issue
- 发送邮件至技术支持

---

**NÜNA LINKS 集运中心** - 让包裹管理更简单、更高效！ 