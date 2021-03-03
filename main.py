from flask import Flask, render_template, request, Response
import pandas as pd
import pickle

output_train_test=pd.read_csv(r'output_train_test.csv')
product_info=pickle.load(open(r'product_info','rb'))
all_order = list(output_train_test.order_id.unique())

app = Flask(__name__)
@app.route('/')
def first():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    id = [int(x) for x in request.form.values()]
    id=int(id[0])

    if id in all_order :
        product_name = list(output_train_test[output_train_test.order_id == id]['products'])
        product_name=product_name[0].split()
        product_name = [product_info[int(i)] for i in product_name]
        return Response(render_template('prediction.html', data=product_name))
    else:
        message='Please, enter valid  Order_id '
        return Response(render_template('invalid.html', data=message))

if __name__ == '__main__':
    app.run(debug=True)
