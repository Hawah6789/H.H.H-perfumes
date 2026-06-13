from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>H.H.H Perfumes</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                background-color: #0f0f0f;
                color: white;
            }

            .header {
                background: linear-gradient(90deg, #111, #333);
                padding: 40px;
                text-align: center;
            }

            .header h1 {
                font-size: 40px;
                margin: 0;
                letter-spacing: 2px;
            }

            .header p {
                color: #d4af37;
                font-size: 18px;
            }

            .container {
                padding: 40px;
                text-align: center;
            }

            .products {
                display: flex;
                justify-content: center;
                gap: 20px;
                flex-wrap: wrap;
                margin-top: 30px;
            }

            .card {
                background-color: #1c1c1c;
                padding: 20px;
                width: 200px;
                border-radius: 12px;
                box-shadow: 0 0 10px rgba(0,0,0,0.5);
            }

            .card h3 {
                color: #d4af37;
            }

            .btn {
                margin-top: 30px;
                padding: 12px 25px;
                border: none;
                background-color: #d4af37;
                color: black;
                font-weight: bold;
                cursor: pointer;
                border-radius: 8px;
            }

            .btn:hover {
                background-color: white;
            }

            footer {
                margin-top: 50px;
                padding: 20px;
                text-align: center;
                background-color: #111;
                font-size: 14px;
                color: #aaa;
            }
        </style>
    </head>

    <body>

        <div class="header">
            <h1>H.H.H PERFUMES</h1>
            <p>Luxury Fragrances for Royal Lifestyle</p>
        </div>

        <div class="container">
            <h2>Our Collection</h2>

            <div class="products">
                <div class="card">
                    <h3>Oud Royal</h3>
                    <p>Deep, rich Arabian oud fragrance.</p>
                </div>

                <div class="card">
                    <h3>Rose Elegance</h3>
                    <p>Soft floral luxury scent.</p>
                </div>

                <div class="card">
                    <h3>Midnight Amber</h3>
                    <p>Warm, bold evening perfume.</p>
                </div>
            </div>

            <button class="btn">Shop Now</button>
        </div>

        <footer>
            © 2026 H.H.H Perfumes | All Rights Reserved
        </footer>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)