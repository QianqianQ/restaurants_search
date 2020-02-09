from search_app import create_app, config

app = create_app(config.DevelopmentConfig)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
