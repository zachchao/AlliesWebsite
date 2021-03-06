import json
from flask import Flask
from flask import render_template, request
from flask import Markup

app = Flask(__name__)

@app.route('/')
def home():
    with open("projects.json") as f:
        projectData = json.loads(f.read())
    with open("workExperience.json") as f:
        workExperienceData = json.loads(f.read())
    with open("activities.json") as f:
        activitiesData = json.loads(f.read())

    return render_template('index.html', 
    	projectData=projectData,
    	workExperienceData=workExperienceData,
    	activitiesData=activitiesData,
    	researchIntersts=[
	    	"Integrated computational materials engineering",
            "solid-state engineering",
            "materials data science",
            "corrosion",
            "failure analysis",
            "wastewater treatment",
            "sustainable materials"
    	],
    	navBarTextColor = "#FFFFFF",
    	# backgroundColor = "#93A8AC",
    	# bannerColor = "9B6A6C",
    	# headerTextColor = "#424B54",
    	# cardBackgroundColor = "#FFFFFF",
    	# bannerTextColor = "#FFFFFF",
    	# cardOutlineColor = "#B4D2E7",
    	# cardHeaderColor = "#424B54",
    	# cardTextColor = "#93A8AC"
    )

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=90, debug=True)
