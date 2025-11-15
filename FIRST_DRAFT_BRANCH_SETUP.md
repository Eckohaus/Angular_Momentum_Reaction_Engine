# First-Draft Branch Setup

## Objective
Recreate the `first-draft` branch in the repository `Eckohaus/Angular_Momentum_Reaction_Engine_v2` to mirror the `master` branch of `Eckohaus-Indonesia/Angular_Momentum_Reaction_Engine_V1`.

## Actions Completed

###  1. Added V1 Repository as Remote
```bash
git remote add v1-repo https://github.com/Eckohaus-Indonesia/Angular_Momentum_Reaction_Engine_V1.git
```

### 2. Fetched V1 Master Branch
```bash
git fetch v1-repo master
```

### 3. Created Local first-draft Branch
```bash
git checkout -b first-draft v1-repo/master
```

The local `first-draft` branch now points to commit `2790401` which is the HEAD of V1's master branch.

## Files in first-draft Branch
The first-draft branch contains the following structure from V1:
- Commercial Licence.md
- LICENSE
- ReadMe.md
- General/ (directory with V1 content)
- Toolsets/ (directory with V1 content)

## Remaining Action Required

Due to environment constraints, the final push operation requires elevated permissions. The `first-draft` branch exists locally and needs to be pushed to the remote repository.

**Manual Push Command (requires appropriate GitHub credentials):**
```bash
git push -u origin first-draft
```

Alternatively, a user with write access to the repository can execute:
```bash
cd /path/to/local/repo
git checkout first-draft
git push -u origin first-draft
```

## Verification

After the push is complete, you can verify the branch exists remotely:
```bash
git ls-remote --heads origin first-draft
```

Or check on GitHub:
https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/tree/first-draft

## Notes
- The master branch in the V2 repository remains unchanged
- The first-draft branch mirrors V1's master branch exactly (commit 2790401)
- No modifications were made to the V1 content during this process
