# ObjectOracle MVP

画像をアップロードすると、OpenAIの画像理解を使って哲学的な詩を返す最小構成アプリです。

## セットアップ

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=your_api_key
python app.py
```

ブラウザで `http://127.0.0.1:5000` を開いて画像をアップロードしてください。

## MVP仕様

- 画像1枚アップロード
- 日本語の自由詩（6〜10行）を生成
- エラーハンドリング（未選択・APIキー未設定・API失敗）

## 次フェーズ候補

- 生成詩の保存履歴
- 詩のトーン切替（ニヒリズム/希望/叙情）
- SNSシェア画像出力
