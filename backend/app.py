import logging
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from api.fetch import fetch_audio
from api.validate import validate_url

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__,
            static_folder="../frontend/static",
            template_folder="../frontend/templates")
app.config['DEBUG'] = True
app.config['PORT'] = 5000
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with secure key for production
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Routes for pages
@app.route('/')
@app.route('/home')
def home():
    logger.debug("Rendering home.html")
    return render_template('home.html')

@app.route('/library')
def library():
    try:
        logger.debug("Attempting to render library.html")
        return render_template('library.html')
    except Exception as e:
        logger.error(f"Error rendering library.html: {str(e)}. Falling back to placeholder.html")
        return render_template('placeholder.html')

@app.route('/split')
def split():
    try:
        logger.debug("Attempting to render split.html")
        return render_template('split.html')
    except Exception as e:
        logger.error(f"Error rendering split.html: {str(e)}. Falling back to placeholder.html")
        return render_template('placeholder.html')

@app.route('/help')
def help_page():
    try:
        logger.debug("Attempting to render help.html")
        return render_template('help.html')
    except Exception as e:
        logger.error(f"Error rendering help.html: {str(e)}. Falling back to placeholder.html")
        return render_template('placeholder.html')

@app.route('/about')
def about():
    try:
        logger.debug("Attempting to render about.html")
        return render_template('about.html')
    except Exception as e:
        logger.error(f"Error rendering about.html: {str(e)}. Falling back to placeholder.html")
        return render_template('placeholder.html')

# API endpoints (placeholders)
@app.route('/api/validate', methods=['POST'])
def validate_url_route():
    try:
        data = request.get_json()
        url = data.get('url')
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        result = validate_url(url)
        return jsonify(result), 200 if result['valid'] else 400
    except Exception as e:
        logger.error(f"Error in validate_url: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/fetch', methods=['POST'])
def fetch_audio_route():
    try:
        data = request.get_json()
        url = data.get('url')
        format = data.get('format')
        if not url or not format:
            return jsonify({'error': 'URL and format are required'}), 400
        result = fetch_audio(url, format)
        return jsonify(result), 200 if result['status'] == 'success' else 400
    except Exception as e:
        logger.error(f"Error in fetch_audio: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    logger.info("Starting Flask app on port %s", app.config['PORT'])
    app.run(debug=True, port=app.config['PORT'])