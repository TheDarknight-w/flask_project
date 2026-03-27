from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb+srv://joelchinta7_db_user:<db_pass>2@cluster2.owf086t.mongodb.net/?appName=Cluster2")
db = client["todo_db"]
collection = db["items"]
#index.html contains itemid and description and data goes to mongo db
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Hello API"})

@app.route('/submittodoitem', methods=['POST'])
def submit():
    data = request.json

    item = {
        "itemName": data.get('itemName'),
        "itemDescription": data.get('itemDescription')
    }

    collection.insert_one(item)

    return jsonify({"status": "stored in mongodb"})

if __name__ == '__main__':
    app.run(debug=True)
