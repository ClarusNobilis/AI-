# 新增异步任务处理器
from celery import Celery
# 异步日志记录实现
from celery import Celery
from models import SecurityLog

celery = Celery(__name__, broker=app.config['CELERY_BROKER_URL'])

@celery.task
def log_security_event(event_data):
    event = SecurityLog(
        user_id=event_data['user_id'],
        event_type=event_data['event_type'],
        ip_address=event_data['ip'],
        user_agent=event_data['user_agent'],
        details=event_data['details']
    )
    db.session.add(event)
    db.session.commit()

celery = Celery(__name__, broker='redis://localhost:6379/0')

@celery.task
def log_download_async(tool_id):
    # 异步记录工具下载统计
    tool = Tool.query.get(tool_id)
    tool.downloads += 1
    db.session.commit()