# Git Branching Strategy for Dynamic CMS Project

## Branching Overview

Our project employs a structured Git branching strategy to ensure that the codebase remains clean and organized. Here are the main types of branches we'll be working with:

### Main Branches

- **`main`:** Production-ready code resides here.
- **`develop`:** Development code resides here. All feature branches branch off from here.

### Supporting Branches

- **Feature Branches:** For new features and non-emergency bugfixes.
- **Release Branches:** For final tasks before a production release.
- **Hotfix Branches:** For urgent production fixes.

---

## Branch Naming Conventions

### Feature Branches

- Prefix: `develop/feature/`
- Example: `develop/feature/user-authentication`

### Version Branches

- Prefix: `release/`
- Example: `release/v1.0.0`

### Hotfix Branches

- Prefix: `hotfix/`
- Example: `hotfix/v1.0.1`

### Experimental/Research Branches

- Prefix: `experiment/` or `research/`
- Example: `experiment/new-algorithm`

---

## Git Commands

### Creating a New Feature Branch

```bash
# Switch to the develop branch
git checkout develop

# Create and switch to a new feature branch
git checkout -b develop/feature/user-authentication
```

### Creating a New Version Branch

```bash
# Switch to the develop branch
git checkout develop

# Create and switch to a new release branch
git checkout -b release/v1.0.0
```

### Creating a Hotfix Branch

```bash
# Switch to the main branch
git checkout main

# Create and switch to a new hotfix branch
git checkout -b hotfix/v1.0.1
```

---

## Merging Strategy

- Merge feature branches back into `develop` once the feature is complete.
- Merge `develop` into `main` via a release branch when the release is ready.
- Merge hotfix branches into both `main` and `develop`.

By adhering to this branching strategy, we can ensure a clean and manageable codebase.
