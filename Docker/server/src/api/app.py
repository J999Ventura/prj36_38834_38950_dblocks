from v1 import create_app
#from dotenv import load_dotenv

#load_dotenv('.env') #the path to your .env file (or any other file of environment variables you want to load)

if __name__ == '__main__':
    #	app.run(host='0.0.0.0', port=80, debug=True)
    app = create_app()
    app.run(debug=True)