# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN python app/models.py

# Expose the port that the Streamlit app will run on
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "run.py"]
