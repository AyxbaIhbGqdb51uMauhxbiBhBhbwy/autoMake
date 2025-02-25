from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

PASTEBIN_API_URL = "https://pastebin.com/api/api_post.php"
PASTEBIN_API_KEY = "MIqSmaGlSwMyJ2rtVvTKGnPNVr4zMmfe"  # Masukkan API Key langsung

@app.route("/create_paste", methods=["POST"])
def create_paste():
    paste_name = "SUBSCRIBE"
    paste_data = "https://discord.gg/juRYbcKdYW"
    
    payload = {
        "api_dev_key": PASTEBIN_API_KEY,
        "api_option": "paste",
        "api_paste_private": "0",
        "api_paste_name": paste_name,
        "api_paste_expire_date": "N",
        "api_paste_format": "lua",
        "api_paste_code": paste_data
    }
    
    response = requests.post(PASTEBIN_API_URL, data=payload)
    if response.status_code == 200:
        return jsonify({"paste_url": response.text})
    else:
        return jsonify({"error": "Failed to create paste"}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
