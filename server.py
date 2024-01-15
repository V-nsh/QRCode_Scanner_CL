from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/qr-code', methods=['POST'])
def process_qr_code():
    data = decode('qr_code_data')
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    else:
        return None
    # Your logic to process the QR code data goes here
    # For example, you can print it
    print("QR Code Data:", data)

    # Respond with some data back to the front end
    response_data = {"message": "QR code data received successfully"}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
