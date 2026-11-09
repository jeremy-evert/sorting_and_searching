import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("check_site", ROOT / "scripts" / "check_site.py")
check_site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_site)

PAGE = ROOT / "docs" / "index.html"


def test_committed_page_passes():
    assert check_site.main(["check_site.py", str(PAGE)]) == 0


def test_broken_image_fails(tmp_path):
    page = tmp_path / "index.html"
    page.write_text(PAGE.read_text(encoding="utf-8").replace("plots/searching.png", "plots/nope.png"),
                    encoding="utf-8")
    problems = check_site.check(page, ROOT)
    assert any("nope.png" in p for p in problems)


def test_missing_section_fails(tmp_path):
    page = tmp_path / "index.html"
    page.write_text(PAGE.read_text(encoding="utf-8").replace('id="agents"', 'id="other"'),
                    encoding="utf-8")
    assert any("agents" in p for p in check_site.check(page, ROOT))
