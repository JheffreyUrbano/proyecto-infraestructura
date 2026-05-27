CREATE TABLE IF NOT EXISTS productos (
    id_producto SERIAL PRIMARY KEY,
    codigo_barras VARCHAR(50),
    nombre_producto VARCHAR(100) NOT NULL,
    stock_actual INTEGER DEFAULT 0,
    precio_venta DECIMAL(10,2) DEFAULT 0
);
