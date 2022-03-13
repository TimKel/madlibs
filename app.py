from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

stories = Flask(__name__)
stories.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(stories)

@stories.route("/")
def ask_questions():
    """Generate and show form to ask words"""
    prompts = story.prompts 

    return render_template("questions.html", prompts=prompts)

@stories.route("/story")
def show_story():
    """Show story result"""
    text = story.generate(request.args)
    return render_template("stories.html", text=text)