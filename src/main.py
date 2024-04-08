from flask import Flask
import pandas as pd

app = Flask(__name__)

def generate_html_from_dataframe(df):
    html = "<h1>Student Data</h1>"
    html += df.to_html(index=False)
    return html

@app.route('/')
def index():
    data = {
        'First Name': ['LATTAB', 'AZZAOUI'],
        'Last Name': ['Nassim', 'Mohamed'],
        'Student Number': ['123456789', '987654321']
    }
    df = pd.DataFrame(data)
    return generate_html_from_dataframe(df)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)