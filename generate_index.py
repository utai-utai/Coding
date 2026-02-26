import os

# 配置：导航页标题和扫描目录
TITLE = "我的算法笔记"
BASE_DIR = "tutorial"
OUTPUT_FILE = "index.html"


def generate_html():
    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{TITLE}</title>
        <style>
            body {{ font-family: -apple-system, sans-serif; line-height: 1.6; padding: 20px; background: #f4f7f9; color: #333; }}
            h1 {{ text-align: center; color: #2c3e50; }}
            .category {{ margin-bottom: 20px; background: white; padding: 15px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }}
            h2 {{ font-size: 1.1rem; color: #3498db; border-left: 4px solid #3498db; padding-left: 10px; margin-top: 0; }}
            ul {{ list-style: none; padding: 0; margin: 0; }}
            li {{ border-bottom: 1px solid #eee; }}
            li:last-child {{ border-bottom: none; }}
            a {{ display: block; padding: 12px 5px; color: #555; text-decoration: none; word-break: break-all; }}
            a:active {{ background: #f0f7ff; color: #3498db; }}
        </style>
    </head>
    <body>
        <h1>{TITLE}</h1>
    """

    # 遍历 tutorial 文件夹
    if not os.path.exists(BASE_DIR):
        print(f"错误：找不到 {BASE_DIR} 文件夹")
        return

    # 获取所有子文件夹
    subfolders = sorted([f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f))])

    for folder in subfolders:
        folder_path = os.path.join(BASE_DIR, folder)
        html_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.html')])

        if html_files:
            html_content += f'<div class="category"><h2>📂 {folder}</h2><ul>'
            for f in html_files:
                # 生成相对路径链接
                file_url = f"{BASE_DIR}/{folder}/{f}"
                display_name = f.replace('.html', '').replace('_', ' ')
                html_content += f'<li><a href="{file_url}">{display_name}</a></li>'
            html_content += '</ul></div>'

    html_content += "</body></html>"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"成功！已生成 {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_html()