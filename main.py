import sys
import argparse

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Execute Notebooks")
    parser.add_argument('--save', dest='save',type=int, action="store",
                           required=False, help="Bool indicating whether to save the executed notebooks (overrides existing notebook)", default=0)
    return parser

def run(save:bool=False):

    app1_notebook = "app1/app1_notebook.ipynb"
    app2_notebook = "app2/app2_notebook.ipynb"

    with open(app1_notebook) as f:
        nb1 = nbformat.read(f, as_version=4)

    with open(app2_notebook) as f:
        nb2 = nbformat.read(f, as_version=4)


    # Processing
    # For no restriction on execution time replace timeout with -1 
    ep = ExecutePreprocessor(timeout=600, kernel_name='jupyterstructure')
    ep.preprocess(nb1, {'metadata': {'path': './app1'}})
    # Processing 2

    ep = ExecutePreprocessor(timeout=600, kernel_name='jupyterstructure')
    ep.preprocess(nb2, {'metadata': {'path': './app2'}})

    if save is True:
        with open(app1_notebook, 'w', encoding='utf-8') as f:
            nbformat.write(nb1, f)
        with open(app2_notebook, 'w', encoding="utf-8") as f:
            nbformat.write(nb2, f)

def main():
    parser = cli()
    args = parser.parse_args()
    
    SAVE = bool(args.save)
    
    run(SAVE)
            
if __name__ == '__main__':
    sys.exit(main)
    
