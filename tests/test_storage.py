from sidehustle import storage


def test_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    d = storage.Draft.new("0001-hello", "Hello", ["ai", "tools"], "Body")
    storage.save(d)
    got = storage.load("0001-hello")
    assert got is not None
    assert got.id == d.id
    assert set(got.tags) == {"ai", "tools"}

