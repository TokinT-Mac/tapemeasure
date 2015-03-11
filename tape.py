from flask import Flask, request, json
import watchdog
app = Flask(__name__)



@app.route('/stat', methods=['GET'])
def stat():
    #data = {}
    #data['cpu'] = loadCpu()
    #data['memory'] = loadMem()
    data = watchdog.getData()
    return json.jsonify(data)


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=2599)
