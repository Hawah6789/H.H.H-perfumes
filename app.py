from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>H.H.H Perfumes</h1>
    <h2>Luxury Fragrances</h2>

    <p>Welcome to H.H.H Perfumes.</p>

    <h3>Our Collection</h3>

    <ul>
        <li>Oud Royal</li>
        <li>Rose Elegance</li>
        <li>Midnight Amber</li>
    </ul>

    <button>Shop Now</button>
    """

if __name__ == "__main__":
    app.run(debug=True)