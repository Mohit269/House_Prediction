from flask import Flask, render_template, request
import joblib
app = Flask(__name__)
model = joblib.load("predict_model.pkl")
@app.route('/')
def base():
	return render_template('base1.html')
@app.route('/price')
def houses():
	return render_template('base.html')
@app.route('/price',methods =['POST'])
def house():
    if request.method=='POST':
	    Income=float(request.form['Income'])
	    House=float(request.form['House'])
	    Rooms=float(request.form['Rooms'])
	    BedRooms=float(request.form['BedRooms'])
	    Population=float(request.form['Population'])
	    house=str(model.predict([[Income,House,Rooms,BedRooms,Population]]))
    return render_template('base.html', prices=house)
if __name__ == '__main__':
    app.run(debug=True)    