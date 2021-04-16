from PIL import Image, ImageFont, ImageDraw 
from flask import Flask
from flask import send_file
import os




app = Flask(__name__)

@app.route('/<name>', methods=['GET'])
def vote(name: str):
    image_source = Image.open("denis_src/denis.jpg")
    title_font = ImageFont.truetype('font/WaitingfortheSunrise-Regular.ttf', 50)
    results = {"name" : name}
    try:
        name = str(name)        
        title_text = name
        filepath = "api-generated-images/"+name+".jpg"
        image_editable = ImageDraw.Draw(image_source)
        image_editable.text((550,400), title_text, (0, 0, 0), font=title_font)
        image_source.save(filepath)    
        return send_file(filepath, "image/jpeg")
    except ValueError:
        results["error"] = "le vote n'est pas passé, snif"
        return results, 500



if __name__ == '__main__':
    app.run(host="0.0.0.0")
