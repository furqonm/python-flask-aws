from flask import Flask, render_template
import boto3

app = Flask(__name__)
ssm = boto3.client('ssm', region_name="us-east-1")

@app.route('/')
def index():
    training = ssm.get_parameter(Name='/belajaraws/course', WithDecryption=False)
    training = training['Parameter']['Value']
    lab = True
    if training == 'Cloud Practitioner Essentials':
      lab = False
    return render_template('index.html',training=training,lab=lab)

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=80)