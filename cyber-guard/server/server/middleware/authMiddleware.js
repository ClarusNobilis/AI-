const jwt = require('jsonwebtoken');

// 身份验证中间件
const authMiddleware = (req, res, next) => {
  // 从请求头获取token
  const token = req.header('x-auth-token');
  if (!token) {
    return res.status(401).json({ message: '无访问令牌，拒绝访问' });
  }

  try {
    // 验证token
    const decoded = jwt.verify(token, 'your_jwt_secret_key'); // 实际使用时应更换为环境变量
    req.user = decoded.user;
    next();
  } catch (err) {
    res.status(401).json({ message: '令牌无效' });
  }
};

module.exports = authMiddleware;