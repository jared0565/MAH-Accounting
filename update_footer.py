import glob, re
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    new_content = re.sub(r'<footer class="footer".*?</footer>', '<div id="global-footer"></div>', content, flags=re.DOTALL)
    if content != new_content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
