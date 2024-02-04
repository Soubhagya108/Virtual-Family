# Virtual Family AI Project

Welcome to the Virtual Family AI project for emotional support! This initiative is dedicated to creating a virtual family environment tailored to provide comfort and companionship for orphaned and depressed kids. Through the power of artificial intelligence (AI), we aim to create a safe and nurturing space where children can find solace and understanding.

Table of Contents

Overview

Features

Getting Started

Usage

Contributing

License

Overview

In a world where some children face emotional challenges, our Virtual Family AI project strives to be a source of support and empathy. By leveraging AI technologies, we aim to create virtual family members that provide companionship and encouragement to those who may be going through difficult phases in their lives.

Features

Compassionate AI Characters: Develop virtual family members with compassionate and understanding personalities, designed to provide emotional support.

Interactive Therapy: Implement interactive scenarios and conversations to help children express their emotions and receive virtual companionship.

Personalized Encouragement: Utilize adaptive learning to tailor virtual family members' responses to each child's unique needs, offering personalized encouragement.

Safe and Inclusive Environment: Create a secure and inclusive virtual environment, fostering a sense of belonging and emotional well-being.

Getting Started

To introduce the Virtual Family AI project for emotional support to children, follow these steps:

Clone the Repository:

bash

Copy code

git clone https://github.com/Soubhagya108/Virtual-Family

cd Virtual-Family

Usage

Once the project is up and running, children can interact with the virtual family members through a user-friendly interface. The goal is to provide a comforting and supportive experience, helping them navigate through challenging emotions.

This site is built for the depressed or orphan kids who doesnot have any one such as their father,mother or friend to guide them. That's why we, Team Paradox created this project in order to help them to get through thier bad phase.


Contributing

We invite contributions from individuals who share our vision of providing emotional support to children. This site is created by Soubhagya Vashistha,Mohit Pal and Deepanshu Chauhan from KCC Institute Of Technology And Management.

License

This project belongs to the creators mentioned above and without their permission any part of this site cannot be used.



TEAM PARADOX:
1.Mohit Pal(Front end)
2.Soubhagya Vashisht(Back end)
3.Deepanshu Chauhan(Layout design, Github manage)

TECH USED:
1.HTML
2.CSS
3.JavaScript
4.Python(flask)
5.Open AI-Chat GPT AI
6.Webflow.com
7.Bootstrap

IDEA DESCRIPTION:
We are using AI to help the orphan or depressed or misleading or unguided kids by creating virtual family which guides them as virtual father, mother and friend

FUTURE TECH CHALLENGES

1.EMOTIONAL SUPPORT IN THE DIGITAL AGE: Addressing the growing need for    emotional support in an increasingly technology-driven world.

2.MENTAL HEALTH AND WELL BEING: Offering personalized emotional support to combat rising mental health challenges among children.

3.ADDRESSING SOCIAL ISOLATION: Serving as companions to reduce loneliness and foster a sense of belonging.

4.GUIDANCE AND MEMBERSHIP: Providing tailored guidance and mentorship for children who lack proper role models.

5.EDUCATIONAL SUPPORT: Enhancing educational support through customized learning plans and AI-driven tutoring.

6.PROMOTING POSITIVE BEHAVIOUR: Encouraging positive behavior and decision-making through reinforcement and positive interactions.

7.CULTURAL SENSITIVITY AND INCLUSIVITY: Being adaptable to various cultural contexts, respecting diversity.

8.MITIGATING RESOURCE GAPS: Bridging the gap in situations where traditional support systems are limited.

9.TECHNOLOGICAL EMPOWERMENT: Introducing orphaned or unguided children to technology, fostering digital literacy skills.


HOW TO RUN THE PROJECT:-

First clone the repository 
command >> git clone https://soubhagya108.github.io/Virtual-Family/
command >> pip3 install requirements.txt
command >> python3 aaa.py

By opening the given link, we have given a home page which tells us about the website and the navbar contains the login link, after login we will be redirected toward our AI chat box.

DEPLOYMENT LINK:
https://soubhagya108.github.io/Virtual-Family/index.html
____________________

HTML (index.html):

Defines the structure of the webpage.
Includes input forms, buttons, and other HTML elements for user interaction.
Connects to external stylesheets and scripts.

We have used Webflow for the layout and frontend technologies

we have made 6 html files

index.html >> the basic layout of our website is built
chatbot-login.html >> login interface
menu.html >> made the menu which asks with whom do u want to talk to
boxchat.html >> interface of virtual father
boxmom.html >> interface of virtual mother
boxfriend.html >> interface of virtual friend

CSS (style.css):

Defines the styles and layout of the webpage.
Customizes the appearance of HTML elements.

we have made 3 css files

chatbot.css >> styles index.html
chatbot-login.css >> styles login page css
menu.css >> styles menu.html

css

/* Add your custom styles here */

JavaScript :

Handles user interactions and communicates with the backend.
Uses AJAX to send data to the Flask server and updates the webpage dynamically.

we made 2 js files

index.js
chatbot-login.js


Flask (aaa.py):

Defines routes for handling HTTP requests.
Processes user input, interacts with the ChatGPT API, and returns the result.
python

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
    return open("boxchat.html", "r").read()

@app.route("/api", methods=["POST"])
def api():
    client = OpenAI(api_key= os.environ.get("OPENAI_API_KEY"))

    pre="behave as a father of and instruct the questions asked your name is john"

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

_______________________________

TEAM MATES DETAIL:-

Deepanshu Chauhan
1.Skill- C,C++,HTML,CSS
2.Background- College Student at KCC ITM

Mohit Pal
Skill- C,C++, HTML, CSS, JS, Python, and also a Music Producer
Background- College Student at KCC ITM

Soubhagya Vashistha
Skill- Java, Python, C, HTML, CSS, JS, Bootstrap
Background- College Student at KCC ITM

