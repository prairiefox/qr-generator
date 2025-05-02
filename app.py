from flask import Flask, request, Response
import segno
from io import BytesIO

app = Flask(__name__)

@app.route("/qr")
def generate_qr():
    data = request.args.get("data", "")
    fmt = request.args.get("format", "svg")  # svg or png
    scale = int(request.args.get("scale", "10"))
    border = int(request.args.get("border", "1"))

    qr = segno.make(data, error='l', micro=False)

    buffer = BytesIO()
    qr.save(buffer, kind=fmt, scale=scale, border=border)
    buffer.seek(0)

    return Response(
        buffer.read(),
        mimetype='image/svg+xml' if fmt == 'svg' else 'image/png',
        headers={
            "Content-Disposition": f"attachment; filename=qr.{fmt}"
        }
    )
