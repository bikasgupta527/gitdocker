FROM python:3.7-slim

# Copy code to the container image.
ADD app.py /

RUN pip install Flask jsonify Flask-Cors Flask-JSON Flask-RESTful

EXPOSE 5000

CMD [ "python", "./app.py","--host", "0.0.0.0" ]
