import segno
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/qr")
def generate_qr():
    data = request.args.get("data", "")
    fmt = request.args.get("format", "svg").lower()

    qr = segno.make(data, error='l')  # ECC = L

    if fmt == "png":
        out = qr.png_as_base64_str(scale=5, border=0)
        return Response(
            response=bytes.fromhex(out),
            content_type="image/png"
        )
    else:  # default to SVG
        out = qr.to_svg(None, xmldecl=False, border=0)
        return Response(out, mimetype="image/svg+xml")
