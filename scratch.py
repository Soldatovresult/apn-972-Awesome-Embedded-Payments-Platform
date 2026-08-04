import os
import re
import subprocess

repo_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Embedded-Payments-Platform"
os.chdir(repo_dir)

def run_git(commit_msg):
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    subprocess.run(["git", "push"], check=True)

def read_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()

def write_readme(content):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

# Step 1: SaaS Company Size and Sort
readme = read_readme()

saas_data = [
    {"name": "Stripe", "val": 65000, "str": "$65B Valuation", "row": ""},
    {"name": "Adyen", "val": 40000, "str": "$40B Valuation", "row": ""},
    {"name": "Checkout.com", "val": 11000, "str": "$11B Valuation", "row": ""},
    {"name": "Rapyd", "val": 8700, "str": "$8.7B Valuation", "row": ""},
    {"name": "Unit", "val": 1200, "str": "$1.2B Valuation", "row": ""},
    {"name": "Treasury Prime", "val": 500, "str": "$500M Valuation", "row": ""},
    {"name": "Synctera", "val": 300, "str": "$300M Valuation", "row": ""},
    {"name": "Moov", "val": 200, "str": "$200M Valuation", "row": ""},
    {"name": "Finix", "val": 200, "str": "$200M Valuation", "row": ""},
    {"name": "Weavr", "val": 100, "str": "$100M Valuation", "row": ""},
]

lines = readme.split('\n')
new_lines = []
in_table = False
table_rows = []
for line in lines:
    if line.startswith('| Platform |'):
        in_table = True
        new_lines.append('| Platform | Description | Pricing | Free Tier Limit | Company Size |')
        continue
    if in_table and line.startswith('|----------|'):
        new_lines.append('|----------|-------------|---------|-----------------|--------------|')
        continue
    if in_table and line.startswith('| **['):
        table_rows.append(line)
        continue
    if in_table and not line.strip():
        in_table = False
        for row in table_rows:
            for s in saas_data:
                if s["name"] in row:
                    s["row"] = row + f" {s['str']} |"
                    break
        saas_data.sort(key=lambda x: x["val"], reverse=True)
        for s in saas_data:
            if s["row"]:
                new_lines.append(s["row"])
        new_lines.append(line)
        continue
    if not in_table:
        new_lines.append(line)

readme = '\n'.join(new_lines)
write_readme(readme)
run_git("Added company size and sorted the SaaS based on that")

# Step 2: Open Source Stars
readme = read_readme()
os_data = [
    {"name": "Formance Ledger", "repo": "formancehq/ledger", "stars": 4500},
    {"name": "Blnk Core", "repo": "blnkfinance/blnk", "stars": 1200},
    {"name": "Apache Fineract", "repo": "apache/fineract", "stars": 2300},
    {"name": "jPOS", "repo": "jpos/jPOS", "stars": 1100},
    {"name": "Mojaloop", "repo": "mojaloop/mojaloop", "stars": 800}
]

for osd in os_data:
    pattern = rf'(- \*\*\[{osd["name"]}\]\((.*?)\)\*\*.*)'
    badge = f'[![GitHub stars](https://img.shields.io/github/stars/{osd["repo"]}?style=social&color=white)](https://github.com/{osd["repo"]}/stargazers)'
    
    # We replace the start of the line with itself + badge
    # Actually wait, let's just do text replacement
    readme = re.sub(rf'(- \*\*\[{osd["name"]}\]\(.*?\)\*\*)', rf'\1 {badge}', readme)

def sort_os_list(text):
    lines = text.split('\n')
    out = []
    current_list = []
    def flush_list():
        if current_list:
            def get_stars(line):
                for osd in os_data:
                    if osd["name"] in line:
                        return osd["stars"]
                return 0
            current_list.sort(key=get_stars, reverse=True)
            out.extend(current_list)
            current_list.clear()

    for line in lines:
        if line.startswith('- **['):
            current_list.append(line)
        else:
            flush_list()
            out.append(line)
    flush_list()
    return '\n'.join(out)

parts = readme.split('## 🔓 Open-Source Software')
if len(parts) > 1:
    parts[1] = sort_os_list(parts[1])
    readme = '## 🔓 Open-Source Software'.join(parts)

write_readme(readme)
run_git("Added github stars and sorted the opensource based on that")

# Step 3: SVG Banner
os.makedirs("assets", exist_ok=True)
svg_content = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#8A2BE2"/>
            <stop offset="100%" stop-color="#4B0082"/>
        </linearGradient>
    </defs>
    <rect width="800" height="200" fill="url(#grad1)" rx="15" ry="15" />
    <text x="50%" y="50%" font-family="Arial, sans-serif" font-size="36" fill="white" font-weight="bold" dominant-baseline="middle" text-anchor="middle">
        Awesome Embedded Payments Platforms
    </text>
    <circle cx="100" cy="100" r="20" fill="white" opacity="0.5">
        <animate attributeName="r" values="20;30;20" dur="2s" repeatCount="indefinite" />
    </circle>
</svg>"""
with open("assets/banner.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

readme = read_readme()
readme = "![Banner](assets/banner.svg)\n\n" + readme
write_readme(readme)
run_git("added banner")

# Step 4: Emojis
readme = read_readme()
readme = readme.replace('## 🏢 SaaS / Hosted Platforms', '## 🏢 SaaS / Hosted Platforms ☁️')
readme = readme.replace('## 🔓 Open-Source Software', '## 🔓 Open-Source Software 🌍')
readme = readme.replace('### Open-Source Ledgers', '### 📒 Open-Source Ledgers')
readme = readme.replace('### Payments Infrastructure', '### 🌉 Payments Infrastructure')
write_readme(readme)
run_git("added emojis")

# Step 5: SEO friendly
readme = read_readme()
readme = readme.replace('# Awesome Embedded Payments Platforms', '# Awesome Embedded Payments Platforms - The Ultimate List')
write_readme(readme)
run_git("seo optimised")

# Step 6: Badges to left
readme = read_readme()
left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
readme = readme.replace('![Banner](assets/banner.svg)\n\n', f'![Banner](assets/banner.svg)\n\n<div align="center">\n{left_badges}\n</div>\n\n')
write_readme(readme)
run_git("badges to left added")

# Step 7: Badges to right
readme = read_readme()
right_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
readme = readme.replace(left_badges, left_badges + '\n' + right_badge)
write_readme(readme)
run_git("badges to right added")

# Step 8: Star History
readme = read_readme()
star_history = """
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Embedded-Payments-Platform&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Embedded-Payments-Platform&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Embedded-Payments-Platform&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Embedded-Payments-Platform&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
readme = readme + "\n" + star_history
write_readme(readme)
run_git("star history added")

# Step 9: Replace chartrepos
readme = read_readme()
readme = readme.replace("chartrepos", "chart?repos")
write_readme(readme)
run_git("fixed star plot")

# Step 10: Replace awesome link
readme = read_readme()
readme = readme.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
write_readme(readme)
run_git("invalid awesome link fixed")

print("All steps completed successfully.")
