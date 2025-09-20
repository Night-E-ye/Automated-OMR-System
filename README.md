# Automated-OMR-System
Automated OMR Evaluation &amp; Scoring System using Python and OpenCV. Upload OMR sheets via web interface, detect filled bubbles, calculate per-subject and total scores, visualize results with overlays, and export CSV. Fast, accurate, and ideal for hackathons, exams, and placement assessments.

#Project Overview

The Automated OMR Evaluation & Scoring System is a Python-based web application designed to automate grading of OMR (Optical Mark Recognition) sheets. Traditional manual evaluation is time-consuming, error-prone, and resource-intensive. This system enables evaluators to process large batches of OMR sheets quickly and accurately, making it ideal for hackathons, schools, universities, and placement assessments.

#Features

Upload OMR sheets through a Streamlit web interface.

Automatic detection of filled bubbles (A/B/C/D) using OpenCV.

Calculates per-subject scores and total score.

Generates overlay images showing detected bubbles (green = filled, red = empty).

Supports multiple subjects, sheet versions, and customizable answer keys.

Export results as CSV for easy record-keeping.

Flexible JSON template for question layout and coordinates.

#Tech Stack

Python 3.x – core programming language

OpenCV – image preprocessing and bubble detection

NumPy – data manipulation and calculations

Streamlit – interactive web application

JSON – configurable templates for questions and subjects




Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py


Upload OMR sheets in the web interface and view results.

Usage

Upload OMR sheet images (JPEG/PNG).

The system automatically detects filled bubbles.

View per-subject scores, total score, and overlay image.

Download CSV results for record-keeping.

Template & Answer Key

Define question layout, options, and subjects in templates/template.json.

Provide the correct answers in answer_key for evaluation.

Example Output
Per-subject scores:
{
  "Math": 2,
  "Physics": 1,
  "Chemistry": 1,
  "English": 1,
  "General": 5
}
Total score: 5


Overlay image shows green rectangles on filled bubbles, red rectangles on empty ones.

License

This project is licensed under the MIT License.
