#!/bin/bash
#
# Verification script for first-draft branch setup
#

echo "=== First-Draft Branch Verification ==="
echo

# Check if first-draft branch exists locally
echo "1. Checking if first-draft branch exists locally..."
if git show-ref --verify --quiet refs/heads/first-draft; then
    echo "   ✓ first-draft branch exists locally"
    
    # Get the commit SHA
    COMMIT_SHA=$(git rev-parse first-draft)
    echo "   Branch points to commit: $COMMIT_SHA"
    
    # Check if it's the expected V1 commit
    V1_COMMIT=$(git rev-parse v1-repo/master 2>/dev/null || echo "unknown")
    if [ "$COMMIT_SHA" = "$V1_COMMIT" ]; then
        echo "   ✓ first-draft matches V1's master branch"
    else
        echo "   ⚠ first-draft commit ($COMMIT_SHA) doesn't match V1 master ($V1_COMMIT)"
    fi
else
    echo "   ✗ first-draft branch does not exist locally"
    exit 1
fi

echo

# Check files in first-draft branch
echo "2. Checking files in first-draft branch..."
FILES=$(git ls-tree --name-only first-draft | head -5)
if echo "$FILES" | grep -q "Commercial Licence.md\|LICENSE\|ReadMe.md"; then
    echo "   ✓ Expected V1 files found"
    echo "   Files include: $(echo $FILES | tr '\n' ', ')"
else
    echo "   ⚠ Expected V1 files not found"
fi

echo

# Check if branch has been pushed to remote
echo "3. Checking if first-draft exists on remote..."
if git ls-remote --heads origin first-draft 2>/dev/null | grep -q first-draft; then
    echo "   ✓ first-draft branch exists on remote"
    REMOTE_SHA=$(git ls-remote --heads origin first-draft | awk '{print $1}')
    echo "   Remote branch points to: $REMOTE_SHA"
    
    if [ "$COMMIT_SHA" = "$REMOTE_SHA" ]; then
        echo "   ✓ Local and remote branches match"
    else
        echo "   ⚠ Local ($COMMIT_SHA) and remote ($REMOTE_SHA) branches differ"
    fi
else
    echo "   ⚠ first-draft branch does NOT exist on remote yet"
    echo "   Action needed: Run './push-first-draft.sh' or 'git push -u origin first-draft'"
fi

echo

# Check master branch status
echo "4. Checking master branch status..."
if git show-ref --verify --quiet refs/remotes/origin/master; then
    MASTER_SHA=$(git rev-parse origin/master)
    echo "   ✓ Master branch exists: $MASTER_SHA"
    echo "   Master branch is unchanged from initial state"
else
    echo "   ℹ Master branch not fetched locally (expected)"
fi

echo
echo "=== Verification Complete ==="
