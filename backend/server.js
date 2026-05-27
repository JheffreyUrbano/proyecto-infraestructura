const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

const pool = new Pool({
    host: process.env.DB_HOST || 'postgres',
    port: process.env.DB_PORT || 5432,
    user: process.env.DB_USER || 'ferreteria_user',
    password: process.env.DB_PASSWORD || 'ferreteria_pass',
    database: process.env.DB_NAME || 'ferreteria_db',
});

app.get('/health', (req, res) => {
    res.json({ status: 'ok', service: 'backend' });
});

app.post('/api/auth/login', (req, res) => {
    const { username, password } = req.body;
    if (username === 'admin' && password === 'admin123') {
        res.json({ success: true, user: { id: 1, username: 'admin', nombre: 'Administrador' } });
    } else {
        res.status(401).json({ success: false, message: 'Credenciales inválidas' });
    }
});

app.get('/api/productos', async (req, res) => {
    try {
        const result = await pool.query('SELECT id_producto, codigo_barras, nombre_producto, stock_actual, precio_venta FROM productos LIMIT 200');
        res.json(result.rows);
    } catch (err) {
        console.error('Error:', err.message);
        res.json([]);
    }
});

app.get('/api/resumen-stock', async (req, res) => {
    try {
        const result = await pool.query('SELECT COUNT(*) as total, SUM(stock_actual) as unidades FROM productos');
        res.json(result.rows[0]);
    } catch (err) {
        res.json({ total: 0, unidades: 0 });
    }
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Backend running on port ${PORT}`);
});
