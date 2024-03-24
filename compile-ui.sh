## compile-ui.sh


function addFile() {
        for file in UI/*.scss
        do
                sassc "$file" >> static/index-new.css
        done
}

addFile