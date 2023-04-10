# Import necessary libraries
import os
from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    # Get the paths of the smaller images
    smaller_images_path = '/static/smaller_images'
    smaller_image_files = os.listdir(smaller_images_path)

    # Get the path of the larger image
    larger_image_path = '/static/larger_image.jpg'

    # Render the template with the image paths
    return render_template('/templates/index.html', smaller_images=smaller_image_files, larger_image=larger_image_path)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
