from flask import Flask, request, render_template_string

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
    
    # Terminal-styled HTML
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Day 1 - Band Name Generator</title>
        <style>
            body {
                background-color: #1e1e1e;
                color: #f0f0f0;
                font-family: 'Courier New', monospace;
                padding: 20px;
                max-width: 800px;
                margin: 0 auto;
                line-height: 1.5;
            }
            .terminal {
                background-color: #121212;
                border-radius: 5px;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0,0,0,0.5);
                border: 1px solid #333;
            }
            .prompt {
                color: #4CAF50;
                display: flex;
                align-items: center;
                margin-bottom: 15px;
            }
            .prompt::before {
                content: "$ ";
                margin-right: 5px;
            }
            .prompt-label {
                color: #4CAF50;
                margin-right: 10px;
            }
            input[type="text"] {
                background-color: transparent;
                border: none;
                color: #f0f0f0;
                font-family: 'Courier New', monospace;
                font-size: 16px;
                flex-grow: 1;
                outline: none;
            }
            input[type="text"]:focus {
                border-bottom: 1px solid #4CAF50;
            }
            input[type="submit"] {
                background-color: #2e2e2e;
                color: #4CAF50;
                border: 1px solid #4CAF50;
                font-family: 'Courier New', monospace;
                padding: 8px 16px;
                margin-top: 20px;
                cursor: pointer;
                font-size: 14px;
            }
            input[type="submit"]:hover {
                background-color: #3e3e3e;
            }
            .output {
                background-color: #1e1e1e;
                border-left: 3px solid #4CAF50;
                padding: 10px;
                margin-top: 20px;
                white-space: pre-wrap;
            }
            h1 {
                color: #4CAF50;
                border-bottom: 1px solid #333;
                padding-bottom: 10px;
            }
            .cursor {
                display: inline-block;
                width: 10px;
                height: 18px;
                background-color: #4CAF50;
                animation: blink 1s step-end infinite;
            }
            @keyframes blink {
                0%, 100% { opacity: 1; }
                50% { opacity: 0; }
            }
        </style>
    </head>
    <body>
        <h1>> Band Name Generator v1.0.0</h1>
        <div class="terminal">
            <form method="POST">
                <div class="prompt">
                    <span class="prompt-label">Enter city you grew up in:</span>
                    <input type="text" name="input1" autocomplete="off">
                </div>
                <div class="prompt">
                    <span class="prompt-label">Enter your pet's name:</span>
                    <input type="text" name="input2" autocomplete="off">
                </div>
                <input type="submit" value="EXECUTE COMMAND">
            </form>
            {% if result %}
            <div class="output">
                $ generating band name...
                $ process completed!
                
                {{ result }}
            </div>
            {% endif %}
        </div>
        <script>
            // Auto-focus on first input when page loads
            document.addEventListener('DOMContentLoaded', function() {
                document.querySelector('input[name="input1"]').focus();
            });
        </script>
    </body>
    </html>
    '''
    
    return render_template_string(html, result=result)

if __name__ == '__main__':
    app.run(debug=True)