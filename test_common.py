import common

class TestCommon:
    def test_greet(self) -> None:
        assert common.greet() == 'Hello World!'
        assert common.greet('Python') == 'Hello Python!'
