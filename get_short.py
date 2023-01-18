from data_for_tests import symbols


def short_article(article):
    n = 25
    try:
        if len(article) > n:
            short = article[:n]
            for a in short[::-1]:
                if a == ' ':
                   short = short[:-1]
                   break
                elif a in symbols:
                    short = short[:-1]
                else:
                    break
            return  short + '...'
        else:
            return article
    except TypeError:
        return 'Input must be string'
