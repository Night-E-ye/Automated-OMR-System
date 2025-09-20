import cv2
import numpy as np

# Sheet size
width, height = 800, 600
sheet = np.ones((height, width, 3), dtype=np.uint8) * 255  # white background

# Bubble settings
bubble_radius = 15
x_start = 100
y_start =100
y_gap = 60
x_gap = 60
options = ["A", "B", "C", "D"]

# Draw 5 questions
for q in range(5):
    y = y_start + q * y_gap
    for o, opt in enumerate(options):
        x = x_start + o * x_gap
        cv2.circle(sheet, (x, y), bubble_radius, (0,0,0), 2)  # outline
    # Fill one bubble as “selected” (simulate student answer)
    cv2.circle(sheet, (x_start + 1 * x_gap, y), bubble_radius-3, (0,0,0), -1)  # filled bubble B

# Add question numbers
for q in range(5):
    y = y_start + q * y_gap
    cv2.putText(sheet, f"Q{q+1}", (x_start-60, y+5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 2)

# Save image
cv2.imwrite("dummy_omr.jpg", sheet)
print("Dummy OMR sheet created: dummy_omr.jpg")
