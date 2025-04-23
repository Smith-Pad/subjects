/*
------------------------------------------------------------------------------------------------
                                        Smith-Pad Subjects
------------------------------------------------------------------------------------------------
*/



// Import all standard libraries
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <math.h>
#include <cpio.h>
#include <ctype.h>
#include <dirent.h>
#include <errno.h>
#include <fcntl.h>
#include <float.h>
#include <signal.h>
#include <sys/types.h>
#include <fcntl.h>

// Import the python library
#include <Python.h>




// This is the main function
int main()
{
        Py_Initialize();

        // This is where we have the abiliy to import python components to it
        PyRun_SimpleString("import flask\nimport os\nimport json\nimport getpass\nimport time\nimport pytest\n\n\n\n");

        Py_Finalize();
}
