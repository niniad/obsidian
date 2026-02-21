import sys, zipfile, os, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

src = 'C:/Users/ninni/projects/obsidian/inbox/Recall_export_2026-02-20T22-49-16.zip'
dest = 'C:/Users/ninni/projects/obsidian/Reference/recall'

def sanitize(name):
    name = name.replace('\n', ' ').replace('\r', ' ')
    name = re.sub(r'[<>:"|?*]', '_', name)
    name = re.sub(r'  +', ' ', name)
    return name.strip()

z = zipfile.ZipFile(src)
fixed = 0
errors = 0
for info in z.infolist():
    original = info.filename
    clean = sanitize(original)
    if clean != original:
        fixed += 1

    target = os.path.join(dest, clean)

    if clean.endswith('/'):
        os.makedirs(target, exist_ok=True)
    else:
        parent = os.path.dirname(target)
        os.makedirs(parent, exist_ok=True)
        try:
            with z.open(info) as source, open(target, 'wb') as out:
                out.write(source.read())
        except Exception as e:
            errors += 1
            print(f'ERROR: {clean}: {e}')

count = 0
for root, dirs, files in os.walk(dest):
    count += len(files)
print(f'展開完了: {count} ファイル')
print(f'ファイル名修正: {fixed} 件')
if errors:
    print(f'エラー: {errors} 件')
