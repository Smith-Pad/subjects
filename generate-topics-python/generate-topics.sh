## generate-topics.sh 




function ImportPythonLibraries() 
{
    python3 -c "import ollama"
    python3 -c "import os"
    python3 -c "import sys"
    python3 -c "import json"  
    python3 -c "import shutil"
}

ImportPythonLibraries



python3 -c """
$ImportPythonLibraries
def main():
    print('hello world!')


"""