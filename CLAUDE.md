# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

An Azure CLI extension (`deploy-to-azure`) that automates setting up GitHub Actions CI/CD pipelines targeting Azure services. The three supported targets are:

- **AKS** (`az aks app up`) — builds container image, pushes to ACR, deploys via Helm to AKS
- **ACI** (`az container app up`) — builds container image, pushes to ACR, deploys to Azure Container Instances
- **Function App** (`az functionapp app up`) — deploys to Azure Functions

All three commands follow the same flow: detect/prompt for GitHub repo → authenticate with GitHub PAT → detect language → select/create Azure resources → generate and commit workflow YAML (and optionally Dockerfiles/Helm charts) → optionally poll for workflow completion.

## Development Commands

All commands run from the repo root unless noted.

### Install for local development
```bash
cd deploy-to-azure && pip install --upgrade -e .
```

### Build wheel
```bash
cd deploy-to-azure && python setup.py sdist bdist_wheel
```

### Run tests
```bash
# From repo root (runs all tests discovered by pytest)
pytest

# Run a single test file
pytest deploy-to-azure/azext_deploy_to_azure/tests/common/test_git.py

# Run a single test by name
pytest deploy-to-azure/azext_deploy_to_azure/tests/common/test_git.py::TestGitMethods::test_github_url_candidate
```

### Linting (both must pass)
```bash
python -m pylint --rcfile pylintrc ./deploy-to-azure/azext_deploy_to_azure -f colorized
python -m flake8 --config .flake8
```

Install linters first if needed: `pip install pylint flake8`

## Code Architecture

### Extension entry point
`deploy-to-azure/azext_deploy_to_azure/__init__.py` registers `DevCommandsLoader` with `COMMAND_LOADER_CLS`. This class delegates to `load_command_table` and `load_arguments` which fan out to the three feature modules (aks, aci, functionapp).

### Feature modules pattern
Each of `dev/aks/`, `dev/aci/`, `dev/functionapp/` contains the same four files:
- `commands.py` — registers the CLI command and maps it to the `up.py` function
- `arguments.py` — declares CLI argument overrides (e.g., `--repository/-r`)
- `_help.py` / `help.py` — help text
- `up.py` — the actual implementation (the `aks_deploy`, `aci_up`, `functionapp_deploy` functions)

### Shared common module (`dev/common/`)
| File | Purpose |
|---|---|
| `git.py` | Detects GitHub remote URL from local git context |
| `github_credential_manager.py` | Singleton that prompts for/caches GitHub PAT; checks `GITHUB_PAT` env var first |
| `github_api_helper.py` | All GitHub REST API calls (branches, file commits, PRs, secrets, check runs). Defines `Files(path, content)` dataclass |
| `github_azure_secrets.py` | Creates `AZURE_CREDENTIALS`, `REGISTRY_USERNAME`, `REGISTRY_PASSWORD` secrets in the GitHub repo via `az ad sp create-for-rbac` |
| `github_workflow_helper.py` | Polls workflow status using `colorama`/`humanfriendly` spinners |
| `azure_cli_resources.py` | Queries Azure resources (AKS, ACR, Function Apps) by shelling out to `az` CLI |
| `prompting.py` | Interactive prompting helpers wrapping knack |
| `const.py` | Placeholder strings used in template substitution |

### Templates and resource files
`dev/resources/resourcefiles.py` contains all GitHub Actions workflow YAML templates as Python string constants (e.g. `DEPLOY_TO_AKS_TEMPLATE`). Placeholders like `container_registry_name_place_holder` are replaced at runtime using `.replace()` with constants from `const.py`.

`dev/resources/packs/{java,javascript,python}/` contains language-specific Dockerfile, `.dockerignore`, and Helm chart templates. The `docker_helm_template.py` reads these from disk and substitutes port/ACR name placeholders before committing to GitHub.

### GitHub API authentication
`GithubCredentialManager` (singleton via `@singleton` decorator in `utils.py`) handles PAT acquisition. It checks the `GITHUB_PAT` environment variable first, then prompts interactively. The PAT is used as HTTP Basic Auth password in all `requests` calls.

### Azure resource queries
`azure_cli_resources.py` shells out to `az` CLI via `subprocess.check_output(..., shell=True)` and parses JSON output. It uses `azure.cli.core._profile.Profile` to get the current subscription context.

## Linting Rules

- Max line length: 120 characters (flake8 and pylint)
- Pylint disabled globally: `missing-docstring`, `too-many-arguments`, `invalid-name`, `duplicate-code`, `import-outside-toplevel`
- Tests are excluded from pylint (`ignore-patterns=test_*`) and flake8 linting

## Versioning and Release

Version is defined in `deploy-to-azure/azext_deploy_to_azure/version.py`. To release:
1. Trigger the Azure Pipelines "Create Release" build (creates wheel + draft GitHub release)
2. Update `src/index.json` in the `azure/azure-cli-extensions` repo with the new wheel URL and SHA256
3. Create a `release-0.x.0` branch from master
4. Bump `version.py` for the next development cycle

See `doc/release_new_version.md` for details.
