from functools import wraps
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('请先登录', 'warning')
            return redirect(url_for('auth.login'))
            
        if not current_user.is_admin():
            flash('您需要管理员权限才能访问此页面', 'danger')
            return redirect(url_for('content.index'))
            
        return f(*args, **kwargs)
    return decorated_function