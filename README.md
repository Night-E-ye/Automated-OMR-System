Automated OMR Evaluation & Scoring System

Project Overview

The Automated OMR Evaluation & Scoring System is a Python-based web application that automates the grading of OMR (Optical Mark Recognition) sheets. Using OpenCV and NumPy, it detects filled bubbles (A/B/C/D), calculates per-subject and total scores, and generates overlay images for visual verification. Built with a Streamlit web interface, it supports multiple subjects, sheet versions, and customizable answer keys. Evaluators can upload OMR sheets, view results instantly, and export scores as CSV. This system reduces manual errors, speeds up evaluation, and is ideal for hackathons, educational institutions, and placement readiness assessments.

Features

Upload OMR sheets via Streamlit web interface

Automatic detection of filled bubbles (A/B/C/D)

Per-subject and total score calculation

Overlay visualization of detected bubbles (green = filled, red = empty)

Supports multiple subjects and sheet versions

Export results as CSV

Flexible JSON template for question layout and answer keys

Tech Stack

Python 3.x

OpenCV – image processing and bubble detection

NumPy – data manipulation

Streamlit – web interface

JSON – template configuration

Installation

Clone the repository:

git clone https://github.com/Night-E-ye/Automated-OMR-System.git
cd Automated-OMR-System


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py


Upload OMR sheets in the web interface to see scores and overlay images.

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


Overlay images show green rectangles for filled bubbles and red rectangles for empty bubbles.

License

This project is licensed under the MIT License.
