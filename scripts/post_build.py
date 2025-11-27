import shutil
import os

def on_post_build(config):
    src = os.path.join("site", "sitemap.xml")
    dst = os.path.join("site", "sitemap-lyceum.xml")
    if os.path.exists(src):
        shutil.copyfile(src, dst)
        print("[HOOK] Copied sitemap to sitemap-lyceum.xml")
    else:
        print("[HOOK] sitemap.xml not found.")
