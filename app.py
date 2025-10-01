import streamlit as st
import openai
import os

# OpenAI APIキー
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    st.error("OpenAI APIキーが設定されていません")
    st.stop()

# 履歴リストの初期化（セッション中）
if "script_history" not in st.session_state:
    st.session_state.script_history = []

# --------------------
# :チェックマーク_緑: メイン画面
# --------------------
st.title("ブラックジョー君の台本作成")

# :小さいひし形_青: 台本作成ボタン
if st.button("台本を作成する"):
    with st.spinner("台本を生成中..."):
        prompt = """
あなたは、YouTubeショートでバズるための「台本職人AI」です。
以下の条件をすべて満たす、60秒以内のショート動画用の台本を1本作成してください：
【目的】
・日本の若者（10〜30代）向けにバズるショート動画台本を作成する
・ブラックユーモア、皮肉、アメリカンジョーク、腹黒ネタ、ちょいスケベ（R-15以内）を含める
【構成】
・最初の3秒で視聴者の注意を引く「強烈なフック」
・短いセリフで展開し、視聴者の共感 or 驚き or 笑いを引き出す
・ラストに「オチ」でインパクトを残す（爆笑 / 皮肉 / 逆転 / セクシーな余韻など）
・話者は1～2名まで（会話形式でセリフは明確に）
【重要な条件】
・毎回、登場人物、シチュエーション、展開、オチは変えること（ワンパターン禁止）
・YouTubeショートのトレンドや、若者の関心事、SNSや日常生活で"ありそうなネタ"をベースにする
・ネタは日本人向けの文化・文脈に沿ったものにする（例：LINE、コンビニ、就活、バイト、マッチングアプリ、ゲーム、カラオケ、学校、SNSなど）
【出力フォーマット】
【タイトル】：（YouTubeショート用の強いタイトル）
【台本】：（セリフ形式で改行、話者ごとに「男：」「女：」などを明記）
【タグ】：（YouTubeにアップロードする際に使える10個のタグ）
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response['choices'][0]['message']['content']

        # 履歴に追加（最大50件まで）
        st.session_state.script_history.insert(0, result)
        if len(st.session_state.script_history) > 50:
            st.session_state.script_history = st.session_state.script_history[:50]

        st.success("台本が生成されました！")
        st.text_area("生成された台本", result, height=500)

# --------------------
# :複数の本: 履歴サイドバー
# --------------------
st.sidebar.title("過去の台本履歴")
if st.session_state.script_history:
    for i, script in enumerate(st.session_state.script_history):
        if st.sidebar.button(f"履歴 {i+1}", key=f"history_{i}"):
            st.text_area(f"履歴 {i+1} の台本", script, height=500)
else:
    st.sidebar.write("（まだ台本がありません）")
