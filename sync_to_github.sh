#!/bin/bash

# Define Directory
AC_DIR="/var/www/amre-mirror/research/docs/previews/electrical_resistance/ac_unit"
mkdir -p $AC_DIR

echo "Initiating Fortran Render..."

# Render Sequencer
/var/www/fortran-services/lambda_webview | tail -n +3 > /var/www/amre-mirror/research/docs/previews/electrical_resistance/lambda_sequencer/base_equation.html
/var/www/fortran-services/lambda_webview_2 | tail -n +3 > /var/www/amre-mirror/research/docs/previews/electrical_resistance/lambda_sequencer/calculating_variables_2.html

# Render AC Unit with NEW filename
/var/www/fortran-services/lambda_webview_3 | tail -n +3 > $AC_DIR/environment_variable_v1.html

# Remove the legacy file if it exists to clean the repo
if [ -f "$AC_DIR/deposition_decimalisation.html" ]; then
    git rm "$AC_DIR/deposition_decimalisation.html"
fi

echo "Staging records..."
git add research/docs/previews/

echo "Committing and pushing..."
git diff --quiet && git diff --staged --quiet || (git commit -m "refactor: rename deposition_decimalisation to environment_variable_v1

Co-authored-by: system operator Gemini <gemini@google.com>
Co-authored-by: system administrator <Corvin Nehal Dhali> <info@eckohaus.co.uk>" && git push origin master)

echo "Synchronization Complete."
