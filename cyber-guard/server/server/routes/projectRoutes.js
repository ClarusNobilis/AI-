const express = require('express');
const router = express.Router();
const pool = require('../config/db');
const authMiddleware = require('../middleware/authMiddleware');

// 获取所有项目
router.get('/', authMiddleware, async (req, res) => {
  try {
    const [rows] = await pool.query('SELECT * FROM projects');
    res.json(rows);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// 获取单个项目
router.get('/:id', authMiddleware, async (req, res) => {
  try {
    const [rows] = await pool.query('SELECT * FROM projects WHERE id = ?', [req.params.id]);
    if (rows.length === 0) return res.status(404).json({ message: '项目不存在' });
    res.json(rows[0]);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// 创建项目
router.post('/', authMiddleware, async (req, res) => {
  try {
    const { name, village_id, description, start_date, end_date, status } = req.body;
    const [result] = await pool.query(
      'INSERT INTO projects (name, village_id, description, start_date, end_date, status) VALUES (?, ?, ?, ?, ?, ?)',
      [name, village_id, description, start_date, end_date, status]
    );
    res.status(201).json({ id: result.insertId, ...req.body });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// 更新项目
router.put('/:id', authMiddleware, async (req, res) => {
  try {
    const { name, village_id, description, start_date, end_date, status } = req.body;
    const [result] = await pool.query(
      'UPDATE projects SET name = ?, village_id = ?, description = ?, start_date = ?, end_date = ?, status = ? WHERE id = ?',
      [name, village_id, description, start_date, end_date, status, req.params.id]
    );
    if (result.affectedRows === 0) return res.status(404).json({ message: '项目不存在' });
    res.json({ id: req.params.id, ...req.body });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// 删除项目
router.delete('/:id', authMiddleware, async (req, res) => {
  try {
    const [result] = await pool.query('DELETE FROM projects WHERE id = ?', [req.params.id]);
    if (result.affectedRows === 0) return res.status(404).json({ message: '项目不存在' });
    res.json({ message: '项目已删除' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;