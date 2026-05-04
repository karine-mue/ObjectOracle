import base64
import os
from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)


def image_to_data_url(file_storage):
    mime = file_storage.mimetype or "image/jpeg"
    b64 = base64.b64encode(file_storage.read()).decode("utf-8")
    return f"data:{mime};base64,{b64}"


def generate_philosophical_poem(image_data_url: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "You are a poetic philosopher. Produce a short Japanese free-verse poem (6-10 lines) inspired by the uploaded image. Blend concrete observation with existential reflection. Avoid cliches.",
            },
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": "この画像から哲学的な詩を書いて。"},
                    {"type": "input_image", "image_url": image_data_url},
                ],
            },
        ],
    )
    return response.output_text.strip()


@app.route("/", methods=["GET", "POST"])
def index():
    poem = None
    error = None

    if request.method == "POST":
        file = request.files.get("image")
        if not file or file.filename == "":
            error = "画像を選んでください。"
        elif not os.getenv("OPENAI_API_KEY"):
            error = "OPENAI_API_KEY が設定されていません。"
        else:
            try:
                image_data_url = image_to_data_url(file)
                poem = generate_philosophical_poem(image_data_url)
            except Exception as exc:
                error = f"生成中にエラーが発生しました: {exc}"

    return render_template("index.html", poem=poem, error=error)


if __name__ == "__main__":
    app.run(debug=True)
