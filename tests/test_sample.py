# Written just to make sure your environment is setup correctly. 
# Extra tests can be added for each package or module that is required by this project. 
def test_pytest_is_working():
    import pytest as pt
    from fluentcheck import Check
    assert Check is not None
    Check(pt).is_not_none()

def test_python_version():
    import sys
    assert sys.version_info.major == 3
    assert sys.version_info.minor >= 10