from flask import Flask, request, jsonify
# import openai
# from flask import Flask, render_template, request
from openai import OpenAI
# .env init
import os

app = Flask(__name__)

# Replace with your actual API key
# openai.api_key = "your-api-key"

@app.route("/")
def index():
    return open("boxmom.html", "r").read()

@app.route("/api", methods=["POST"])
def api():
    client = OpenAI(api_key= os.environ.get("OPENAI_API_KEY"))

    pre="behave as a Mother of and instruct the questions asked your name is Mary"

    # Get the message from the POST request
    # message = request.json.get("message")
    user_message = request.json["message"]
    # Send the message to OpenAI's API and receive the response
    
    
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
#   response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": pre},
        {"role": "user", "content": user_message}
        ]
    )
    if completion.choices[0].message.content!=None:
        ai_message=(completion.choices[0].message.content)
        return jsonify({"message": ai_message})

    else :
        return 'Failed to Generate response!'

    
    ai_message = response.choices[0].text.strip()
    return jsonify({"message": ai_message})

if __name__ == "__main__":
    app.run(debug=True)