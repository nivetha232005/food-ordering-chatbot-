from flask import Flask, render_template, request, jsonify, session
import json
import pickle
import numpy as np
import nltk
import random
from nltk.stem import WordNetLemmatizer
from datetime import datetime
import os
import re

app = Flask(__name__)
app.secret_key = 'swiftbite_ai_secret_key_2024'

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Load menu
def load_menu():
    try:
        if os.path.exists('data/menu.json'):
            with open('data/menu.json', 'r', encoding='utf-8') as f:
                menu_data = json.load(f)
            print("✓ Loaded menu.json")
            return menu_data
        else:
            # Create default menu
            menu_data = {
                "categories": [
                    {
                        "name": "Pizza",
                        "items": [
                            {"id": 1, "name": "Margherita Pizza", "price": 299, "description": "Classic cheese and tomato pizza", "category": "Pizza", "image": "/static/images/pizza/margherita-pizza.jpg"},
                            {"id": 2, "name": "Pepperoni Pizza", "price": 399, "description": "Spicy pepperoni with cheese", "category": "Pizza", "image": "/static/images/pizza/pepperoni-pizza.jpg"},
                            {"id": 3, "name": "Farmhouse Pizza", "price": 449, "description": "Fresh vegetables and herbs", "category": "Pizza", "image": "/static/images/pizza/farmhouse-pizza.jpg"}
                        ]
                    },
                    {
                        "name": "Burgers",
                        "items": [
                            {"id": 4, "name": "Veg Burger", "price": 99, "description": "Crunchy veg patty burger", "category": "Burgers", "image": "/static/images/burgers/veg-burger.jpg"},
                            {"id": 5, "name": "Chicken Burger", "price": 149, "description": "Grilled chicken burger", "category": "Burgers", "image": "/static/images/burgers/chicken-burger.jpg"},
                            {"id": 6, "name": "Double Cheese Burger", "price": 179, "description": "Double patty with extra cheese", "category": "Burgers", "image": "/static/images/burgers/double-cheese-burger.jpg"}
                        ]
                    },
                    {
                        "name": "Drinks",
                        "items": [
                            {"id": 7, "name": "Coca Cola", "price": 40, "description": "Chilled soft drink", "category": "Drinks", "image": "/static/images/drinks/coca-cola.jpg"},
                            {"id": 8, "name": "Fresh Lime Soda", "price": 60, "description": "Refreshing lime soda", "category": "Drinks", "image": "/static/images/drinks/fresh-lime-soda.jpg"},
                            {"id": 9, "name": "Butter Milk", "price": 50, "description": "Traditional chaas", "category": "Drinks", "image": "/static/images/drinks/buttermilk.jpg"}
                        ]
                    },
                    {
                        "name": "South Indian",
                        "items": [
                            {"id": 10, "name": "Masala Dosa", "price": 120, "description": "Crispy dosa with potato filling", "category": "South Indian", "image": "/static/images/south-indian/masala-dosa.jpg"},
                            {"id": 11, "name": "Idli Sambhar", "price": 80, "description": "Soft idlis with sambhar", "category": "South Indian", "image": "/static/images/south-indian/idli-sambhar.jpg"},
                            {"id": 12, "name": "Vada", "price": 50, "description": "Crispy lentil donuts", "category": "South Indian", "image": "/static/images/south-indian/vada.jpg"}
                        ]
                    },
                    {
                        "name": "Desserts",
                        "items": [
                            {"id": 13, "name": "Gulab Jamun", "price": 70, "description": "Sweet fried milk balls", "category": "Desserts", "image": "/static/images/desserts/gulab-jamun.jpg"},
                            {"id": 14, "name": "Ice Cream", "price": 90, "description": "Vanilla chocolate strawberry", "category": "Desserts", "image": "/static/images/desserts/ice-cream.jpg"},
                            {"id": 15, "name": "Brownie", "price": 120, "description": "Chocolate brownie", "category": "Desserts", "image": "/static/images/desserts/brownie.jpg"}
                        ]
                    },
                    {
                        "name": "Combo Meals",
                        "items": [
                            {"id": 16, "name": "Pizza Combo", "price": 499, "description": "Pizza + Drink + Dessert", "category": "Combo Meals", "image": "/static/images/combos/pizza-combo.jpg"},
                            {"id": 17, "name": "Burger Combo", "price": 249, "description": "Burger + Fries + Drink", "category": "Combo Meals", "image": "/static/images/combos/burger-combo.jpg"},
                            {"id": 18, "name": "South Indian Combo", "price": 199, "description": "Dosa + Idli + Vada + Coffee", "category": "Combo Meals", "image": "/static/images/combos/south-indian-combo.jpg"}
                        ]
                    }
                ]
            }
            
            os.makedirs('data', exist_ok=True)
            with open('data/menu.json', 'w', encoding='utf-8') as f:
                json.dump(menu_data, f, indent=2)
            
            print("✓ Created default menu.json")
            return menu_data
    except Exception as e:
        print(f"✗ Error loading menu: {e}")
        return {"categories": []}

