from peewee import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
	render_template, flash, current_app
from models import *


app = Flask(__name__,template_folder="templates", static_url_path="/static",
            static_folder="static")
app.config.from_object(__name__)


def init_db():
	ConnectDatabase.db.connect()
	ConnectDatabase.db.drop_tables([Story], safe=True)
	ConnectDatabase.db.create_tables([Story], safe=True)


@app.route('/')
@app.route('/list')
def show_stories():
	stories = Story.select().order_by(Story.id)
	return render_template('list.html', stories=stories)


@app.route('/story', methods=['GET'])
def add_new_story():
	story = []
	return render_template('form.html', story=story, header='Create story', button='Create')

@app.route('/story', methods=['POST'])
def save_new_story():
	new_record = Story.create(title=request.form['title'],
							   text=request.form['text'],
							   criteria=request.form['criteria'],
							   business_value=request.form['business_value'],
							   estimation=request.form['estimation'],
							   status=request.form['status'])
	return redirect(url_for('show_stories'))

@app.route('/story/<story_id>', methods=['GET'])
def edit_story(story_id):
	story = Story.get(Story.id==story_id)
	return render_template("form.html", story=story, header="Edit story", button="Update")


@app.route('/story/<story_id>', methods=['POST'])
def update_story(story_id):
	edit_record = Story.update(title=request.form['title'],
							   text=request.form['text'],
							   criteria=request.form['criteria'],
							   business_value=request.form['business_value'],
							   estimation=request.form['estimation'],
							   status=request.form['status']).where(Story.id==story_id)
	return redirect(url_for('show_stories'))

@app.route('/delete/<story_id>', methods=['POST'])
def delete_story(story_id):
	story = Story.select().where(Story.id==story_id).get()
	story.delete_instance()
	return redirect(url_for('show_stories'))

if __name__=='__main__':
	init_db()
	app.run(debug=True)
