import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from PageObject.DockerPage import DockerPagefun
import pytest

@pytest.mark.usefixtures("multiple_browser")
class TestDockerScenarios:

    #@pytest.mark.smoke
    def test_docker_header(self, jsonData):

        obj = DockerPagefun(self.driver)
        obj.launch_app_with_url(jsonData['url_docker'])
        obj.docker_logo_validation()

