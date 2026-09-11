from config import HF_API_KEY
import requests
import base64
import os
from colorama import init, Fore
init(autoreset=True)
URL = "https://router.huggingface.co/v1/chat/completions"
MODELS_URL = "https://router.huggingface.co/v1/models"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}
def get_models():

    try:

        r = requests.get(
            MODELS_URL,
            headers=HEADERS,
            timeout=30
        )

        if r.status_code == 200:
            return r.json().get("data", [])

    except Exception:
        pass

    return []


def find_model(keywords):

    models = get_models()
    for kw in keywords:
        kw_lower = kw.lower()
        for model in models:
            model_id = model.get("id", "")
            if kw_lower in model_id.lower():
                return model_id

    return None


def get_vision_model():

    return find_model([
        "qwen2.5-vl",
        "qwen-vl",
        "llava",
        "pixtral",
        "vision"
    ])


# ==========================================================

def get_text_model():

    return find_model([
        "llama-3.3-70b",
        "qwen2.5-72b",
        "qwen2.5",
        "deepseek-v3",
        "mistral",
        "gemma"
    ])



def image_to_base64(path):

    ext = os.path.splitext(path)[1].lower()

    mime = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp"
    }.get(
        ext,
        "image/jpeg"
    )

    with open(path, "rb") as f:

        data = base64.b64encode(
            f.read()
        ).decode()

    return f"data:{mime};base64,{data}"


# ============================================================
# ASK AI
# ============================================================

def ask_api(model, messages, tokens=200):

    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": tokens,
        "temperature": 0.3
    }

    try:

        r = requests.post(
            URL,
            headers=HEADERS,
            json=payload,
            timeout=120
        )

        if r.status_code != 200:

            return None, (
                f"Error {r.status_code}: "
                f"{r.text}"
            )

        data = r.json()

        text = (
            data["choices"][0]
            ["message"]
            .get("content", "")
        )

        return text.strip(), None

    except Exception as e:

        return None, str(e)


# ============================================================
# STEP 1: VISION MODEL
# ============================================================

def caption_image(image_path):

    model = get_vision_model()

    if not model:

        return None, (
            "No vision model available"
        )

    print(
        f"\n{Fore.CYAN}"
        f"👀 Vision Model: {model}"
    )

    image_data = image_to_base64(
        image_path
    )

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "Look at this school bag image. "
                        "List the objects you can see. "
                        "Keep the answer simple."
                    )
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_data
                    }
                }
            ]
        }
    ]

    return ask_api(
        model,
        messages,
        tokens=100
    )


# ============================================================
# STEP 2: TEXT MODEL
# ============================================================

def make_shopping_list(objects):

    model = get_text_model()

    if not model:

        return None, (
            "No text model available"
        )

    print(
        f"\n{Fore.GREEN}"
        f"✍️ Text Model: {model}"
    )

    prompt = f"""
You are helping a student organize
their school bag.

The vision model found these objects:

{objects}

Create a simple checklist of useful
school items the student should have.

Do not invent many items.
Use only the objects mentioned above.
"""

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    return ask_api(
        model,
        messages,
        tokens=150
    )


# ============================================================
# MAIN PROGRAM
# ============================================================

print("\n====================================")
print("       🎒 SCHOOL BAG HELPER")
print("====================================")

image_path = input(
    "\nEnter the image path: "
).strip().strip("'\"")


# Check image path

if not os.path.exists(image_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    alt_path = os.path.join(script_dir, image_path)
    if os.path.exists(alt_path):
        image_path = alt_path

if not os.path.exists(image_path):

    print(
        f"\n{Fore.RED}"
        "❌ Image not found."
    )

else:

    # --------------------------------------------------------
    # VISION MODEL
    # --------------------------------------------------------

    objects, error = caption_image(
        image_path
    )

    if error:

        print(
            f"\n{Fore.RED}"
            f"❌ {error}"
        )

    else:

        print("\n👀 What I can see:")
        print(objects)


        # ----------------------------------------------------
        # TEXT MODEL
        # ----------------------------------------------------

        result, error = make_shopping_list(
            objects
        )

        if error:

            print(
                f"\n{Fore.RED}"
                f"❌ {error}"
            )

        else:

            print(
                "\n✍️ Your School Bag Checklist:"
            )

            print(result)


print("\n====================================")
print("              DONE")
print("====================================")