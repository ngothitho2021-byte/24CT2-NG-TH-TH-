from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chào mừng bạn</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #a8c0ff 0%, #3f2b96 100%);
                height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .card {
                background: white;
                padding: 40px 30px;
                border-radius: 20px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
                text-align: center;
                max-width: 420px;
                width: 90%;
            }
            h1 {
                color: #2b5876;
                margin-bottom: 10px;
                font-size: 28px;
            }
            p.sub {
                color: #555;
                font-size: 15px;
                line-height: 1.5;
            }
            .info-box {
                background: #f4f6f9;
                border-radius: 12px;
                padding: 15px;
                margin: 20px 0;
            }
            .info-box h3 {
                margin: 0 0 8px 0;
                color: #3f2b96;
                font-size: 16px;
            }
            .btn {
                display: inline-block;
                background: #3f2b96;
                color: white;
                padding: 12px 28px;
                border-radius: 25px;
                text-decoration: none;
                font-weight: bold;
                transition: 0.3s;
            }
            .btn:hover {
                background: #2b1d69;
            }
            .footer {
                margin-top: 15px;
                font-size: 12px;
                color: #888;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Chào mừng bạn!</h1>
            <p class="sub"><b>Chào bạn khóa 24CT đến với học phần CNPM-DAU</b></p>
            
            <div class="info-box">
                <h3>📘 Lập trình Web với FastAPI</h3>
                <p style="margin:0; font-size: 13px; color: #666;">Chúc bạn học tập thật tốt, sáng tạo và đạt kết quả cao! 🚀</p>
                <p style="margin-top: 8px; font-size: 12px; color: #e91e63;">FastAPI Framework ❤️</p>
            </div>

            <a href="/docs" class="btn">🚀 Bắt đầu học</a>
            <div class="footer">© 2026 - 24CT2 | CNPM-DAU</div>
        </div>
    </body>
    </html>
    """
    return html_content
