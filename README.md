# Planning Skill

**Universal planning pipeline with 6-phase orchestration.**

Domain-agnostic orchestrator: P0 Context → P1 Hypothetical Goals (MECE) → P2 Research (calls research-frame) → P3 Convergence (spine extraction) → P4 Creative Jump (analogy, TRIZ) → P5 Plan Evolution. Gates between phases prevent skipping.

### Example Prompts

```
"Plan a market entry strategy for Southeast Asia" → context→goals→research→spine→creative options→plan
"Start planning" → full 6-phase pipeline
```

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

This is one of 25 custom skills. See the full catalog: [https://github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## License

MIT License — feel free to use, modify, and share.
