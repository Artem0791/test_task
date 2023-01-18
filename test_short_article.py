import pytest
from get_short import short_article
from data_for_tests import article1, article2, article3, article4, article5, negative_article1, negative_article2


class TestShort:

    @pytest.mark.parametrize('article', [article1, article2, article3, article4])
    def test_article_length(self, article):
        result = short_article(article)
        assert len(result) <= 28  # 25 symbols with ...


    @pytest.mark.parametrize('article', [article5])
    def test_article_abracadabra(self, article):
        result = short_article(article)
        assert len(result) <= 28  # 25 symbols with ...


    @pytest.mark.parametrize('article', [negative_article1, negative_article2])
    def test_article_type_error(self, article):
        result = short_article(article)
        assert result == 'Input must be string'
