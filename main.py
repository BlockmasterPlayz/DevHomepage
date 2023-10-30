from flask import Flask, render_template, request
import webbrowser

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/searchtext", methods = ["POST"])
def Searchtext():
    query = request.form.get("query")
    new_query = ""
    for letter in query:
        # print(letter)
        if letter == " ":
            letter = "+"
        new_query += letter

    webbrowser.open(f"https://www.google.com/search?q={new_query}&client=safari&sca_esv=577734576&sxsrf=AM9HkKlKYxPyWD_slVV0ZF3wiIqoN1CwRA:1698651467274&source=hp&ei=S10_ZcbIDpuA2roPi_itmAo&iflsig=AO6bgOgAAAAAZT9rW1QDA0I8jRtDNNB1kJsX1qEFIE0F&ved=0ahUKEwiGmrXqoZ2CAxUbgFYBHQt8C6MQ4dUDCAk&uact=5&oq=What+is+dev+ops&gs_lp=Egdnd3Mtd2l6Ig9XaGF0IGlzIGRldiBvcHMyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGAoyBxAAGIAEGApIrBZQAFiXFHAAeACQAQCYAYICoAHJFqoBBjAuMTEuNLgBA8gBAPgBAcICBxAjGIoFGCfCAgQQIxgnwgIOEAAYigUYsQMYgwEYkQLCAggQABiKBRiRAsICCxAuGIAEGLEDGIMBwgILEAAYgAQYsQMYgwHCAgsQABiKBRixAxiDAcICBRAAGIAEwgIIEAAYgAQYsQPCAg0QABiABBgUGIcCGLEDwgIIEAAYigUYsQM&sclient=gws-wiz&safe=active")
    return render_template("Index.html")

if __name__ == "__main__":
    app.run(debug=True)