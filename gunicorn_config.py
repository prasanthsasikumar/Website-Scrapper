bind = '0.0.0.0:8000'  # The address and port Gunicorn should bind to
workers = 4  # The number of worker processes to spawn
module = 'viewApp:app'  # Replace with the module and application object of your web app
errorlog = '/home/ubuntu/Website-Scrapper/gunicorn_error.log'