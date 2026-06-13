from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>H.H.H Perfumes - Shop</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                background: #0f0f0f;
                color: white;
            }

            .header {
                text-align: center;
                padding: 40px;
                background: linear-gradient(90deg, #111, #333);
            }

            .header h1 {
                margin: 0;
                font-size: 40px;
                color: #d4af37;
            }

            .header p {
                color: #d4af37;
                font-size: 18px;
            }

            .container {
                text-align: center;
                padding: 30px;
            }

            .grid {
                display: flex;
                justify-content: center;
                gap: 20px;
                flex-wrap: wrap;
                margin-top: 20px;
            }

            .product {
                background: #1c1c1c;
                padding: 20px;
                width: 250px;
                border-radius: 12px;
                box-shadow: 0 0 10px rgba(0,0,0,0.5);
            }

            .product img {
                width: 100%;
                height: 250px;
                object-fit: cover;
                border-radius: 10px;
            }

            .product h3 {
                color: #d4af37;
            }

            .price {
                margin: 10px 0;
                font-weight: bold;
                color: #d4af37;
                font-size: 20px;
            }

            .btn {
                background: #d4af37;
                border: none;
                padding: 12px;
                width: 100%;
                cursor: pointer;
                font-weight: bold;
                border-radius: 6px;
            }

            .btn:hover {
                background: white;
            }

            footer {
                margin-top: 50px;
                padding: 20px;
                text-align: center;
                background: #111;
                color: #aaa;
            }
        </style>
    </head>

    <body>

        <div class="header">
            <h1>H.H.H PERFUMES</h1>
            <p>Luxury Fragrance Online Shop</p>
        </div>

        <div class="container">
            <h2>Our Products</h2>

            <div class="grid">

                <div class="product">
                    <img src="/static/images/oud-royal.jpg">
                    <h3>Oud Royal</h3>
                    <p>Deep Arabian luxury scent</p>
                    <div class="price">$45</div>
                    <a href="https://wa.me/256745176042?text=I%20want%20to%20buy%20Oud%20Royal">
                        <button class="btn">Buy on WhatsApp</button>
                    </a>
                </div>

                <div class="product">
                    <img src="/static/images/rose-elegance.jpg">
                    <h3>Rose Elegance</h3>
                    <p>Soft floral premium perfume</p>
                    <div class="price">$40</div>
                    <a href="https://wa.me/256745176042?text=I%20want%20to%20buy%20Rose%20Elegance">
                        <button class="btn">Buy on WhatsApp</button>
                    </a>
                </div>

                <div class="product">
                    <img src="/static/images/midnight-amber.jpg">
                    <h3>Midnight Amber</h3>
                    <p>Warm evening fragrance</p>
                    <div class="price">$50</div>
                    <a href="https://wa.me/256745176042?text=I%20want%20to%20buy%20Midnight%20Amber">
                        <button class="btn">Buy on WhatsApp</button>
                    </a>
                </div>

                <div class="product">
                    <img src="/static/images/strawberry-bliss.jpg">
                    <h3>Strawberry Bliss</h3>
                    <p>Sweet fruity luxury fragrance</p>
                    <div class="price">$35</div>
                    <a href="https://wa.me/256745176042?text=I%20want%20to%20buy%20Strawberry%20Bliss">
                        <button class="btn">Buy on WhatsApp</button>
                    </a>
                </div>

                <div class="product">
                    <img src="/static/images/golden-musk.jpg">
                    <h3>Golden Musk</h3>
                    <p>Elegant long-lasting fragrance</p>
                    <div class="price">$55</div>
                    <a href="https://wa.me/256745176042?text=I%20want%20to%20buy%20Golden%20Musk">
                        <button class="btn">Buy on WhatsApp</button>
                    </a>
                </div>

                <div class="product">
                    <img src="/static/images/royal-velvet.jpg">
                    <h3>Royal Velvet</h3>
                    <p>Luxury premium fragrance</p>
                    <div class="price">$60</div>
                    <a href="https://wa.me/256745176042?text=I%20want%20to%20buy%20Royal%20Velvet">
                        <button class="btn">Buy on WhatsApp</button>
                    </a>
                </div>

            </div>
        </div>

        <footer>
            <p>WhatsApp Orders: +256 745 176042</p>
            <p>© 2026 H.H.H Perfumes | All Rights Reserved</p>
        </footer>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)