import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_DIR = 'uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'png'])

app = Flask( __name__ )
prefix = '/diafilm'

def checkfile( filename ):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route( prefix + '/' )
def index():
     return "\n".join( open( 'tpl/index.mst', "r" ).readlines() )

@app.route( prefix + '/get' )

@app.route( prefix + '/upload', methods = ['POST'] )
def upload():
	status = ''
	if request.method == 'POST' and request.files['img']:
		file = request.files['img']
		if checkfile( file.filename ):
			filename = secure_filename( file.filename )
			file.save( os.path.join( app.config['UPLOAD_DIR'], filename ) )
			status = 'ok'
	
	return status

if __name__ == "__main__":
	app.debug = True
	app.config['UPLOAD_DIR'] = UPLOAD_DIR
	app.run()