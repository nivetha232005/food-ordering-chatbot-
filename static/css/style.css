* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    transition: all 0.3s ease;
}

body.dark {
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
}

/* Navbar */
.navbar {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
}

body.dark .navbar {
    background: rgba(30, 30, 30, 0.95);
    color: white;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: #667eea;
}

.logo i {
    margin-right: 10px;
}

.nav-links {
    display: flex;
    gap: 20px;
    align-items: center;
}

.nav-link {
    text-decoration: none;
    color: #333;
    transition: color 0.3s;
}

body.dark .nav-link {
    color: white;
}

.cart-btn, .theme-toggle {
    background: none;
    border: none;
    cursor: pointer;
    font-size: 1.2rem;
    position: relative;
    padding: 8px;
    border-radius: 50%;
    transition: background 0.3s;
}

.cart-btn:hover, .theme-toggle:hover {
    background: rgba(0, 0, 0, 0.1);
}

.cart-count {
    position: absolute;
    top: -5px;
    right: -5px;
    background: #ff4757;
    color: white;
    border-radius: 50%;
    padding: 2px 6px;
    font-size: 0.7rem;
}

/* Hero Section */
.hero {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: white;
}

.hero-content h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.highlight {
    color: #ffd700;
}

.chat-trigger-btn {
    margin-top: 2rem;
    padding: 1rem 2rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    border-radius: 50px;
    color: white;
    cursor: pointer;
    font-size: 1.1rem;
    transition: transform 0.3s;
}

/* Menu Section */
.menu-section {
    padding: 4rem 2rem;
    background: #f8f9fa;
}

body.dark .menu-section {
    background: #1a1a1a;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
}

.section-title {
    text-align: center;
    margin-bottom: 2rem;
    font-size: 2rem;
}

.category-tabs {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}

.category-btn {
    padding: 0.5rem 1.5rem;
    border: none;
    background: white;
    border-radius: 25px;
    cursor: pointer;
    transition: all 0.3s;
}

.category-btn.active {
    background: #667eea;
    color: white;
}

.menu-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 2rem;
}

.menu-card {
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s;
}

body.dark .menu-card {
    background: #2d2d2d;
    color: white;
}

.menu-card:hover {
    transform: translateY(-5px);
}

.menu-card-image {
    height: 200px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 4rem;
    color: white;
}

.menu-card-content {
    padding: 1rem;
}

.price {
    font-size: 1.5rem;
    font-weight: bold;
    color: #667eea;
    margin: 0.5rem 0;
}

.add-to-cart-btn {
    width: 100%;
    padding: 0.5rem;
    background: #667eea;
    border: none;
    border-radius: 8px;
    color: white;
    cursor: pointer;
    transition: background 0.3s;
}

/* Chatbot Widget */
.chatbot-widget {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 350px;
    height: 500px;
    background: white;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    display: flex;
    flex-direction: column;
    z-index: 1000;
    transition: all 0.3s;
    transform: scale(0);
    transform-origin: bottom right;
}

.chatbot-widget.open {
    transform: scale(1);
}

.chatbot-widget.minimized {
    height: 60px;
}

.chatbot-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 1rem;
    border-radius: 15px 15px 0 0;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.chatbot-messages {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
}

.message {
    display: flex;
    gap: 10px;
    margin-bottom: 1rem;
    animation: fadeIn 0.3s;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.message-avatar {
    width: 35px;
    height: 35px;
    border-radius: 50%;
    background: #667eea;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
}

.message.user .message-avatar {
    background: #ff4757;
}

.message-content {
    flex: 1;
    padding: 0.5rem 1rem;
    background: #f0f0f0;
    border-radius: 10px;
}

.message.user .message-content {
    background: #667eea;
    color: white;
}

.quick-suggestions {
    display: flex;
    gap: 0.5rem;
    margin-top: 0.5rem;
    flex-wrap: wrap;
}

.suggestion-btn {
    padding: 0.25rem 0.75rem;
    background: white;
    border: 1px solid #667eea;
    border-radius: 20px;
    font-size: 0.8rem;
    cursor: pointer;
    transition: all 0.3s;
}

.suggestion-btn:hover {
    background: #667eea;
    color: white;
}

.chatbot-input {
    padding: 1rem;
    border-top: 1px solid #e0e0e0;
    display: flex;
    gap: 0.5rem;
}

.chatbot-input input {
    flex: 1;
    padding: 0.5rem;
    border: 1px solid #e0e0e0;
    border-radius: 25px;
    outline: none;
}

.voice-input, .send-message {
    width: 40px;
    height: 40px;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    transition: all 0.3s;
}

.voice-input {
    background: #ff4757;
    color: white;
}

.send-message {
    background: #667eea;
    color: white;
}

/* Floating Chat Button */
.floating-chat-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    color: white;
    font-size: 1.5rem;
    cursor: pointer;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    z-index: 999;
    transition: transform 0.3s;
}

.floating-chat-btn:hover {
    transform: scale(1.1);
}

/* Cart Sidebar */
.cart-sidebar {
    position: fixed;
    top: 0;
    right: -400px;
    width: 400px;
    height: 100vh;
    background: white;
    box-shadow: -5px 0 20px rgba(0, 0, 0, 0.1);
    z-index: 1100;
    transition: right 0.3s;
    display: flex;
    flex-direction: column;
}

.cart-sidebar.open {
    right: 0;
}

.cart-header {
    padding: 1rem;
    background: #667eea;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.cart-items {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
}

.cart-footer {
    padding: 1rem;
    border-top: 1px solid #e0e0e0;
}

.checkout-btn {
    width: 100%;
    padding: 0.75rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    border-radius: 8px;
    color: white;
    cursor: pointer;
    font-size: 1rem;
}

/* Responsive */
@media (max-width: 768px) {
    .chatbot-widget {
        width: 100%;
        height: 100%;
        bottom: 0;
        right: 0;
        border-radius: 0;
    }
    
    .cart-sidebar {
        width: 100%;
        right: -100%;
    }
    
    .menu-grid {
        grid-template-columns: 1fr;
    }
    
    .hero-content h1 {
        font-size: 2rem;
    }
}
