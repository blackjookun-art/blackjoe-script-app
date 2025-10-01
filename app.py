import streamlit as st

# 初期化：台本履歴の初期化
if "script_history" not in st.session_state:
    st.session_state.script_history = []  # 台本履歴の初期化

# ログインなしで台本作成ページを表示
st.title("ブラックジョー君の台本作成")
st.write("台本作成を始めましょう！")

# 台本作成のテキストエリア
new_script = st.text_area("新しい台本を作成", height=150)

# 保存ボタン
if st.button("台本を保存"):
    if new_script:
        st.session_state.script_history.append(new_script)
        st.success("台本が保存されました！")
    else:
        st.warning("台本が入力されていません。")

# 過去の台本履歴
st.subheader("過去の台本履歴")
if st.session_state.script_history:
    for idx, script in enumerate(st.session_state.script_history):
        st.write(f"{idx + 1}. {script}")
else:
    st.write("まだ台本が作成されていません。")

# 履歴リセット機能
if st.button("履歴をリセット"):
    st.session_state.script_history = []
    st.success("履歴がリセットされました。")
