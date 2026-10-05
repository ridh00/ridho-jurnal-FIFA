# Creating a research repository

The preferred model is **one independent repository per research project**. A project should not inherit the builder's Git history.

## Option A — GitHub Template Repository

When the repository owner has enabled GitHub's **Template repository** setting, use GitHub's **Use this template** action and create a new private repository.

After creation:

1. confirm `.agents/` and `.github/` are present;
2. set `Workspace mode: RESEARCH` in `research/project-brief.md` and `Mode: RESEARCH` in `brain.md`;
3. preserve the recorded builder version;
4. create the initialization Issue before substantive customization;
5. use Issue → Branch → PR for subsequent research work.

The template-repository flag is a GitHub repository setting, not a file in this repository.

## Option B — portable bootstrap script

From a local clone of Better Research:

```bash
python scripts/init_research.py ../my-research --name "My Research Project"
```

Optionally configure a remote:

```bash
python scripts/init_research.py ../my-research \
  --name "My Research Project" \
  --remote git@github.com:OWNER/REPO.git
```

The script:

- copies the builder without `.git/`;
- switches the copied project brief and `brain.md` to RESEARCH mode;
- records the project name in both;
- initializes a fresh Git repository unless `--no-git` is used;
- does not push automatically.

Review the copied project brief before pushing.

## Why no automatic upstream sync?

Research repositories pin the builder version they were created from. Builder upgrades are explicit migrations through an Issue and PR; see [migration policy](migrations/README.md).

Automatic synchronization could silently change research rules, quality gates, or skill behavior mid-project, which harms reproducibility.
