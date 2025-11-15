#!/bin/bash
# Script to push the first-draft branch to origin
# This script should be run with proper GitHub credentials

set -e

echo "Pushing first-draft branch to origin..."
git push -u origin first-draft

echo "Successfully pushed first-draft branch!"
echo "Verifying the branch exists on remote..."
git ls-remote --heads origin first-draft

echo "Done!"
