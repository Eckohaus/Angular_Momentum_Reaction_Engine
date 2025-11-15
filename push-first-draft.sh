#!/bin/bash
#
# Script to push the first-draft branch to the remote repository
# This script requires appropriate GitHub credentials to be configured
#

set -e

echo "Pushing first-draft branch to origin..."
git push -u origin first-draft

echo "Verifying the branch was pushed successfully..."
git ls-remote --heads origin first-draft

echo "✓ first-draft branch successfully pushed!"
echo "You can view it at: https://github.com/Eckohaus/Angular_Momentum_Reaction_Engine_v2/tree/first-draft"
