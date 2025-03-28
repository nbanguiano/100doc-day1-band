from flask import Flask, request, render_template, jsonify, send_from_directory, url_for
import os
import mimetypes

# Ensure proper MIME types
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('application/javascript', '.js')

app = Flask(__name__, 
            # static_url_path='/static',
            static_url_path='/100DoC/day1-band/static',
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

# Explicit route for serving static files with proper MIME types
@app.route('/static/<path:filename>')
def serve_static(filename):
    mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
    response = send_from_directory(app.static_folder, filename)
    response.headers['Content-Type'] = mimetype
    return response

if __name__ == '__main__':
    print(f"Static folder is at: {app.static_folder}")
    print(f"Static URL path is: {app.static_url_path}")
    # app.run(debug=True, host='127.0.0.1', port=8080)
    app.run(debug=True)