import streamlit as st
import openai
import os
# :閉じた錠と鍵: 環境変数からAPIキー取得
openai.api_key = os.getenv("OPENAI_API_KEY")
# :閉じた錠と鍵: ログインパスワード設定（ハードコードOK）
PASSWORD = "blackloe"
# :閉じた錠と鍵: ログイン認証
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if not st.session_state.authenticated:
    st.title("ログイン")
    password = st.text_input("パスワードを入力", type="password")
    if password == PASSWORD:
        st.session_state.authenticated = True
        st.experimental_rerun()
    else:
        st.stop()
else:
    # メイン画面
    st.title("ブラックジョー君の台本作成")
    if st.button("作成する"):
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
            st.success(":チェックマーク_緑: 台本が生成されました")

            st.text_area(":文書: 台本", result, height=500)

