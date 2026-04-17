# CHANGELOG — planning-skill

SemVer 규칙 적용. Major=파이프라인 구조 변경, Minor=섹션 추가·트리거 확장, Patch=버그·오탈자.

---

## [1.0.0] — 2026-04-17

### Added
- **절대 규칙 섹션 (5개)** — 포맷 지정·P1→P2 Hard Gate·스파인 확정·도메인 라우팅·허브 위임 명문화
- **frontmatter version 필드** — SemVer 진화 추적 기반
- **파이프라인 총괄 로딩 규칙 명시** — Phase별 순차 로드, 동시 로드 금지
- **evals/cases.json** — 라우팅·Phase 진입·핸드오프 3축 회귀 검증 샘플 3케이스
- **scripts/validate.py** — frontmatter·Phase md·트리거·NOT 라우팅·evals 5항목 self-check

### Skill Health
- skill-doctor 진단 결과: 🟠 66.1/100 → 처방 P0+P1 적용 후 🟢 80+ 목표
- 개선 축: ⑦ 진화불능 (4→0), ⑧ 무자각 (4→2), ① 느림 (1→0), ④ 취약 (4→3)

### Origin
- planning-recipe 7법칙 중 6개 흡수 (절대자 프레임·MECE 분해·리서치→결정 3단·반복 진화·복수 컨셉·갭이 구조 생성)
- 6 Phase 오케스트레이터 구조 확립 (P0 상황배경 → P5 기획안 진화)
- 외부 스킬 직접 호출 2건(research-frame·hit-skill) + trigger-dictionary 경유 다수

---

## Roadmap

### [1.1.0] — 계획
- P2 처방 번들 A (④ 취약 축): PREFLIGHT·vault fallback·세션 재검증
- P2 처방 번들 B (⑧ 무자각 축): 게이트 미통과 STOP·피드백 채널·session-briefing 연계
- evals 자동화 스크립트 (수동 → 자동)

### [1.2.0] — 계획
- P2 처방 번들 C (③ 불통 축): 예시 섹션·Gotchas 확장·부제 추가
- 허브스포크 재점검 (SKILL.md 5KB 목표 도전)
