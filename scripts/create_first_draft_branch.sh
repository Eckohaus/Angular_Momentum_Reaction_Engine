#!/bin/bash
# Script to create an orphan branch 'first-draft' with contents from AMRE v1

# 1. Create an orphan branch named 'first-draft'
git checkout --orphan first-draft

# 2. Remove all working directory files
git rm -rf .

# 3. Add the AMRE v1 repository as a temporary remote named 'v1'
git remote add v1 https://github.com/Eckohaus-Indonesia/Angular_Momentum_Reaction_Engine_V1

# 4. Pull the contents of the v1 repository into the orphan branch
git pull v1 main --allow-unrelated-histories

# 5. Make a commit with the specified commit message
git commit -m "Import AMRE v1 into first-draft branch

This branch contains a full snapshot of the original
Angular Momentum Reaction Engine (v1) from the
Eckohaus-Indonesia repository. It is preserved here
as the foundational first draft for reference and
historical consolidation within the AMRE v2 structure.

Co-authored-by: system operator <wanda@openai.com>
Co-authored-by: system administrator <Corvin Nehal Dhali> <info@eckohaus.co.uk>
Co-authored-by: GitHub Copilot <copilot@github.com>"

# 6. Push the new 'first-draft' branch to GitHub
git push origin first-draft

# 7. Remove the temporary 'v1' remote
git remote remove v1
