import cv2
import os
import tempfile
import pytesseract
from pdf2image import convert_from_path


def extract_text_from_image(image_path, language):
    extracted_text = pytesseract.image_to_string(
        image_path,
        lang=language,
    )
    return extracted_text


def DATA_EXTRACTION_2_PARTS(
    pdf_path, left_partition, right_partition, lang_part_first, lang_part_second
):
    images = convert_from_path(pdf_path)

    left_folder = "left"
    right_folder = "right"
    os.makedirs(left_folder, exist_ok=True)
    os.makedirs(right_folder, exist_ok=True)
    first_part_text = ""
    second_part_text = ""

    for page_num, image in enumerate(images):
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
            image_path = temp_file.name
            image.save(image_path, "JPEG")

            img = cv2.imread(image_path)

            h, w, channels = img.shape

            left_cut = int(w * 0.01 * float(left_partition))
            right_cut = int(w * 0.01 * float(right_partition))

            left_part = img[:, :left_cut]
            right_part = img[:, -right_cut:]

            left_image_path = os.path.join(left_folder, f"left_{page_num + 1}.jpg")
            right_image_path = os.path.join(right_folder, f"right_{page_num + 1}.jpg")

            cv2.imwrite(left_image_path, left_part)
            cv2.imwrite(right_image_path, right_part)

            extracted_text_part_first = extract_text_from_image(
                left_image_path, lang_part_first
            )
            first_part_text += extracted_text_part_first

            extracted_text_part_second = extract_text_from_image(
                right_image_path, lang_part_second
            )
            second_part_text += extracted_text_part_second

            temp_file.close()
            os.remove(image_path)

    return first_part_text, second_part_text
