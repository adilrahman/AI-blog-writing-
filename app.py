from flask import Flask, render_template
import config

app = Flask(__name__)
app.config.from_object(config.config["development"])

# app.register_error_handler(404, page_not_found)

@app.route("/")
def index():
    return render_template("index.html", **locals())



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)