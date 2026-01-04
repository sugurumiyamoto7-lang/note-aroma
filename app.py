import streamlit as st
import datetime
import google.generativeai as genai

st.title("🔮 今日の運勢 × アロマ（Note用）")

st.write("日付を選んで『生成する』を押すだけで、Note用文章が出ます。")

api_key = st.text_input("Gemini API Key（最初だけ入力）", type="password")
date = st.date_input("日付", datetime.date.today())

if st.button("生成する"):
    if not api_key:
        st.error("APIキーを入力してください")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
あなたは「占い×アロマ」を毎日Noteで配信する日本語ライター。

【日付】{date.strftime("%Y年%m月%d日")}

必ずMarkdown形式で出力すること。

## 今日の運勢
## 仕事運
## 恋愛運
## 健康運
## 金運
## 今日のラッキーアクション
## 今日のおすすめアロマ
## 香りの使い方（朝・昼・夜）
## ひとこと締め
## タイトル案（3つ）
## ハッシュタグ（10個以内）
"""
        result = model.generate_content(prompt)
        st.text_area("Note貼り付け用Markdown", result.text, height=500)
