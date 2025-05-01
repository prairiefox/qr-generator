@app.route("/qr")
def generate_qr():
    import io
    data = request.args.get("data", "")
    fmt = request.args.get("format", "svg").lower()
    qr = segno.make(data, error='l')

    buffer = io.BytesIO()

    if fmt == "png":
        qr.save(buffer, kind='png', scale=5, border=0)
        buffer.seek(0)
        return Response(buffer.read(), mimetype='image/png')
    else:
        qr.save(buffer, kind='svg', xmldecl=False, border=0)
        buffer.seek(0)
        return Response(buffer.read(), mimetype='image/svg+xml')
