from flask import Flask, render_template
# Memasukkan AWS SDK untuk Python.
import boto3

app = Flask(__name__)
# Menggunakan AWS SDK untuk mengakses service System Manager (SSM) di region tertentu.
ssm = boto3.client('ssm', region_name="us-east-1")

@app.route('/')
def index():
# Mengambil nama training yang diambil dari System Manager - Parameter Store. Harap buat System Manager - Parameter Store dengan nama parameter yang sama di AWS Console. Buat IAM Role untuk container dengan permission ssm:GetParameter ke Task Role di ECS Task Definition. IAM Policy dengan nama AmazonSSMManagedInstanceCore sudah memiliki permission tersebut.
    training = ssm.get_parameter(Name='/belajaraws/course', WithDecryption=False)
    training = training['Parameter']['Value']
# Mengecek apakah nama training-nya adalah Cloud Practitioner Essentials. Kalau iya, maka Flask tidak akan menampilkan informasi lab. Hal ini dikarenakan kelas Cloud Practitioner Essentials tidak menyediakan lab.
    lab = True
    if training == 'Cloud Practitioner Essentials':
      lab = False
# Membuat halaman html dari inputan yang diterima agar bisa ditampilkan ke pengguna.
    return render_template('index.html',training=training,lab=lab)

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=80)