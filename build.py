import sys
import os

from resume_data import basic_info, resume_sections

def generate_index_html():
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>欢迎 - {basic_info['name']}的个人主页</title>
    <style>
        body, html {{ margin: 0; padding: 0; height: 100%; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; background: linear-gradient(135deg, #0d47a1 0%, #1e3c72 40%, #2a5298 100%); display: flex; align-items: center; justify-content: center; color: #ffffff; overflow: hidden; }}
        .bg-shape {{ position: absolute; border-radius: 50%; filter: blur(80px); z-index: 0; opacity: 0.5; }}
        .shape1 {{ width: 40vw; height: 40vw; background: rgba(66, 165, 245, 0.4); top: -10vw; left: -10vw; animation: float 10s ease-in-out infinite alternate; }}
        .shape2 {{ width: 30vw; height: 30vw; background: rgba(144, 202, 249, 0.3); bottom: -5vw; right: -5vw; animation: float 12s ease-in-out infinite alternate-reverse; }}
        .container {{ position: relative; text-align: center; z-index: 10; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); padding: 60px 80px; border-radius: 24px; box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2); border: 1px solid rgba(255, 255, 255, 0.2); animation: slideUp 1s cubic-bezier(0.16, 1, 0.3, 1); }}
        h1 {{ font-size: 3.5rem; margin: 0 0 10px 0; font-weight: 600; letter-spacing: 2px; color: #ffffff; }}
        p.subtitle {{ font-size: 1.2rem; color: rgba(255, 255, 255, 0.8); margin-bottom: 40px; letter-spacing: 1px; }}
        .btn {{ display: inline-flex; align-items: center; justify-content: center; padding: 16px 48px; font-size: 1.2rem; color: #1e3c72; background-color: #ffffff; text-decoration: none; border-radius: 50px; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); font-weight: bold; letter-spacing: 1px; position: relative; z-index: 2; }}
        .btn:hover {{ transform: translateY(-4px); box-shadow: 0 15px 35px rgba(0, 0, 0, 0.25); color: #0d47a1; }}
        @keyframes slideUp {{ from {{ opacity: 0; transform: translateY(40px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        @keyframes float {{ 0% {{ transform: translate(0, 0); }} 100% {{ transform: translate(30px, 50px); }} }}
        @media (max-width: 600px) {{ .container {{ padding: 40px 30px; width: 80%; }} h1 {{ font-size: 2.5rem; }} }}
    </style>
</head>
<body>
    <div class="bg-shape shape1"></div>
    <div class="bg-shape shape2"></div>
    <div class="container">
        <h1>{basic_info['home_welcome']}</h1>
        <p class="subtitle">{basic_info['home_subtitle']}</p>
        <a href="resume.html" class="btn">中文简历</a>
    </div>
</body>
</html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated index.html successfully.")

def generate_resume_html():
    sections_html = ""
    for sec in resume_sections:
        sections_html += f"        <section class='cv-section'>\n            <h2>{sec['title']}</h2>\n"
        for item in sec['items']:
            sections_html += f"            <div class='cv-item'>{item}</div>\n"
        sections_html += "        </section>\n"

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{basic_info['name']}的简历</title>
    <style>
        body {{ margin: 0; padding: 40px 20px; background-color: #f7f9fc; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; color: #333; line-height: 1.8; }}
        
        .back-btn {{ position: fixed; top: 20px; left: 20px; color: #666; text-decoration: none; font-size: 0.95rem; padding: 10px 15px; transition: all 0.3s ease; z-index: 1000; display: flex; align-items: center; background: rgba(255,255,255,0.95); border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border: 1px solid #e1e4e8; }}
        .back-btn:before {{ content: "←"; margin-right: 5px; }}
        .back-btn:hover {{ color: #1e3c72; background-color: #f1f3f5; box-shadow: 0 4px 12px rgba(0,0,0,0.12); transform: translateY(-1px); }}
        
        .container {{ max-width: 850px; margin: 0 auto; padding: 50px 60px; background: #fff; box-shadow: 0 10px 40px rgba(0,0,0,0.08); border-radius: 12px; }}
        
        .header {{ text-align: center; margin-bottom: 40px; border-bottom: 2px solid #f1f3f5; padding-bottom: 30px; }}
        .header h1 {{ font-size: 2.8em; margin: 0 0 15px 0; font-weight: 700; color: #1e3c72; letter-spacing: 2px; }}
        .contact-info {{ display: flex; justify-content: center; gap: 25px; flex-wrap: wrap; color: #586069; font-size: 1em; }}
        .contact-info a {{ color: #1e3c72; text-decoration: none; font-weight: 500; transition: all 0.2s; position: relative; }}
        .contact-info a:hover {{ color: #0d47a1; text-decoration: underline; }}
        .contact-icon {{ margin-right: 6px; }}
        
        .cv-section {{ margin-bottom: 40px; }}
        .cv-section h2 {{ font-size: 1.5em; border-bottom: 1px solid #e1e4e8; padding-bottom: 10px; margin-top: 30px; margin-bottom: 20px; font-weight: 700; color: #1e3c72; display: flex; align-items: center; }}
        .cv-section h2::before {{ content: ""; display: inline-block; width: 4px; height: 1.1em; background: #1e3c72; margin-right: 12px; border-radius: 2px; }}
        
        .cv-item {{ margin-bottom: 24px; color: #444; font-size: 1.05em; text-align: justify; padding-left: 16px; border-left: 2px solid transparent; transition: border-left-color 0.3s; }}
        .cv-item:hover {{ border-left-color: #1e3c72; }}
        .cv-item strong {{ font-weight: 600; color: #24292e; }}
        
        @media (max-width: 768px) {{
            .container {{ padding: 30px 20px; margin-top: 50px; }}
            .header h1 {{ font-size: 2.2em; }}
            .contact-info {{ flex-direction: column; gap: 12px; align-items: center; }}
            .back-btn {{ border-radius: 20px; padding: 8px 15px; top: 10px; left: 10px; }}
            body {{ padding: 10px; }}
        }}
    </style>
</head>
<body>
    <a href="index.html" class="back-btn">返回首页</a>
    <div class="container">
        <div class="header">
            <h1>{basic_info['name']}</h1>
            <div class="contact-info">
                <span><span class="contact-icon">📞</span><a href="tel:{basic_info['phone'].replace('-','').replace(' ','')}">{basic_info['phone']}</a></span>
                <span><span class="contact-icon">✉️</span><a href="mailto:{basic_info['email']}">{basic_info['email']}</a></span>
                <span><span class="contact-icon">🌐</span><a href="https://{basic_info['website']}" target="_blank">{basic_info['website']}</a></span>
            </div>
        </div>
        
        <div class="content">
{sections_html}
        </div>
    </div>
</body>
</html>"""
    with open("resume.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated resume.html successfully.")

if __name__ == "__main__":
    generate_index_html()
    generate_resume_html()
    print("All files generated successfully! You can now deploy these HTML files.")
