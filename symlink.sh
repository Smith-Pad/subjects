## symlink.sh

## This script allows the ability to dynamically symlink and use the particular files
## that way it will be better organized for any use case. 





function symlink_css() 
{
	ln -sf static/css/FOIL-Bar.css FOIL-Bar.css					## Symlink the FOIL-Bar.css file
	ln -sf static/css/UI-new.css UI-new.css						## Symlink the UI-new.css file
	ln -sf static/css/UI.css UI.css							## Symlink the UI.css file
	
}

symlink_css
