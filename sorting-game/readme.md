# Sorting Game


This game allows the ability for individuals to sort items in the correct order
based on randomization. This portion of the game is an activity which starts on
the second layer of the interactive game.





# Process of the Game


1. The Game Boots
2. First Splashscreen is activated showing the Smith-Pad Logo
3. The game menu starts




# SDL references 


## Creating Window Pointer

When it comes to window pointers, it is recommended to initialize the window pointer like this:

``` c
SDL_Window *window = SDL_CreateWindow("Sorting Game", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 800, 600, SDL_WINDOW_SHOWN);
```