menu_data = load_menu()

# Load orders
orders_file = 'data/orders.json'
if os.path.exists(orders_file):
    try:
        with open(orders_file, 'r', encoding='utf-8') as f:
            orders = json.load(f)
        print(f"✓ Loaded {len(orders)} orders")
    except:
        orders = []
else:
    orders = []

def get_all_menu_items():
    all_items = []
    for category in menu_data.get('categories', []):
        for item in category.get('items', []):
            all_items.append(item)
    return all_items

def get_formatted_menu():
    menu_text = "🍕 **OUR DELICIOUS MENU** 🍔\n\n"
    for category in menu_data.get('categories', []):
        menu_text += f"**{category['name']}:**\n"
        for item in category.get('items', []):
            menu_text += f"  • *{item['name']}* - ₹{item['price']}\n"
            menu_text += f"    {item['description']}\n"
        menu_text += "\n"
    menu_text += "💡 *Tip: Just type the item name to order!*"
    return menu_text

def predict_intent(text):
    text_lower = text.lower()
    
    if any(word in text_lower for word in ['menu', 'show menu', 'what do you have']):
        return 'show_menu'
    elif any(word in text_lower for word in ['cart', 'my cart', 'view cart']):
        return 'view_cart'
    elif any(word in text_lower for word in ['checkout', 'place order', 'buy now']):
        return 'checkout'
    elif any(word in text_lower for word in ['hi', 'hello', 'hey']):
        return 'greeting'
    elif any(word in text_lower for word in ['thanks', 'thank you']):
        return 'thanks'
    elif any(word in text_lower for word in ['bye', 'goodbye', 'exit']):
        return 'goodbye'
    elif any(word in text_lower for word in ['want', 'order', 'get', 'add', 'buy']) or \
         any(item['name'].lower() in text_lower for item in get_all_menu_items()):
        return 'add_to_cart'
    
    return 'unknown'

def get_response(intent, user_message, cart_items=None):
    if intent == 'show_menu':
        return get_formatted_menu()
    elif intent == 'view_cart':
        if cart_items and len(cart_items) > 0:
            cart_summary = "🛒 **YOUR CART** 🛒\n\n"
            total = 0
            for i, item in enumerate(cart_items, 1):
                subtotal = item['price'] * item['quantity']
                total += subtotal
                cart_summary += f"{i}. **{item['name']}**\n"
                cart_summary += f"   Quantity: {item['quantity']} × ₹{item['price']} = ₹{subtotal}\n\n"
            cart_summary += f"💰 **TOTAL: ₹{total}**\n\n"
            return cart_summary
        else:
            return "Your cart is empty! 🛒 Type 'show menu' to see our items!"
    elif intent == 'checkout':
        if cart_items and len(cart_items) > 0:
            total = sum(item['price'] * item['quantity'] for item in cart_items)
            return f"🎉 **Ready to Checkout!** 🎉\n\nYour order total is ₹{total}\n\nPlease click the checkout button above!"
        else:
            return "Your cart is empty! Please add some items first!"
    elif intent == 'greeting':
        return "Hello! 👋 Welcome to SwiftBite AI! Ready to order? Type 'show menu' to see what we have!"
    elif intent == 'thanks':
        return "You're welcome! 🍽️ Happy to serve you!"
    elif intent == 'goodbye':
        return "Goodbye! 🍔 Come back soon!"
    else:
        return "Type 'show menu' to see our items or tell me what you'd like to order!"

def extract_food_items(message):
    items = []
    message_lower = message.lower()
    
    numbers = re.findall(r'\b\d+\b', message_lower)
    quantity = int(numbers[0]) if numbers else 1
    
    all_items = get_all_menu_items()
    
    found_item = None
    for menu_item in all_items:
        item_name = menu_item['name'].lower()
        if item_name in message_lower:
            found_item = menu_item
            break
        
        keywords = {
            'margherita': 'Margherita Pizza',
            'pepperoni': 'Pepperoni Pizza',
            'farmhouse': 'Farmhouse Pizza',
            'veg': 'Veg Burger',
            'chicken': 'Chicken Burger',
            'double cheese': 'Double Cheese Burger',
            'coke': 'Coca Cola',
            'soda': 'Fresh Lime Soda',
            'butter milk': 'Butter Milk',
            'dosa': 'Masala Dosa',
            'idli': 'Idli Sambhar',
            'vada': 'Vada',
            'gulab jamun': 'Gulab Jamun',
            'ice cream': 'Ice Cream',
            'brownie': 'Brownie'
        }
        
        for keyword, full_name in keywords.items():
            if keyword in message_lower and full_name.lower() == item_name:
                found_item = menu_item
                break
        if found_item:
            break
    
    if found_item:
        items.append({
            'name': found_item['name'],
            'quantity': quantity,
            'price': found_item['price'],
            'id': found_item['id']
        })
    
    return items

