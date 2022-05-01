from flask import Flask, redirect, url_for, request ,render_template,jsonify, make_response
from urllib.request import Request, urlopen
from model import Summary
import bs4 as bs
import urllib.request
import re
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def scraper(input_url):
    url = str(input_url)
    # opening the url for reading
    html = urllib.request.urlopen(url)
    # parsing the html file 
    htmlParse = bs.BeautifulSoup(html, 'html.parser')
    extracted_data = ''
    # getting all the paragraphs from the html file
    for para in htmlParse.find_all("p"):
        extracted_data += para.get_text()

    return extracted_data

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/output',methods=['POST'])
def output():
    if request.method == 'POST':
        textvalue = request.form.get("textarea", None)
        if textvalue:
            sumObj = Summary()
            summary = sumObj.summary(textvalue)
        else:
            url = request.form.get('url')
            urltext = scraper(url)
            sumObj = Summary()
            summary = sumObj.summary(urltext)
        return render_template('result.html', res=summary)

@app.route("/query")
def query():
    # Gets article URL
    url = request.args.get('article')
    urltext = scraper(url)
    sumObj = Summary()
    summary = sumObj.summary(urltext)
    # Create dictionary 
    test = {
        "summary": "%s" %summary
    }

    # Convert dict to JSON & return
    return jsonify(test)



if __name__ == '__main__':
    app.run(debug=True)
