from utils.snowflake import Snowflake


def test_snowflake():
    num = Snowflake(0).generate()
    assert isinstance(num, int)
    assert len(str(num)) == 18