@app.route('/')
def index():
    if 'cart' not in session:
        session['cart'] = []
    return render_template('index.html')

@app.route('/checkout')
def checkout():
    cart = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart)
    return render_template('checkout.html', cart=cart, total=total)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/api/menu', methods=['GET'])
def get_menu_api():
    try:
        return jsonify(menu_data)
    except Exception as e:
        print(f"Error serving menu: {e}")
        return jsonify({"categories": []})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    cart = session.get('cart', [])
    
    extracted_items = extract_food_items(user_message)
    intent = predict_intent(user_message)
    response_text = ""
    
    if extracted_items:
        added_messages = []
        for item in extracted_items:
            found = False
            for cart_item in cart:
                if cart_item.get('name') == item['name']:
                    cart_item['quantity'] += item['quantity']
                    found = True
                    added_messages.append(f"Added {item['quantity']} more {item['name']}")
                    break
            if not found:
                cart.append(item)
                added_messages.append(f"Added {item['quantity']} {item['name']}")
        
        session['cart'] = cart
        
        if added_messages:
            total_items = len(cart)
            response_text = f"✅ {', '.join(added_messages)} to your cart!\n\n📦 Total items: {total_items}\n\nType 'view cart' to see your order or 'checkout' to place order!"
    
    if not response_text:
        response_text = get_response(intent, user_message, cart)
    
    if intent == 'view_cart' and not extracted_items:
        response_text = get_response('view_cart', user_message, cart)
    if intent == 'checkout' and not extracted_items:
        response_text = get_response('checkout', user_message, cart)
    if intent == 'show_menu' and not extracted_items:
        response_text = get_formatted_menu()
    
    cart_count = len(session.get('cart', []))
    
    return jsonify({
        'response': response_text,
        'intent': intent,
        'cart_count': cart_count
    })

@app.route('/api/add_to_cart', methods=['POST'])
def add_to_cart_api():
    data = request.json
    item_id = data.get('item_id')
    quantity = data.get('quantity', 1)
    
    item = None
    for category in menu_data.get('categories', []):
        for menu_item in category.get('items', []):
            if menu_item.get('id') == item_id:
                item = menu_item
                break
        if item:
            break
    
    if item:
        cart_item = {
            'id': item['id'],
            'name': item['name'],
            'price': item['price'],
            'quantity': quantity
        }
        
        cart = session.get('cart', [])
        found = False
        for cart_item_existing in cart:
            if cart_item_existing['id'] == item_id:
                cart_item_existing['quantity'] += quantity
                found = True
                break
        
        if not found:
            cart.append(cart_item)
        
        session['cart'] = cart
        return jsonify({
            'success': True, 
            'message': f'Added {quantity}x {item["name"]} to cart', 
            'cart_count': len(cart)
        })
    
    return jsonify({'success': False, 'message': 'Item not found'})

@app.route('/api/remove_from_cart', methods=['POST'])
def remove_from_cart_api():
    data = request.json
    item_id = data.get('item_id')
    
    cart = session.get('cart', [])
    cart = [item for item in cart if item.get('id') != item_id]
    session['cart'] = cart
    
    return jsonify({
        'success': True, 
        'message': 'Item removed from cart', 
        'cart_count': len(cart)
    })

@app.route('/api/cart', methods=['GET'])
def get_cart():
    cart = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart)
    return jsonify({'items': cart, 'total': total, 'count': len(cart)})

@app.route('/api/place_order', methods=['POST'])
def place_order():
    data = request.json
    cart = session.get('cart', [])
    
    if not cart:
        return jsonify({'success': False, 'message': 'Cart is empty'})
    
    order = {
        'id': len(orders) + 1,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'items': cart,
        'total': sum(item['price'] * item['quantity'] for item in cart),
        'customer': data.get('customer', {}),
        'payment_method': data.get('payment_method', 'Cash on Delivery'),
        'status': 'confirmed'
    }
    
    orders.append(order)
    os.makedirs('data', exist_ok=True)
    
    with open('data/orders.json', 'w', encoding='utf-8') as f:
        json.dump(orders, f, indent=2)
    
    session['cart'] = []
    
    return jsonify({'success': True, 'order_id': order['id']})

