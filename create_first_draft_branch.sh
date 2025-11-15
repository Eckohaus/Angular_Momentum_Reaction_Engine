#!/bin/bash
# Script to create the first-draft branch with V1 content

# This script should be run from the repository root
# It will create a first-draft branch incorporating content from V1

set -e

echo "Creating first-draft branch with V1 content integration..."

# Add V1 remote if not already added
if ! git remote | grep -q "^v1$"; then
    echo "Adding V1 remote..."
    git remote add v1 https://github.com/Eckohaus-Indonesia/Angular_Momentum_Reaction_Engine_V1.git
fi

# Fetch from V1
echo "Fetching from V1 master..."
git fetch v1 master

# Create first-draft branch from current main/master
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $CURRENT_BRANCH"

# Check if first-draft already exists
if git show-ref --verify --quiet refs/heads/first-draft; then
    echo "first-draft branch already exists locally"
    read -p "Do you want to delete and recreate it? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git branch -D first-draft
    else
        echo "Keeping existing first-draft branch"
        exit 0
    fi
fi

# Create first-draft branch
echo "Creating first-draft branch..."
git checkout -b first-draft

# Merge V1 master content
echo "Merging V1 master content..."
git merge v1/master --allow-unrelated-histories -m "Merge V1 master branch into first-draft"

# Push to origin
echo "Pushing first-draft branch to origin..."
git push -u origin first-draft

echo "✓ first-draft branch created and pushed successfully!"
echo "Switching back to $CURRENT_BRANCH..."
git checkout "$CURRENT_BRANCH"
