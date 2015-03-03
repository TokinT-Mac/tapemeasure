from flask import Flask, request, json

app = Flask(__name__)

def loadStats():
    with file('/proc/stat', 'r') as stats:
        cpus = {}
        for line in stats:
            if line[:3] == 'cpu':
                l = line.split(" ")
                if "" in l:
                    l.remove("")

                cpus[l[0]] = l[1:4]
    return cpus

@app.route('/stat', methods=['GET'])
def stat():
    return json.jsonify(loadStats())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2599)
