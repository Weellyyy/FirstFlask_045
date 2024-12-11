from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nama = request.form.get('Nama')
    umur = request.form.get('Umur')
    alamat = request.form.get('Alamat')
    jenis_kelamin = request.form.get('Jenis_Kelamin')
    keluhan = request.form.get('Keluhan')
    tanggal_pendaftaran = request.form.get('Tanggal_Pendaftaran')
    jam_pendaftaran = request.form.get('Jam_Pendaftaran')
    return render_template(
        'response.html',
        nama=nama,
        umur=umur,
        alamat=alamat,
        jenis_kelamin=jenis_kelamin,
        keluhan=keluhan,
        tanggal_pendaftaran=tanggal_pendaftaran,
        jam_pendaftaran=jam_pendaftaran
    )

if __name__ == '__main__':
    app.run(debug=True)
