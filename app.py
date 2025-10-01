import streamlit as st
# 初期化
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
# パスワードの設定（ここで自分のパスワードを設定）
PASSWORD = "blackjoe"  # ここに自分のパスワードを設定
# ログイン画面の処理
if not st.session_state.authenticated:
    st.title("ログイン")
    input_pw = st.text_input("パスワードを入力してください", type="password")  # パスワード入力
    # パスワードが正しいか確認
    if input_pw == PASSWORD:
        st.session_state.authenticated = True
        st.experimental_rerun()  # ログイン後にページを再読み込み
    elif input_pw:
        st.error("パスワードが間違っています。")  # パスワードが間違っている場合にエラー表示
else:
    # ログイン後の画面（台本作成など）
    st.title("ブラックジョー君の台本作成")
    st.write("ログインしました！")
    # ここから台本作成の処理を追加
    st.text_area("台本作成用のテキストエリア", height=200)
    # 過去の台本履歴を表示
    if "script_history" not in st.session_state:
        st.session_state.script_history = []  # 初期化（最初は履歴が空）
    # 過去の履歴を表示
    st.subheader("過去の台本履歴")
    if st.session_state.script_history:
        for idx, script in enumerate(st.session_state.script_history):
            st.write(f"{idx + 1}. {script}")
    else:
        st.write("まだ台本が作成されていません。")
    # 台本作成後に履歴に保存
    new_script = st.text_area("新しい台本を作成", height=150)
    if st.button("台本を保存"):
        if new_script:
            st.session_state.script_history.append(new_script)
            st.success("台本が保存されました！")
        else:
            st.warning("台本が入力されていません。")
    # その他の処理（例：履歴を削除する機能など）
    if st.button("履歴をリセット"):
        st.session_state.script_history = []
        st.success("履歴がリセットされました。")

