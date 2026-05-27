#!/usr/bin/env python3
import psycopg2
import os

print("=" * 70)
print("ANALISIS DE DATOS - FERRETERIA")
print("=" * 70)

try:
    conn = psycopg2.connect(
        host=os.environ.get('POSTGRES_HOST', 'ferreteria_postgres'),
        port=os.environ.get('POSTGRES_PORT', 5432),
        dbname=os.environ.get('POSTGRES_DB', 'ferreteria_db'),
        user=os.environ.get('POSTGRES_USER', 'ferreteria_user'),
        password=os.environ.get('POSTGRES_PASSWORD', 'ferreteria_pass')
    )
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM productos")
    total = cursor.fetchone()[0]
    print(f"📦 Total productos: {total:,}")
    
    cursor.execute("SELECT COUNT(*) FROM productos WHERE stock_actual = 0")
    sin_stock = cursor.fetchone()[0]
    print(f"⚠️  Sin stock: {sin_stock:,}")
    
    cursor.execute("SELECT COUNT(*) FROM productos WHERE stock_actual > 0 AND stock_actual < 10")
    stock_bajo = cursor.fetchone()[0]
    print(f"⚠️  Stock bajo (<10): {stock_bajo:,}")
    
    cursor.execute("SELECT SUM(stock_actual * precio_venta) FROM productos")
    valor = cursor.fetchone()[0] or 0
    print(f"💰 Valor inventario: ${valor:,.2f}")
    
    cursor.execute("SELECT nombre_producto, precio_venta FROM productos ORDER BY precio_venta DESC LIMIT 5")
    print("\n🏆 TOP 5 PRODUCTOS MAS CAROS:")
    for p in cursor.fetchall():
        print(f"   - {p[0][:45]}: ${p[1]:,.2f}")
    
    cursor.close()
    conn.close()
    print("\n✅ Analisis completado")
    
except Exception as e:
    print(f"❌ Error: {e}")
