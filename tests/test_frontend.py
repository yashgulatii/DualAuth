import os

TEMPLATE_DIR = "frontend/templates"
TEMPLATE_FILES = [
    "index.html",
    "login_vulnerable.html",
    "login_secure.html",
    "dashboard.html",
    "result.html",
    "awareness.html"
]

def test_templates_exist():
    for tpl in TEMPLATE_FILES:
        path = os.path.join(TEMPLATE_DIR, tpl)
        assert os.path.exists(path), f"Missing: {tpl}"
