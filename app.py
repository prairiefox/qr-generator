import segno
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/qr")
def generate_qr():
    data = request.args.get("data", "")
    qr = segno.make(data, error='l')  # ECC = L
    out = qr.to_svg(None, xmldecl=False, border=0)  # Quiet zone = 0
    return Response(out, mimetype='image/svg+xml')
