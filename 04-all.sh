## Clean the program
rm -rf run.dSYM
rm -rf run


## Compile the program
gcc -o run index.c $(python3-config --cflags) -L$(python3-config --prefix)/lib -lpython3.13




## Run the Program
./run