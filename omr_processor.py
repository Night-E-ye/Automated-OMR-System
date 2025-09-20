import cv2


def evaluate_omr(image_path, answer_key, template):
    """
    Evaluate an OMR sheet image.

    Parameters:
    - image_path: path to OMR sheet image
    - answer_key: list of correct answers ["A", "B", ...]
    - template: JSON template defining bubble coordinates and subjects

    Returns:
    - result dict with:
        - student_answers: list of detected answers
        - subject_scores: dict per subject
        - total_score: int
        - overlay: image with detected bubbles highlighted
    """

    # 1 Read and preprocess image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    student_answers = []
    overlay = img.copy()
    filled_threshold = 0.2  # fraction of area to consider bubble filled

    # 2️ Detect filled bubbles for each question
    for q in template["questions"]:
        selected_option = None

        for idx, opt in enumerate(template["options"]):
            x = q["x"] + idx * q.get("x_gap", 0)
            y = q["y"]
            w, h = q["width"], q["height"]

            bubble = thresh[y:y+h, x:x+w]
            filled_ratio = cv2.countNonZero(bubble) / (w*h)

            if filled_ratio > filled_threshold:
                selected_option = opt
                cv2.rectangle(overlay, (x, y), (x+w, y+h), (0,255,0), 2)  # green = filled
            else:
                cv2.rectangle(overlay, (x, y), (x+w, y+h), (0,0,255), 1)  # red = empty

        student_answers.append(selected_option)

    # 3️ Calculate per-subject scores
    subject_scores = {}
    for subject, bounds in template["subjects"].items():
        correct = 0
        for i in range(bounds["start"], bounds["end"]+1):
            if i < len(student_answers) and student_answers[i] == answer_key[i]:
                correct += 1
        subject_scores[subject] = correct

    # 4️ Calculate total score correctly (use General if defined)
    total_score = subject_scores.get("General", sum(
        subject_scores[subject] for subject in template["subjects"] if subject != "General"
    ))

    # 5️ Return results
    result = {
        "student_answers": student_answers,
        "subject_scores": subject_scores,
        "total_score": total_score,
        "overlay": overlay
    }

    return result




