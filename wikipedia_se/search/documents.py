from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from article_wiki.models import WikiArticle
from titre_wiki.models import WikiArticleTitle

@registry.register_document
class WikiTitleDocument(Document):
    class Index:
        name = 'titre_wiki'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = WikiArticleTitle

        fields = [
            'id', 'title', 'slug'
        ]