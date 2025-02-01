from ext import app  # Import the app instance
from routes import register_routes  # Import route registration function

# Register routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
