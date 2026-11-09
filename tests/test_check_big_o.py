import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("check_big_o", ROOT / "scripts" / "check_big_o.py")
check_big_o = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_big_o)

DOC = ROOT / "BIG_O.md"
RESULTS = ROOT / "results"


def run(doc):
    return check_big_o.main(["check_big_o.py", str(doc), str(RESULTS)])


def test_committed_doc_passes():
    assert run(DOC) == 0


def test_changed_sort_number_fails(tmp_path):
    text = DOC.read_text(encoding="utf-8")
    assert "204480.0" in text
    copy = tmp_path / "BIG_O.md"
    copy.write_text(text.replace("204480.0", "204481.0", 1), encoding="utf-8")
    assert run(copy) == 1


def test_changed_search_number_fails(tmp_path):
    text = DOC.read_text(encoding="utf-8")
    assert "481.25" in text
    copy = tmp_path / "BIG_O.md"
    copy.write_text(text.replace("481.25", "481.26", 1), encoding="utf-8")
    assert run(copy) == 1


def test_missing_table_fails(tmp_path):
    copy = tmp_path / "BIG_O.md"
    copy.write_text("# nothing here\n", encoding="utf-8")
    assert run(copy) == 1
