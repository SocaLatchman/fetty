from flask import Flask, render_template
from dotenv import load_dotenv
import os, random

load_dotenv('.env')
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') 


def get_random_image():
    '''
    get all the images from a directory, iterate over them and if its a
    hidden file skip it. If its not, append it the file name to a list
    and return a random item from the list.
    '''
    image_list = []
    img_dir = os.getcwd() + "/static/images/giphy"
    with os.scandir(img_dir) as images:
        for image in images:
            if image.name.startswith('.'):
                continue
            else:
                image_list.append(image.name)
    return random.choice(image_list)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', random_image=get_random_image())



if __name__ == '__main__':
    app.run(debug=True)
