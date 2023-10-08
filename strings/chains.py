text = "  Python  "
assert text.strip().upper() == "PYTHON"
assert text.lstrip().lower() == "python  "

items = ["dog", "cat"]
assert "-".join(items).upper() == "DOG-CAT"

raw_zip_code = "123-"
assert raw_zip_code.rstrip("-").zfill(5) == "00123"

