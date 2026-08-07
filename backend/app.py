import os
import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
CORS(app)  # Чтобы Cursor мог спокойно делать запросы с фронтенда

# Подключаем автоматический сбор метрик для Prometheus
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.0')

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        database=os.getenv('POSTGRES_DB', 'pizzadb'),
        user=os.getenv('POSTGRES_USER', 'pizza_user'),
        password=os.getenv('POSTGRES_PASSWORD', 'pizza_pass')
    )
    return conn

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/menu', methods=['GET'])
def get_menu():
    menu = [
        {"id": 1, "name": "Margherita", "price": 10.99, "image": "https://via.placeholder.com/150"},
        {"id": 2, "name": "Pepperoni", "price": 12.99, "image": "https://via.placeholder.com/150"},
        {"id": 3, "name": "Four Cheese", "price": 13.50, "image": "https://via.placeholder.com/150"}
    ]
    return jsonify(menu), 200

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.json or {}
    # В будущем напишем сохранение в Postgres
    return jsonify({
        "status": "success",
        "message": "Order received!",
        "order": data
    }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)