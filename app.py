from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        input1 = request.form.get('input1')
        input2 = request.form.get('input2')
        
        def your_function(input1, input2):
            return f"Your band name could be: {input1} {input2}"
        
        result = your_function(input1, input2)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)