from flask import Flask, request, render_template

@app.route("/")

def home():
    return "<h1>This is home page</h1>

@app.route("/predict", methods=["GET", "POST"])
def predict():
    return "<h1>This is predict page</h1>

if __name__ == "__main__":
    app.run()



        
