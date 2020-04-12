from v1 import create_app

if __name__ == '__main__':
    #	app.run(host='0.0.0.0', port=80, debug=True)
    app = create_app()
    app.run(debug=True)