@app.route('/api/orders', methods=['GET'])
def get_orders():
    """Get all orders for admin"""
    try:
        return jsonify(orders)
    except Exception as e:
        print(f"Error getting orders: {e}")
        return jsonify([])

@app.route('/api/update_order_status', methods=['POST'])
def update_order_status():
    """Update order status"""
    try:
        data = request.json
        order_id = data.get('order_id')
        new_status = data.get('status')
        
        for order in orders:
            if order.get('id') == order_id:
                order['status'] = new_status
                order['status_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                break
        
        with open('data/orders.json', 'w', encoding='utf-8') as f:
            json.dump(orders, f, indent=2)
        
        return jsonify({'success': True, 'message': 'Order status updated'})
    except Exception as e:
        print(f"Error updating status: {e}")
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/user_orders', methods=['POST'])
def get_user_orders():
    """Get orders for a specific phone number"""
    try:
        data = request.json
        phone = data.get('phone')
        
        user_orders = [order for order in orders if order.get('customer', {}).get('phone') == phone]
        
        return jsonify({'success': True, 'orders': user_orders})
    except Exception as e:
        print(f"Error getting user orders: {e}")
        return jsonify({'success': False, 'message': str(e), 'orders': []})

@app.route('/api/track_order/<int:order_id>', methods=['GET'])
def track_order(order_id):
    """Track specific order"""
    try:
        order = None
        for o in orders:
            if o.get('id') == order_id:
                order = o
                break
        
        if order:
            return jsonify({
                'success': True,
                'order': order,
                'status': order.get('status', 'confirmed')
            })
        else:
            return jsonify({'success': False, 'message': 'Order not found'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/add_menu_item', methods=['POST'])
def add_menu_item():
    """Add a new menu item"""
    try:
        data = request.json
        name = data.get('name')
        category_name = data.get('category')
        price = data.get('price')
        description = data.get('description', '')
        
        for category in menu_data.get('categories', []):
            if category['name'] == category_name:
                new_id = 1
                for cat in menu_data['categories']:
                    for item in cat['items']:
                        if item['id'] >= new_id:
                            new_id = item['id'] + 1
                
                new_item = {
                    'id': new_id,
                    'name': name,
                    'price': price,
                    'description': description,
                    'category': category_name,
                    'image': f"/static/images/{category_name.lower().replace(' ', '-')}/placeholder.jpg"
                }
                category['items'].append(new_item)
                
                with open('data/menu.json', 'w', encoding='utf-8') as f:
                    json.dump(menu_data, f, indent=2)
                
                return jsonify({'success': True, 'message': 'Item added', 'item': new_item})
        
        return jsonify({'success': False, 'message': 'Category not found'})
    except Exception as e:
        print(f"Error adding item: {e}")
        return jsonify({'success': False, 'message': str(e)})

@app.after_request
def add_header(response):
    """Disable caching for development"""
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

# Add this route to app.py for clearing cart
@app.route('/api/clear_cart', methods=['POST'])
def clear_cart():
    """Clear user's cart"""
    session['cart'] = []
    return jsonify({'success': True, 'message': 'Cart cleared successfully'})

# Add this route to app.py
@app.route('/api/clear_all_orders', methods=['POST'])
def clear_all_orders():
    """Clear all orders (Admin only)"""
    global orders
    orders = []
    
    # Save empty orders
    with open('data/orders.json', 'w', encoding='utf-8') as f:
        json.dump(orders, f, indent=2)
    
    return jsonify({'success': True, 'message': 'All orders cleared'})

@app.route('/api/delete_order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete a specific order"""
    global orders
    orders = [order for order in orders if order.get('id') != order_id]
    
    with open('data/orders.json', 'w', encoding='utf-8') as f:
        json.dump(orders, f, indent=2)
    
    return jsonify({'success': True, 'message': f'Order #{order_id} deleted'})

if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    print("\n" + "="*60)
    print("🚀 SwiftBite AI Starting...")
    print("="*60)
    print(f"✓ Menu loaded: {sum(len(cat.get('items', [])) for cat in menu_data.get('categories', []))} items")
    print(f"✓ Orders loaded: {len(orders)}")
    print("="*60)
    print("\n📍 Server running at: http://localhost:5000")
    print("📍 Admin panel: http://localhost:5000/admin")
    print("\n💡 Test these commands:")
    print("   • 'show menu' - View menu")
    print("   • 'pizza' - Order pizza")
    print("   • 'view cart' - Check cart")
    print("   • 'checkout' - Place order")
    print("\nPress Ctrl+C to stop the server\n")
    print("="*60 + "\n")
    
    app.run(debug=True, port=5000)
