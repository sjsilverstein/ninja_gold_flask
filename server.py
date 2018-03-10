from flask import Flask, render_template, request, redirect, session
import random
import time
import datetime
app = Flask(__name__)
app.secret_key = 'test2' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
@app.route('/') #This is the root
def index():
	if 'gold' not in session:
		session['gold'] = 0
	if 'activities_log' not in session:
		session['activities_log'] = []
	if 'length' not in session:
		session['length'] = 0
	return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def process_money():
	building = str(request.form['building'])
	farmv = random.randint(10, 20)
	cavev = random.randint(5, 10)
	housev = random.randint(2, 5)
	casinov = random.randint(-50,50)
	timestamp = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
	buildingsList = [['farm', farmv], ['cave', cavev], ['house', housev], ['casino', casinov]]
	for i in range(0,len(buildingsList)):
		if building == buildingsList[i][0]:
			session['gold'] = session['gold'] + buildingsList[i][1]
			if buildingsList[i][1] >= 0:
				session['activities_log'].append(['pos','Earned '+ str(buildingsList[i][1]) + ' gold from the'+str(building)+ '! ' + str(timestamp)])
				session.modified = True
			else:
				session['activities_log'].append(['neg','Entered a '+str(building)+' and lost '+str(buildingsList[i][1])+' gold...Ouch.. ' + str(timestamp)])
				session.modified = True
	session['length'] = len(session['activities_log'])
	return redirect('/')


app.run(debug=True)