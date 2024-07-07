from flask import Flask

# create an instance of Flask
app = Flask(__name__)

# route decorator binds a function to a URL
@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <p>Smirth S.: idk it just makes it easier than spelling out the whole thing</p>
        <p>Francisco L.: lol since it sounds better than laugh out loud</p>
        <p>Oscar A.: frs i use it to say for sures or for reals</p>
    </body>
    </html>
    '''

@app.route('/maria')
def hello_maria():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <p>Maria S.: omw is my favorite and i use it all the time when i am letting my friends know im on my way to pick them up.</p>
        <div class="text-center">
            <img src="https://i.natgeofe.com/k/9acd2bad-fb0e-43a8-935d-ec0aefc60c2f/monarch-butterfly-grass_3x2.jpg" class="rounded w-50" style="height: 200px;" style="width: 100px;">
        </div>
    </body>
    </html>
    '''
if __name__ == '__main__':
    app.run(debug=True)