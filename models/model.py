# /app/model.py
from config import config
import io
from PIL import Image
from ultralytics import YOLO

SKIN_MODEL_PATH = config.SKIN_MODEL_PATH
SKIN_IMAGE_SIZE = config.SKIN_IMAGE_SIZE
model = YOLO(SKIN_MODEL_PATH)
skin_class_names = config.skin_class_names

# skin
def classification_skin(image_bytes: bytes):
    try:
        # 이미지 입력
        image = Image.open(io.BytesIO(image_bytes))
        # 예측
        results = model(image, imgsz = SKIN_IMAGE_SIZE, verbose=False)
        result = results[0]
        probs = result.probs
        ans_idx = probs.top1
        conf = probs.top1conf.item()
        predicted_class_name = skin_class_names[ans_idx]

        return {
            "predicted_class": predicted_class_name,
            "confidence": f"{conf:.4f}",
            "class_index": ans_idx,
        }

    except Exception as e:
        print(f"Error : {e}")

# eye
def classification_eye():
    return