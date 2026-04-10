# 범용 기획 파이프라인

> 🇺🇸 [English README](./README.md)

**범용 6단계 기획 파이프라인 오케스트레이터 — 도메인 무관한 구조화된 기획: 상황에서 실행 로드맵까지**

## 사전 요구사항

- **Obsidian Vault** — 기본 출력 형식은 Obsidian 호환 `.md`; vault 없어도 표준 마크다운으로 작동
- **Claude Cowork 또는 Claude Code** 환경

## 목적

전략 기획은 raw 상황에서 가설, 리서치, 수렴, 창의적 인사이트, 최종 실행 기획까지의 체계적 진행을 요구합니다. Planning-Skill은 도메인 무관하게 이 6단계 파이프라인을 오케스트레이션합니다 (스타트업, 캠프, 제품, 팀, 변환 등) research-frame과 trigger-dictionary를 단계별 도구로 활용하여 엄밀함을 보장합니다.

## 사용 시점 및 방법

중요한 이니셔티브를 시작하고 brief에서 로드맵까지의 구조화된 진행이 필요할 때 호출하세요. 스킬이 모든 6단계를 관리합니다 단계 간 게이트: P0 상황 수집 → P1 가설적 목표 (MECE 프레임) → P2 리서치 (research-frame 호출) → P3 수렴 (스파인 추출) → P4 창의적 점프 (유추 및 TRIZ 도구) → P5 기획 발전 (실행 로드맵). 각 단계는 명확한 입력, 의사결정 게이트, 출력을 가집니다; 기준이 충족될 때만 진행합니다.

## 사용 예시

| 상황 | 프롬프트 | 결과 |
|---|---|---|
| 신제품 런칭 | `"Plan this: we want to enter the SMB market with a $500 SaaS product"` | P0→P1 (목표: GTM, 유지, 차별화)→P2 (SMB pain 리서치)→P3 (단일 스파인)→P4 (유추)→P5 (로드맵) |
| 엔지니어링팀 재구성 | `"planning-skill on: move from feature teams to platform teams"` | P0 (조직 상황)→P1 (가설적 구조)→P2 (Spotify 모델 리서치)→P3 (수렴)→P4 (창의적)→P5 (90일 계획) |
| 캠프 전략 | `"Plan our campaign: Q2 focus on retention in Southeast Asia"` | 지역별 리서치, 경쟁사 분석, 창의적 포지셔닝, 월별 분석이 포함된 단계 0-5 |

## 핵심 기능

- 6단계 진행: P0 상황 → P1 가설적 목표 (MECE) → P2 리서치 → P3 수렴 → P4 창의적 점프 → P5 기획 발전
- 도메인 무관: 제품 런칭, 조직 변경, 캠프, 인수, 위기, 전략 전환에 작동
- 통합 도구 오케스트레이션: P2 (리서치 단계)에서 research-frame 호출, P4 (창의적 점프 단계)에서 trigger-dictionary 도구 활용
- 단계 간 의사결정 게이트는 엄밀함 보장 및 조기 수렴 방지
- 출력은 가설 맵에서 리소스 할당이 포함된 실행 가능한 90일 로드맵까지


## 연관 스킬

- **[research-frame](https://github.com/jasonnamii/research-frame)** — planning-skill은 P2 (리서치 단계)에서 research-frame을 호출합니다
- **[trigger-dictionary](https://github.com/jasonnamii/trigger-dictionary)** — planning-skill은 P4 (창의적 점프 단계)에서 trigger-dictionary 도구를 활용합니다
- **[hit-skill](https://github.com/jasonnamii/hit-skill)** — hit-skill은 기획 출력을 기반으로 진단 및 설계 가능
- **[deliverable-engine](https://github.com/jasonnamii/deliverable-engine)** — deliverable-engine은 최종 기획과 로드맵 포맷

## 설치

```bash
git clone https://github.com/jasonnamii/planning-skill.git ~/.claude/skills/planning-skill
```

## 업데이트

```bash
cd ~/.claude/skills/planning-skill && git pull
```

`~/.claude/skills/`에 배치된 스킬은 Claude Code 및 Cowork 세션에서 자동으로 사용할 수 있습니다.

## Cowork 스킬 생태계

25개 이상의 커스텀 스킬 중 하나입니다. 전체 카탈로그: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## 라이선스

MIT 라이선스 — 자유롭게 사용, 수정, 공유하세요.
