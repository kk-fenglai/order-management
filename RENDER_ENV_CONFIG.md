# Render环境参数配置指南

## 环境参数说明

### 1. 基础配置参数

#### Python版本配置
```yaml
- key: PYTHON_VERSION
  value: 3.11.18
```
**说明**: 指定Python版本，确保与依赖包兼容

#### Flask应用配置
```yaml
- key: FLASK_ENV
  value: production
- key: FLASK_DEBUG
  value: false
- key: SECRET_KEY
  value: your-super-secret-key-change-this-in-production-2024
```
**说明**: 
- `FLASK_ENV`: 设置为production生产环境
- `FLASK_DEBUG`: 生产环境关闭调试模式
- `SECRET_KEY`: 用于会话加密，必须更改默认值

### 2. 数据库配置

#### 自动配置 (推荐)
Render会自动提供`DATABASE_URL`环境变量，无需手动设置。

#### 手动配置 (可选)
```yaml
- key: DATABASE_URL
  value: postgresql://username:password@host:port/database
- key: SQLALCHEMY_TRACK_MODIFICATIONS
  value: false
```

### 3. 邮件配置

#### Gmail配置 (推荐)
```yaml
- key: MAIL_SERVER
  value: smtp.gmail.com
- key: MAIL_PORT
  value: 587
- key: MAIL_USE_TLS
  value: true
- key: MAIL_USE_SSL
  value: false
- key: MAIL_USERNAME
  value: your-email@gmail.com
- key: MAIL_PASSWORD
  value: your-app-password
```

#### 163邮箱配置 (备选)
```yaml
- key: MAIL_SERVER
  value: smtp.163.com
- key: MAIL_PORT
  value: 465
- key: MAIL_USE_TLS
  value: false
- key: MAIL_USE_SSL
  value: true
- key: MAIL_USERNAME
  value: your-email@163.com
- key: MAIL_PASSWORD
  value: your-password
```

### 4. 应用配置

```yaml
- key: BASE_URL
  value: https://your-app-name.onrender.com
- key: ITEMS_PER_PAGE
  value: 20
- key: MAX_CONTENT_LENGTH
  value: 16777216
```

**说明**:
- `BASE_URL`: 你的应用访问地址，部署后需要更新
- `ITEMS_PER_PAGE`: 每页显示的项目数量
- `MAX_CONTENT_LENGTH`: 文件上传大小限制 (16MB)

### 5. 安全配置

```yaml
- key: WTF_CSRF_ENABLED
  value: true
- key: WTF_CSRF_SECRET_KEY
  value: your-csrf-secret-key-2024
```

### 6. 日志配置

```yaml
- key: LOG_LEVEL
  value: INFO
- key: LOG_TO_STDOUT
  value: true
```

## 部署前检查清单

### ✅ 必须修改的参数

1. **SECRET_KEY**: 生成新的密钥
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

2. **BASE_URL**: 更新为你的实际应用地址
   ```
   https://your-app-name.onrender.com
   ```

3. **邮件配置**: 确保邮箱和密码正确
   - Gmail需要使用应用专用密码
   - 163邮箱需要使用授权码

### ✅ 可选修改的参数

1. **ITEMS_PER_PAGE**: 根据需要调整分页数量
2. **MAX_CONTENT_LENGTH**: 根据需要调整文件上传限制
3. **LOG_LEVEL**: 根据需要调整日志级别 (DEBUG, INFO, WARNING, ERROR)

## 环境变量优先级

1. **Render环境变量** (最高优先级)
2. **render.yaml配置**
3. **.env文件** (本地开发)
4. **默认值** (最低优先级)

## 安全注意事项

### 🔒 敏感信息保护

1. **不要在代码中硬编码密码**
2. **使用环境变量存储敏感信息**
3. **定期更换密钥和密码**
4. **使用HTTPS协议**

### 🔒 生产环境安全

1. **关闭调试模式**: `FLASK_DEBUG=false`
2. **使用强密钥**: 生成32位随机密钥
3. **启用CSRF保护**: `WTF_CSRF_ENABLED=true`
4. **限制文件上传**: 设置合理的文件大小限制

## 常见问题解决

### Q: 邮件发送失败？
A: 检查以下配置：
- 邮箱服务器地址和端口
- 用户名和密码是否正确
- TLS/SSL设置是否正确
- Gmail需要使用应用专用密码

### Q: 数据库连接失败？
A: 检查以下配置：
- Render是否自动提供了DATABASE_URL
- 数据库类型是否支持
- 连接字符串格式是否正确

### Q: 应用无法启动？
A: 检查以下配置：
- Python版本是否兼容
- 依赖包是否正确安装
- 环境变量是否完整
- 日志输出是否有错误信息

## 测试环境变量

部署后，可以通过以下方式测试环境变量：

```python
import os
print(f"MAIL_SERVER: {os.environ.get('MAIL_SERVER')}")
print(f"BASE_URL: {os.environ.get('BASE_URL')}")
print(f"FLASK_ENV: {os.environ.get('FLASK_ENV')}")
```

## 更新环境变量

### 方法1: 通过render.yaml (推荐)
修改render.yaml文件，重新部署

### 方法2: 通过Render控制台
1. 进入Render控制台
2. 选择你的服务
3. 点击"Environment"
4. 添加或修改环境变量
5. 重新部署

### 方法3: 通过Render CLI
```bash
render env set KEY VALUE
render deploy
``` 