from flask import Flask, redirect, url_for, request

from comet import load_from_checkpoint

app = Flask(__name__)
model = load_from_checkpoint('./checkpoints/model.ckpt')

@app.route('/qe',methods = ['POST'])
def login():
    if request.method == 'POST':
        src = request.form['src']
        mt = request.form['mt']
        data = [
            {
                "src": src,
                "mt": mt,
            }
        ]
        model_output = model.predict(data, batch_size=8, gpus=0)

        return str(model_output[-1])

if __name__ == '__main__':
    app.run(debug = True)