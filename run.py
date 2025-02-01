from ext import app  # Import the app instance from ext
from routes import register_routes  # Import the function to register routes

# Register the routes in the app
register_routes(app)

# Run the app on all available interfaces (host="0.0.0.0")
app.run(host="0.0.0.0")
