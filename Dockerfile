# Use the official Python image from Docker Hub
FROM python

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install dependencies
RUN pip install --verbose -r requirements.txt

# Set PYTHONPATH to include specific directories
ENV PYTHONPATH="/usr/src/app/src:/usr/src/app/src/stubs:${PYTHONPATH}"

# Display PYTHONPATH for debugging (optional)
RUN echo $PYTHONPATH

# Run the Flask application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
