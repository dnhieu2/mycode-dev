#!/usr/bin/env python3
from flask import Flask, render_template, request
app = Flask(__name__)

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/listofdomains")
def listofdomains():
    gparms = {}

#    for x in groups:
    gparms["hostname"] = request.args.get("hostname", groups["hostname"][0])
    gparms["ip"] = request.args.get("ip", groups["ip"][0])
    gparms["fqdn"] = request.args.get("fqdn", groups["fqdn"][0])
        #gparms["hostname"] = request.args.get("hostname", [0]["hostname"])
        #gparms["hostname"] = request.args.get("hostname", [0]["hostname"])
        #gparms["hostname"] = request.args.get("hostname", [0]["hostname"])
        #gparms["hostname"] = request.args.get("hostname", [0]["hostname"])
        #gparms["hostname"] = request.args.get("hostname", [0]["hostname"])
    return render_template("hellobasic2.html", **gparms)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

