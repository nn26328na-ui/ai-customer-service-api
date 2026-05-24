from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟订单数据库
MOCK_ORDERS = {
    "2024051800123456": {
        "order_id": "2024051800123456",
        "status": "已发货",
        "product": "蓝牙耳机 Pro",
        "amount": 299.00,
        "create_time": "2024-05-18 10:23:00",
        "ship_time": "2024-05-19 14:00:00",
        "logistics": "顺丰速运",
        "tracking_no": "SF1234567890",
        "estimated_delivery": "2024-05-21"
    },
    "2024051900654321": {
        "order_id": "2024051900654321",
        "status": "待发货",
        "product": "电子阅读器 Lite",
        "amount": 499.00,
        "create_time": "2024-05-19 09:10:00",
        "ship_time": None,
        "logistics": None,
        "tracking_no": None,
        "estimated_delivery": None
    },
    "2024052000999888": {
        "order_id": "2024052000999888",
        "status": "已完成",
        "product": "蓝牙耳机 Pro",
        "amount": 299.00,
        "create_time": "2024-05-20 15:00:00",
        "ship_time": "2024-05-20 18:00:00",
        "logistics": "京东快递",
        "tracking_no": "JD9876543210",
        "estimated_delivery": "2024-05-22"
    }
}

@app.route('/query_order', methods=['POST'])
def query_order():
    data = request.get_json()
    order_id = data.get('order_id', '').strip()

    if not order_id:
        return jsonify({
            "success": False,
            "message": "订单号不能为空"
        }), 400

    order = MOCK_ORDERS.get(order_id)

    if not order:
        return jsonify({
            "success": False,
            "message": f"未找到订单号 {order_id} 对应的订单，请确认订单号是否正确"
        }), 404

    return jsonify({
        "success": True,
        "data": order
    })


@app.route('/create_ticket', methods=['POST'])
def create_ticket():
    data = request.get_json()
    user_id = data.get('user_id', 'unknown')
    issue = data.get('issue', '')
    order_id = data.get('order_id', '')

    if not issue:
        return jsonify({
            "success": False,
            "message": "问题描述不能为空"
        }), 400

    # 模拟生成工单号
    import random, time
    ticket_no = f"TK{int(time.time())}{random.randint(100,999)}"

    return jsonify({
        "success": True,
        "data": {
            "ticket_no": ticket_no,
            "status": "已创建",
            "message": f"工单 {ticket_no} 已创建成功，客服将在1小时内与您联系",
            "order_id": order_id,
            "issue": issue
        }
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)

