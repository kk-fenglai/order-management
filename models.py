from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import random
import string
import pytz

db = SQLAlchemy()

class Package(db.Model):
    """集运包裹模型"""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(120), nullable=False)
    shenzhen_tracking_number = db.Column(db.String(50), unique=True, nullable=False)
    pickup_code = db.Column(db.String(10), unique=True, nullable=False)
    shenzhen_arrival_date = db.Column(db.DateTime, default=datetime.utcnow)
    cafe_arrival_date = db.Column(db.DateTime)
    pickup_date = db.Column(db.DateTime)  # 新增：取件时间
    status = db.Column(db.String(20), default='shenzhen_arrived')
    shenzhen_email_sent = db.Column(db.Boolean, default=False)
    cafe_email_sent = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text)  # 新增：备注字段
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Package {self.id}: {self.customer_name} - {self.shenzhen_tracking_number}>'

    @staticmethod
    def generate_pickup_code():
        """生成唯一的取件码"""
        max_attempts = 100  # 防止无限循环
        attempts = 0
        
        while attempts < max_attempts:
            # 生成6位数字取件码
            pickup_code = ''.join(random.choices(string.digits, k=6))
            
            try:
                # 检查是否已存在
                if not Package.query.filter_by(pickup_code=pickup_code).first():
                    return pickup_code
            except Exception as e:
                # 如果查询失败，记录错误并继续尝试
                import logging
                logging.error(f"检查取件码唯一性时出错: {e}")
            
            attempts += 1
        
        # 如果尝试次数过多，抛出异常
        raise ValueError("无法生成唯一的取件码，请重试") 

    def to_dict(self):
        """转换为字典格式"""
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'customer_email': self.customer_email,
            'shenzhen_tracking_number': self.shenzhen_tracking_number,
            'pickup_code': self.pickup_code,
            'shenzhen_arrival_date': self.shenzhen_arrival_date.isoformat() if self.shenzhen_arrival_date else None,
            'cafe_arrival_date': self.cafe_arrival_date.isoformat() if self.cafe_arrival_date else None,
            'pickup_date': self.pickup_date.isoformat() if self.pickup_date else None,
            'status': self.status,
            'shenzhen_email_sent': self.shenzhen_email_sent,
            'cafe_email_sent': self.cafe_email_sent,
            'notes': self.notes,
            'latest_pickup_time': self.latest_pickup_time_paris.isoformat() if self.latest_pickup_time_paris else None,
            'is_overdue': self.is_overdue
        }

    @property
    def status_display(self):
        """状态显示文本"""
        status_map = {
            'shenzhen_arrived': '已到深圳',
            'cafe_arrived': '已到咖啡馆',
            'picked_up': '已取件'
        }
        return status_map.get(self.status, self.status)

    @property
    def status_color(self):
        """状态对应的颜色"""
        color_map = {
            'shenzhen_arrived': 'warning',
            'cafe_arrived': 'success',
            'picked_up': 'primary'
        }
        return color_map.get(self.status, 'secondary')
    
    @property
    def latest_pickup_time(self):
        """计算最晚取货时间（从咖啡馆到达后7天）"""
        if self.cafe_arrival_date:
            return self.cafe_arrival_date + timedelta(days=7)
        return None
    
    @property
    def is_overdue(self):
        """检查是否超过最晚取货时间"""
        if self.status == 'cafe_arrived' and self.latest_pickup_time:
            return datetime.utcnow() > self.latest_pickup_time
        return False
    
    def to_paris_time(self, dt):
        """转换为巴黎时间"""
        if dt is None:
            return None
        utc_tz = pytz.UTC
        paris_tz = pytz.timezone('Europe/Paris')
        if dt.tzinfo is None:
            dt = utc_tz.localize(dt)
        return dt.astimezone(paris_tz)
    
    @property
    def cafe_arrival_date_paris(self):
        """咖啡馆到达时间（巴黎时间）"""
        return self.to_paris_time(self.cafe_arrival_date)
    
    @property
    def latest_pickup_time_paris(self):
        """最晚取件时间（巴黎时间）"""
        return self.to_paris_time(self.latest_pickup_time)
    
    @property
    def pickup_date_paris(self):
        """取件时间（巴黎时间）"""
        return self.to_paris_time(self.pickup_date) 