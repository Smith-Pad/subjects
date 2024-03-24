#!/bin/bash

# Remove the old index.css file
rm -f static/index.css

# Loop through all .scss files in the UI directory and append their contents to index-new.css
for file in UI/*.scss
do
  sassc "$file" >> static/index-new.css
done