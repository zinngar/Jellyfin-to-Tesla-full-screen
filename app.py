import os
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Persistence setup
DATA_DIR = os.environ.get('DATA_DIR', './data')
LINKS_FILE = os.path.join(DATA_DIR, 'links.json')

def load_links():
    if not os.path.exists(LINKS_FILE):
        # Create directory if it doesn't exist
        os.makedirs(DATA_DIR, exist_ok=True)
        # Write default links
        with open(LINKS_FILE, 'w') as f:
            json.dump([
                {"Name": "Home Assistant", "Url": "http://homeassistant.local:8123"},
                {"Name": "Jellyfin", "Url": "http://jellyfin.local:8096"}
            ], f, indent=4)

    try:
        with open(LINKS_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading links: {e}")
        return []

def save_links(links):
    os.makedirs(DATA_DIR, exist_ok=True)
    try:
        with open(LINKS_FILE, 'w') as f:
            json.dump(links, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving links: {e}")
        return False

@app.route('/')
def index():
    links = load_links()
    return render_template('index.html', links=links)

@app.route('/api/links', methods=['POST'])
def add_link():
    data = request.get_json()
    if not data or 'Name' not in data or 'Url' not in data:
        return jsonify({"error": "Missing Name or Url"}), 400

    name = data['Name'].strip()
    url = data['Url'].strip()

    if not name or not url:
        return jsonify({"error": "Name and Url cannot be empty"}), 400

    links = load_links()
    # Check if a link with this name already exists
    for link in links:
        if link['Name'].lower() == name.lower():
            return jsonify({"error": f"A link with the name '{name}' already exists"}), 400

    links.append({"Name": name, "Url": url})
    if save_links(links):
        return jsonify({"success": True, "links": links})
    else:
        return jsonify({"error": "Failed to save link to file"}), 500

@app.route('/api/links/delete', methods=['POST'])
def delete_link():
    data = request.get_json()
    if not data or 'Name' not in data:
        return jsonify({"error": "Missing Name"}), 400

    name = data['Name'].strip()
    links = load_links()

    new_links = [l for l in links if l['Name'].lower() != name.lower()]
    if len(new_links) == len(links):
        return jsonify({"error": f"Link with name '{name}' not found"}), 404

    if save_links(new_links):
        return jsonify({"success": True, "links": new_links})
    else:
        return jsonify({"error": "Failed to save changes"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8097, debug=True)
