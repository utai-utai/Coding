import os

# 配置
TITLE = "我的算法笔记"
BASE_DIR = ""
OUTPUT_FILE = "../index.html"


def generate_html():
    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{TITLE}</title>
        <style>
            body {{ font-family: -apple-system, sans-serif; line-height: 1.6; padding: 15px; background: #f4f7f9; color: #333; }}
            h1 {{ text-align: center; color: #2c3e50; font-size: 1.5rem; margin-bottom: 20px; }}

            /* 折叠框容器 */
            details {{ 
                margin-bottom: 12px; 
                background: white; 
                border-radius: 10px; 
                box-shadow: 0 2px 5px rgba(0,0,0,0.05); 
                overflow: hidden; 
                transition: all 0.3s;
            }}

            /* 未展开时的标题栏 */
            summary {{ 
                padding: 15px; 
                list-style: none; /* 隐藏默认箭头 */
                cursor: pointer;
                outline: none;
                display: flex;
                justify-content: space-between;
                align-items: center;
                font-weight: bold;
                color: #2c3e50;
            }}

            /* 自定义箭头指示器 */
            summary::after {{
                content: '▶';
                font-size: 0.8rem;
                color: #999;
                transition: transform 0.3s;
            }}

            /* 展开后的样式变化 */
            details[open] summary::after {{
                transform: rotate(90deg);
            }}

            details[open] {{
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }}

            ul {{ list-style: none; padding: 0 15px 10px 15px; margin: 0; background: #fff; }}
            li {{ border-top: 1px solid #f0f0f0; }}
            a {{ display: block; padding: 12px 5px; color: #3498db; text-decoration: none; font-size: 0.95rem; }}
            a:active {{ background: #f9f9f9; }}
        </style>
    </head>
    <body>
        <h1>{TITLE}</h1>
    """

    if not os.path.exists(BASE_DIR):
        print(f"错误：找不到 {BASE_DIR} 文件夹")
        return

    subfolders = sorted([f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f))])

    for folder in subfolders:
        folder_path = os.path.join(BASE_DIR, folder)
        html_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.html')])

        if html_files:
            # 使用 details 和 summary 实现折叠
            html_content += f'''
            <details>
                <summary>📂 {folder} ({len(html_files)})</summary>
                <ul>'''
            for f in html_files:
                file_url = f"{BASE_DIR}/{folder}/{f}"
                display_name = f.replace('.html', '').replace('_', ' ')
                html_content += f'<li><a href="{file_url}">{display_name}</a></li>'
            html_content += '</ul></details>'

    html_content += "</body></html>"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"成功！已生成带折叠功能的 {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_html()