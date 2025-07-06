import re
from datetime import datetime
from models import Article, Tool, SecurityEvent

def generate_slug(model, title):
    """生成唯一的slug"""
    base_slug = re.sub(r'[^\w\s-]', '', title).strip().lower()
    base_slug = re.sub(r'[-\s]+', '-', base_slug)
    
    slug = base_slug
    counter = 1
    
    while model.query.filter_by(slug=slug).first():
        slug = f"{base_slug}-{counter}"
        counter += 1
    
    return slug

def format_datetime(value, format='%Y-%m-%d %H:%M'):
    """格式化日期时间"""
    if value is None:
        return ""
    return value.strftime(format)

def calculate_reading_time(text, wpm=200):
    """计算阅读时间"""
    words = text.split()
    minutes = len(words) // wpm
    return max(1, minutes)  # 至少1分钟

def get_popular_articles(limit=5):
    """获取热门文章"""
    return Article.query.filter_by(is_published=True).order_by(Article.views.desc()).limit(limit).all()

def get_recent_tools(limit=5):
    """获取最新工具"""
    return Tool.query.filter_by(is_verified=True).order_by(Tool.created_at.desc()).limit(limit).all()

def get_upcoming_events(limit=5):
    """获取即将发生的事件"""
    return SecurityEvent.query.filter(SecurityEvent.occurred_at > datetime.utcnow()).order_by(SecurityEvent.occurred_at.asc()).limit(limit).all()

# 添加请求频率限制装饰器
def rate_limit(requests=100, window=15):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            # 实现基于IP的请求频率限制
            ...
        return wrapped
    return decorator