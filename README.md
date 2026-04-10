# planning-skill

**Universal 6-phase planning pipeline orchestrator — domain-agnostic structured planning from context to executable roadmap.**

## Prerequisites

- **Obsidian Vault** — default output format is Obsidian-compatible `.md`; without a vault, outputs still work as standard markdown
- **Claude Cowork or Claude Code** environment

## Goal

Strategic planning demands methodical progression from raw context through hypothesis, research, convergence, creative insight, and final execution planning. Planning-Skill orchestrates this 6-phase pipeline across any domain — startups, campaigns, products, teams, transformations — using research-frame and trigger-dictionary as phase-specific tools, ensuring rigor without domain lock-in.

## When & How to Use

Invoke planning-skill when you're starting a significant initiative and need structured progression from brief to roadmap. The skill manages all 6 phases with gates between each: P0 Context gathering → P1 Hypothetical Goals (MECE framework) → P2 Research (calls research-frame) → P3 Convergence (spine extraction) → P4 Creative Jump (analogy and TRIZ tools) → P5 Plan Evolution (executable roadmap). Each phase has clear inputs, decision gates, and outputs; you only move forward when criteria are met.

## Use Cases

| Scenario | Prompt | What Happens |
|---|---|---|
| Launch new product line | `"Plan this: we want to enter the SMB market with a $500 SaaS product"` | P0→P1 (goals: GTM, retention, differentiation)→P2 (research SMB pain)→P3 (single spine)→P4 (analogy)→P5 (roadmap) |
| Restructure engineering team | `"planning-skill on: move from feature teams to platform teams"` | P0 (org context)→P1 (hypothetical structures)→P2 (Spotify model research)→P3 (convergence)→P4 (creative)→P5 (90-day plan) |
| Campaign strategy | `"Plan our campaign: Q2 focus on retention in Southeast Asia"` | Phases 0-5 with region-specific research, competitor analysis, creative positioning, month-by-month breakdown |

## Key Features

- Six-phase progression: P0 Context → P1 Hypothetical Goals (MECE) → P2 Research → P3 Convergence → P4 Creative Jump → P5 Plan Evolution
- Domain-agnostic: works for product launches, organizational changes, campaigns, acquisitions, crises, strategy shifts
- Integrated tool orchestration: calls research-frame for P2, trigger-dictionary tools for P4 creative jump
- Decision gates between phases ensure rigor and prevent premature convergence
- Outputs range from hypothesis maps to executable 90-day roadmaps with resource allocation

## Works With

- **[research-frame](https://github.com/jasonnamii/research-frame)** — planning-skill calls research-frame in P2 (Research phase)
- **[trigger-dictionary](https://github.com/jasonnamii/trigger-dictionary)** — planning-skill uses trigger-dictionary tools in P4 (Creative Jump phase)
- **[hit-skill](https://github.com/jasonnamii/hit-skill)** — hit-skill can diagnose and design based on plan outputs
- **[deliverable-engine](https://github.com/jasonnamii/deliverable-engine)** — deliverable-engine formats final plans and roadmaps

## Installation

```bash
git clone https://github.com/jasonnamii/planning-skill.git ~/.claude/skills/planning-skill
```

## Update

```bash
cd ~/.claude/skills/planning-skill && git pull
```

Skills placed in `~/.claude/skills/` are automatically available in Claude Code and Cowork sessions.

## Part of Cowork Skills

This is one of 25+ custom skills. See the full catalog: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## License

MIT License — feel free to use, modify, and share.
