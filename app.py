import io
import segno
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/qr")
def generate_qr():
    import io
    data = request.args.get("data", "")
    fmt = request.args.get("format", "svg").lower()

    qr = segno.make(data, error='l', micro=False)  # ⬅️ FULL QR + lowest ECC
    buffer = io.BytesIO()

    if fmt == "png":
        qr.save(buffer, kind='png', scale=10, border=2)
        buffer.seek(0)
        return Response(buffer.read(), mimetype='image/png')
    else:
        qr.save(buffer, kind='svg', xmldecl=False, scale=10, border=2)
        buffer.seek(0)
        return Response(buffer.read(), mimetype='image/svg+xml')
