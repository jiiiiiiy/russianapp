from flask import Flask, render_template, jsonify, request
import psycopg2
import openai


app = Flask(__name__)

# OpenAI API 설정
openai.api_key = "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"

# PostgreSQL 데이터베이스 연결 설정
DATABASE_URL = "postgresql://postgres:jin2577019!@db.ajdnnumrcdvtmmrrxtpp.supabase.co:5432/postgres"
conn = psycopg2.connect(DATABASE_URL)

# 데이터베이스로부터 데이터 가져오기

def fetch_topics_duplicate():
    with conn.cursor() as cur:
        cur.execute("SELECT id, image_url, korean_sentence, russian_sentence, name FROM topics_duplicate ORDER BY id, name")
        topics_duplicate = cur.fetchall()
    return topics_duplicate

@app.route('/')
def index():
    topics_duplicate = fetch_topics_duplicate()
    return render_template('index.html', topics_duplicate=topics_duplicate)



if __name__ == '__main__':
    app.run(debug=True)
