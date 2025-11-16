# Create First-Draft Orphan Branch

This directory contains scripts to create an orphan branch called `first-draft` that contains the entire contents of the Angular Momentum Reaction Engine V1 repository.

## Files

- **create_first_draft_branch.sh** - Executable shell script with comments
- **create_first_draft_branch_commands.txt** - Plain text list of commands for manual execution

## Usage

### Option 1: Run the shell script

```bash
cd /path/to/Angular_Momentum_Reaction_Engine_v2
./scripts/create_first_draft_branch.sh
```

### Option 2: Copy and paste commands

View the contents of `create_first_draft_branch_commands.txt` and paste the commands into your terminal one by one.

## What the script does

1. Creates an orphan branch named `first-draft` (no shared history with current branches)
2. Removes all working directory files
3. Adds the AMRE v1 repository as a temporary remote named `v1`
4. Pulls the contents from the v1 repository using `--allow-unrelated-histories`
5. Makes a commit with a detailed message including co-authors
6. Pushes the new `first-draft` branch to GitHub
7. Removes the temporary `v1` remote

## Important Notes

- This creates an **orphan branch** with no shared history with your current branches
- The `first-draft` branch will contain a complete snapshot of AMRE v1
- After running the script, you'll be on the `first-draft` branch
- To return to your previous branch, use: `git checkout <previous-branch-name>`

## Commit Message

The script will create a commit with the following message:

```
Import AMRE v1 into first-draft branch

This branch contains a full snapshot of the original
Angular Momentum Reaction Engine (v1) from the
Eckohaus-Indonesia repository. It is preserved here
as the foundational first draft for reference and
historical consolidation within the AMRE v2 structure.

Co-authored-by: system operator <wanda@openai.com>
Co-authored-by: system administrator <Corvin Nehal Dhali> <info@eckohaus.co.uk>
Co-authored-by: GitHub Copilot <copilot@github.com>
```
