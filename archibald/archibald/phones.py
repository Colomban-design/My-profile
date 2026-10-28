"""Numéros de téléphone au format international (E.164), comme les opérateurs les attendent."""

from __future__ import annotations

import re


def to_e164(raw: str, default_country: str = "33") -> str:
    """« 06 12 34 56 78 », « +33 6 12… », « 0033 6… » → « +33612345678 ». Laisse le reste tel quel."""
    s = re.sub(r"[^\d+]", "", raw or "")
    if s.startswith("00"):
        s = "+" + s[2:]
    if s.startswith("+"):
        return s
    if s.startswith("0") and len(s) == 10:
        return f"+{default_country}{s[1:]}"
    return s


def is_mobile_fr(e164: str) -> bool:
    return bool(re.fullmatch(r"\+33[67]\d{8}", e164))


def pretty(e164: str) -> str:
    if re.fullmatch(r"\+33\d{9}", e164):
        d = "0" + e164[3:]
        return " ".join(d[i:i + 2] for i in range(0, 10, 2))
    return e164
