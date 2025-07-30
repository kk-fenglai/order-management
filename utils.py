import logging
from flask import render_template
from flask_mail import Message
from datetime import datetime, timedelta
import qrcode
import io
import base64
from email_validator import validate_email, EmailNotValidError

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_email_address(email):
    """验证邮箱地址格式"""
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

def send_shenzhen_arrival_email(package, mail):
    """发送深圳仓库到达通知邮件"""
    try:
        msg = Message(
            subject=f'您的包裹已到达深圳仓库 - 快递单号: {package.shenzhen_tracking_number}',
            sender=mail.app.config['MAIL_USERNAME'],
            recipients=[package.customer_email]
        )
        
        msg.html = render_template(
            'email/shenzhen_arrival.html',
            package=package
        )
        
        mail.send(msg)
        
        # 更新邮件发送状态 - 在应用上下文中执行
        with mail.app.app_context():
            from models import db
            # 重新查询包裹以确保数据是最新的
            updated_package = db.session.get(package.__class__, package.id)
            if updated_package:
                updated_package.shenzhen_email_sent = True
                updated_package.updated_at = datetime.utcnow()
                db.session.commit()
                logger.info(f"深圳到达邮件发送成功并更新状态: {package.customer_email}")
            else:
                logger.warning(f"包裹不存在，无法更新状态: {package.id}")
        
        return True
    except Exception as e:
        logger.error(f"发送深圳到达邮件失败: {e}")
        return False

def send_cafe_arrival_email(package, mail):
    """发送咖啡馆到达通知邮件"""
    try:
        msg = Message(
            subject=f'您的包裹已到达咖啡馆 - 取件码: {package.pickup_code}，请到咖啡馆取件',
            sender=mail.app.config['MAIL_USERNAME'],
            recipients=[package.customer_email]
        )
        
        msg.html = render_template(
            'email/cafe_arrival.html',
            package=package,
            timedelta=timedelta
        )
        
        mail.send(msg)
        
        # 更新邮件发送状态 - 在应用上下文中执行
        with mail.app.app_context():
            from models import db
            # 重新查询包裹以确保数据是最新的
            updated_package = db.session.get(package.__class__, package.id)
            if updated_package:
                updated_package.cafe_email_sent = True
                updated_package.updated_at = datetime.utcnow()
                db.session.commit()
                logger.info(f"咖啡馆到达邮件发送成功并更新状态: {package.customer_email}")
            else:
                logger.warning(f"包裹不存在，无法更新状态: {package.id}")
        
        return True
    except Exception as e:
        logger.error(f"发送咖啡馆到达邮件失败: {e}")
        return False

def generate_pickup_codes_qr(packages):
    """生成批量二维码，内容为移动端取件码页面网址，便于微信扫码跳转"""
    if not packages:
        return None, None
    
    # 自动获取当前请求的URL
    from flask import request, current_app
    try:
        if request and hasattr(request, 'host_url'):
            # 如果有请求上下文，使用当前请求的URL
            base_url = request.host_url.rstrip('/')
            logger.info(f"使用请求URL作为BASE_URL: {base_url}")
        else:
            # 否则使用配置的BASE_URL
            base_url = current_app.config.get('BASE_URL', 'http://localhost:5000')
            logger.info(f"使用配置的BASE_URL: {base_url}")
    except Exception as e:
        # 如果获取失败，使用配置的BASE_URL
        base_url = current_app.config.get('BASE_URL', 'http://localhost:5000')
        logger.warning(f"获取BASE_URL失败，使用默认值: {base_url}, 错误: {e}")
    
    url = f"{base_url}/mobile_pickup"
    
    # 生成二维码
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    qr_image = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    # 生成更详细的预览内容
    preview_content = f"""二维码内容预览：
URL: {url}
功能: 移动端取件码查看页面
用途: 扫描后可在手机上查看所有取件码
包含包裹数量: {len(packages)} 个
生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"""
    
    return qr_image, preview_content

def format_datetime(dt, format_str='%Y-%m-%d %H:%M'):
    """格式化日期时间"""
    if dt is None:
        return '未设置'
    return dt.strftime(format_str)

def get_status_info(status):
    """获取状态信息"""
    status_info = {
        'shenzhen_arrived': {
            'display': '已到深圳',
            'color': 'warning',
            'icon': 'fa-truck'
        },
        'cafe_arrived': {
            'display': '已到咖啡馆',
            'color': 'success',
            'icon': 'fa-store'
        },
        'picked_up': {
            'display': '已取件',
            'color': 'primary',
            'icon': 'fa-check-circle'
        }
    }
    return status_info.get(status, {
        'display': status,
        'color': 'secondary',
        'icon': 'fa-question'
    }) 