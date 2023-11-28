import os
from pytest_venv import VirtualEnvironment

from .utils import PROJECT_PATH
from .utils import prepare_poetry
from .utils import run_command


def test_bake(cookies):
    """
    tests if the baking process of the cookiecutter template in general works. So if all the 
    files exists etc.
    """
    project_slug = 'project'
    version = '0.3.1'
    
    context = {
        'project_slug': project_slug,
        'version': version,
    }
    result = cookies.bake(template=PROJECT_PATH, extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    
    files = os.listdir(result.project_path)
    expected_files = [
        'README.rst',
        'DEVELOP.rst',
        'pyproject.toml',
        'tests',
        project_slug,
    ]
    for name in expected_files:
        assert name in files, f'{name} not found in the baked folder'
        
        
def test_testing(cookies, venv):
    """
    This test will bake a new version of the cookiecutter and then execute pytest on that 
    that new instance.
    """
    # instantiating a new version of the template
    project_slug = 'project'
    version = '0.3.1'
    
    context = {
        'project_slug': project_slug,
        'version': version,
    }
    result = cookies.bake(template=PROJECT_PATH, extra_context=context)
    poetry, path = prepare_poetry(result.project_path, venv)
    
    tests_path = os.path.join(path, 'tests')
    test_command = f'{venv.python} -m pytest -s {tests_path}'
    proc, out, err = run_command(test_command)
    print('OUTPUT', out)
    print('ERROR', err)
    assert proc.returncode == 0
    
    