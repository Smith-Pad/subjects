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
        PyRun_SimpleString("import flask\nimport os\nimport json\n");
        Py_Finalize();
}
