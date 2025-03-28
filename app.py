from flask import Flask, request, render_template, jsonify, send_from_directory
import os

app = Flask(__name__, 
            static_url_path='/static',
            static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input1 = request.form.get('input1')
        input2 = request.form.get('input2')
        
        def your_function(input1, input2):
            return f"Your band name could be: {input1} {input2}"
        
        result = your_function(input1, input2)
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'result': result})
        return render_template('index.html', result=result)
    
    return render_template('index.html')

# Explicit route for serving static files (as a backup)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    print(f"Static folder is at: {app.static_folder}")
    print(f"Static URL path is: {app.static_url_path}")
    # app.run(debug=True, host='127.0.0.1', port=5000)
    app.run(debug=True)