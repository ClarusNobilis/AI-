const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const path = require('path');
const projectRoutes = require('./routes/projectRoutes');

// 初始化Express应用
const app = express();
const PORT = process.env.PORT || 3000;

// 中间件
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// 静态文件服务
app.use(express.static(path.join(__dirname, '../')));

// 路由注册
app.use('/api/projects', projectRoutes);

// 根路由
app.get('/', (req, res) => {
  res.json({ message: '乡村振兴管理平台API服务器' });
});

// 错误处理中间件
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: '服务器内部错误' });
});

// 启动服务器
app.listen(PORT, () => {
  console.log(`服务器运行在 http://localhost:${PORT}`);
});

module.exports = app;