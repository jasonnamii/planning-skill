#!/usr/bin/env python3
"""
planning-skill self-check validator.

5개 검증 항목:
1. SKILL.md frontmatter 필수 필드 (name·description·vault_dependency·version)
2. references/ Phase md 6개 존재 (phase0~phase5)
3. P1~P5 키워드 카운트 최소 요건 (P1≥5, P2≥3, NOT 존재)
4. NOT 라우팅 ≥ 4건
5. evals/cases.json 존재

사용:
    python scripts/validate.py
    python scripts/validate.py --json  # JSON 출력
"""
import json
import re
import sys
from pathlib import Path


def validate(skill_root: Path) -> dict:
    results = {"pass": 0, "fail": 0, "details": []}

    def check(name: str, ok: bool, detail: str = ""):
        results["details"].append({"check": name, "status": "PASS" if ok else "FAIL", "detail": detail})
        if ok:
            results["pass"] += 1
        else:
            results["fail"] += 1

    skill_md = skill_root / "SKILL.md"

    # 1. frontmatter 필수 필드
    if not skill_md.exists():
        check("skill_md_exists", False, f"{skill_md} 없음")
        return results
    text = skill_md.read_text(encoding="utf-8")
    fm_match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not fm_match:
        check("frontmatter_parsed", False, "frontmatter 없음")
        return results
    fm = fm_match.group(1)
    required_fields = ["name:", "description:", "vault_dependency:", "version:"]
    missing = [f for f in required_fields if f not in fm]
    check(
        "frontmatter_required_fields",
        not missing,
        f"누락: {missing}" if missing else "name·description·vault_dependency·version 모두 존재",
    )

    # 2. references Phase md 6개
    refs = skill_root / "references"
    expected_phases = [f"phase{n}-" for n in range(6)]
    found = []
    missing_phases = []
    if refs.exists():
        ref_files = [p.name for p in refs.iterdir() if p.suffix == ".md"]
        for phase_prefix in expected_phases:
            if any(f.startswith(phase_prefix) for f in ref_files):
                found.append(phase_prefix)
            else:
                missing_phases.append(phase_prefix)
    check(
        "references_phases_complete",
        len(found) == 6,
        f"발견 {len(found)}/6. 누락: {missing_phases}" if missing_phases else "phase0~phase5 모두 존재",
    )

    # 3. P1~P5 키워드 카운트
    p1_match = re.search(r"P1:\s*(.+)", text)
    p2_match = re.search(r"P2:\s*(.+)", text)
    p1_count = len([k for k in p1_match.group(1).split(",") if k.strip()]) if p1_match else 0
    p2_count = len([k for k in p2_match.group(1).split(",") if k.strip()]) if p2_match else 0
    check(
        "trigger_p1_min_5",
        p1_count >= 5,
        f"P1={p1_count} (최소 5)",
    )
    check(
        "trigger_p2_min_3",
        p2_count >= 3,
        f"P2={p2_count} (최소 3)",
    )

    # 4. NOT 라우팅
    not_match = re.search(r"NOT:\s*(.+)", text)
    not_count = 0
    if not_match:
        not_count = len(re.findall(r"→\s*[\w\-]+", not_match.group(1)))
    check(
        "not_routing_min_4",
        not_count >= 4,
        f"NOT 라우팅 {not_count}개 (최소 4)",
    )

    # 5. evals/cases.json
    evals = skill_root / "evals" / "cases.json"
    evals_ok = evals.exists()
    case_count = 0
    if evals_ok:
        try:
            data = json.loads(evals.read_text(encoding="utf-8"))
            case_count = len(data.get("cases", []))
        except Exception as e:
            evals_ok = False
            check("evals_cases_json", False, f"파싱 실패: {e}")
    if evals_ok:
        check(
            "evals_cases_json",
            case_count >= 3,
            f"케이스 {case_count}개 (최소 3)",
        )

    return results


def main():
    skill_root = Path(__file__).resolve().parent.parent
    results = validate(skill_root)

    as_json = "--json" in sys.argv
    if as_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print(f"=== planning-skill self-check ===")
        print(f"PASS: {results['pass']}  FAIL: {results['fail']}")
        for d in results["details"]:
            mark = "✓" if d["status"] == "PASS" else "✗"
            print(f"  {mark} {d['check']}: {d['detail']}")

    sys.exit(0 if results["fail"] == 0 else 1)


if __name__ == "__main__":
    main()
