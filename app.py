"""
Form online untuk pendataan data peserta sebelum kelas AWS dimulai
"""
import boto3
from flask import Flask, render_template

app = Flask(__name__)
ssm = boto3.client('ssm', region_name="us-east-1")

@app.route('/')
def index():
    """
    Mengambil nama training yang diambil dari System Manager-Parameter Store.
    - Jika tidak ada, maka buat dengan nama parameter yang sama di AWS Console.
    - Buat Task Role untuk container dengan permission ssm:GetParameter di ECS Task Definition.
    - IAM Policy dengan nama AmazonSSMManagedInstanceCore sudah memiliki permission tersebut.
    """
    training = ssm.get_parameter(Name='/belajaraws/course', WithDecryption=False)
    training = training['Parameter']['Value']
    link = ssm.get_parameter(Name='/belajaraws/link', WithDecryption=False)
    link = link['Parameter']['Value']

    return render_template('index.html',training=training,link=link)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=80)