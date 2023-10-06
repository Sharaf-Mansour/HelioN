from flask import Flask
from flask import jsonify
from flask import request 
import pickle
# import joblib
import json 

def Predict(data): 
	# model = pickle.load(open('xg.pkl', 'rb'))
	# prediction = model.predict(data)
	# model = pickle.load('xg.pkl')
	with open('xg.pkl', 'rb') as f: 
		model = pickle.load(f)
	prediction = model.predict(data)
	return data

labels = 'time,proton_vx_gse,proton_vy_gse,proton_vz_gse,proton_vx_gsm,proton_vy_gsm,proton_vz_gsm,proton_speed,proton_density,proton_temperature,hour,dayofweek,quarter,month,year,dayofyear,dayofmonth,weekofyear'.split(',')


def parser(text): 
	arr = text.split(',')
	dic = {}
	for i in range(len(labels)): 
		dic[labels[i]] = arr[i]
	return dic

app = Flask(__name__)

@app.route('/')
def dscvor():
	try: 
		if(request.method == 'GET'): 
			print(str(request.args.get('text')))
			# print(request.args.get('text'))
			parsed = parser(request.args.get('text'))
			parsedAsJsonf = json.dumps(parsed)
			parsedAsJsonf = json.loads(parsedAsJsonf)

			result = Predict(parsedAsJsonf)
			print(result)

			return jsonify(
				result='NOT IMPLEMENTED'
			#result
			)
	except Exception as e: 
		return jsonify({'error': 'something went wrong',
			'error': e})


if __name__ == '__main__':
	app.run()
