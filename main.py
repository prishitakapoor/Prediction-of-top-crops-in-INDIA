from flask import Flask,request,jsonify

import numpy as np
import pickle
import os


app = Flask(__name__)

model = pickle.load(open("label_pst.pkl", "rb"))
ind_to_crop_dict = pickle.load(open("index-to-crop.pkl", "rb"))
district_dict = pickle.load(open("district.pkl", "rb"))

@app.route('/', methods=['GET'])
def index():
    state = request.args.get('state')
    district=request.args.get('district')
    
    if district in district_dict:
        district_val = district_dict[district]
    else:
        district_val = 0
        
    #print(district)
    season=request.args.get('season')
    #print(season)
    
    lst = [[state, district_val, season]]
    arr = np.asarray(lst, dtype=int)
    
    #print(type(arr))
    
    pred_val = model.predict(arr)
    
    pred_ans = pred_val.todense()
    #print(pred_ans)
    
    pred_ans = np.asarray(pred_ans)
    #print(type(pred_ans))
    
    pred_ans = pred_ans.reshape(36,)
    #print(pred_ans.shape)
    ind = np.argpartition(pred_ans, -3)[-3:]

    ans_lst = []
    
    for i in ind.tolist():
        if i in ind_to_crop_dict:
            #print(ind_to_crop_dict[i])
            ans_lst.append(ind_to_crop_dict[i])

    #print(ans_lst)    
    
    return jsonify(result=ans_lst)
    
    
    
    
    
    
if __name__ == "__main__":
	#decide what port to run the app in
	port = int(os.environ.get('PORT', 5000))
	#run the app locally on the givn port
    
	app.run(host='0.0.0.0', port=port)
	#optional if we want to run in debugging mode
	#app.run(debug=True)
