Automated OMR Evaluation & Scoring System

Overview

The Automated OMR Evaluation & Scoring System is a Python-based web application that automates the grading of OMR (Optical Mark Recognition) sheets. Using OpenCV and NumPy, it detects filled bubbles (A/B/C/D), calculates per-subject and total scores, and generates overlay images for visual verification. Built with a Streamlit web interface, it supports multiple subjects, sheet versions, and customizable answer keys. Evaluators can upload OMR sheets, view results instantly, and export scores as CSV. This system reduces manual errors, speeds up evaluation, and is ideal for hackathons, educational institutions, and placement readiness assessments.

Features

1. Upload OMR sheets via Streamlit web interface
2. Automatic detection of filled bubbles (A/B/C/D)
3. Per-subject and total score calculation
4. Overlay visualization of detected bubbles (green = filled, red = empty)
5. Supports multiple subjects and sheet versions
6. Export results as CSV
7. Flexible JSON template for question layout and answer keys

Tech Stack

1. Python 3.x
2. OpenCV – image processing and bubble detection
3. NumPy – data manipulation
4. Streamlit – web interface
5. JSON – template configuration

Installation

1. Clone the repository:

git clone https://github.com/Night-E-ye/Automated-OMR-System.git
cd Automated-OMR-System

2. Install dependencies:

   pip install -r requirements.txt

3. Run the Streamlit app:

   streamlit run app.py

4. Upload OMR sheets in the web interface to see scores and overlay images.


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
