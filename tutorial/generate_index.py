import os

# 获取脚本所在的当前文件夹 (即 tutorial 文件夹)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# 强制把 index.html 生成在 tutorial 文件夹内
OUTPUT_FILE = os.path.join(CURRENT_DIR, "index.html")
TITLE = "算法笔记库"


def generate_html():
    # 打印确认一下路径
    print(f"📍 脚本位置: {CURRENT_DIR}")
    print(f"📝 目标文件: {OUTPUT_FILE}")

    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{TITLE}</title>
        <style>
            body {{ font-family: -apple-system, sans-serif; line-height: 1.6; padding: 15px; background: #f4f7f9; }}
            h1 {{ text-align: center; color: #2c3e50; font-size: 1.5rem; }}
            details {{ margin-bottom: 12px; background: white; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }}
            summary {{ padding: 15px; cursor: pointer; display: flex; justify-content: space-between; font-weight: bold; }}
            summary::after {{ content: '▶'; font-size: 0.8rem; color: #999; }}
            details[open] summary::after {{ transform: rotate(90deg); }}
            ul {{ list-style: none; padding: 0 15px 10px 15px; margin: 0; }}
            li {{ border-top: 1px solid #f0f0f0; }}
            a {{ display: block; padding: 12px 5px; color: #3498db; text-decoration: none; }}
        </style>
    </head>
    <body>
        <h1>{TITLE}</h1>
    """

    items = sorted(os.listdir(CURRENT_DIR))
    found_any = False

    for item in items:
        item_path = os.path.join(CURRENT_DIR, item)
        # 只扫描子文件夹
        if os.path.isdir(item_path) and not item.startswith('.'):
            html_files = sorted([f for f in os.listdir(item_path) if f.endswith('.html')])
            if html_files:
                found_any = True
                html_content += f'<details><summary>📂 {item} ({len(html_files)})</summary><ul>'
                for f in html_files:
                    # 【关键】因为 index.html 和子文件夹都在 tutorial 下，所以直接写 子文件夹/文件名.html
                    html_content += f'<li><a href="{item}/{f}">{f.replace(".html", "")}</a></li>'
                html_content += '</ul></details>'

    html_content += "</body></html>"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ 成功！文件已生成，请刷新文件夹查看。")


if __name__ == "__main__":
    generate_html()