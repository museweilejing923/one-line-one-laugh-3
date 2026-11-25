"""One funny line about a password manager, written by this script.

The joke is a fixed string. A set of small named rules audits it
before it may be saved: topic, size, cleanliness, ending, and a
ban on links. If any rule objects, the program bails out with
exit code 1 and writes nothing. With no input, no network, and
no randomness, each run writes the same bytes to
/output/entry.txt.
"""

import sys
from pathlib import Path

ENTRY = "My password manager just emailed me to say my password is weak. It is the only thing in my life that checks in on me."
MAXIMUM = 200
RESULT = Path("/output/entry.txt")


def bail(msg):
    print(f"rejected: {msg}", file=sys.stderr)
    raise SystemExit(1)


def rule_topic_password(text):
    if "password" not in text:
        bail("entry is off topic")


def rule_no_link(text):
    if "http" in text:
        bail("entry must not contain a link")


def rule_bounded(text):
    if len(text) > MAXIMUM:
        bail("entry is longer than the limit")


def rule_present(text):
    if not text or not text.strip():
        bail("entry is empty")


def rule_clean(text):
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        bail("entry has control characters")


def rule_closed(text):
    if not text or text[-1] not in ".!?":
        bail("entry must end with . ! or ?")


def rule_readable(text):
    if text != text.strip() or "  " in text or "\n" in text or "\r" in text:
        bail("entry has ragged edges or line breaks")


def rule_lettered(text):
    if not any(ch.isalpha() for ch in text):
        bail("entry has no letters")


def rule_not_digits(text):
    if text.isdigit():
        bail("entry is only digits")


def rule_not_symbols(text):
    if not any(ch.isalnum() for ch in text):
        bail("entry is only punctuation")


def rule_no_tab(text):
    if "\t" in text:
        bail("entry contains a tab")


RULESET = (
    rule_no_tab,
    rule_topic_password,
    rule_no_link,
    rule_bounded,
    rule_present,
    rule_clean,
    rule_closed,
    rule_readable,
    rule_lettered,
    rule_not_digits,
    rule_not_symbols,
)


def audit(text):
    for rule in RULESET:
        rule(text)


def main():
    audit(ENTRY)
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
