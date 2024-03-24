## compile-ui.sh

rm -rf static/index-new.css

function addFile() {
        for file in UI/*.scss
        do
                sassc "$file" >> static/index-new.css
        done
}

addFile