import os
from pytest_venv import VirtualEnvironment

from .utils import PROJECT_PATH


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
    for name in files:
        assert name in expected_files, f'{name} not found in the baked folder'