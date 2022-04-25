"""
Form online untuk pendataan data peserta sebelum kelas AWS dimulai
"""

# Include AWS SDK untuk bahasa Python, serta Flask dan render_template untuk website framework.
import boto3
from flask import Flask, render_template

app = Flask(__name__)
# Menggunakan AWS SDK untuk mengakses service System Manager (SSM) di region tertentu.
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
# Mengecek apakah nama training adalah CPE, jika ya maka Flash tidak mengenerate informasi lab.
    lab = True
    if training == 'Cloud Practitioner Essentials':
        lab = False
# Membuat halaman html dari inputan yang diterima agar bisa ditampilkan ke pengguna.
    return render_template('index.html',training=training,lab=lab)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=80)