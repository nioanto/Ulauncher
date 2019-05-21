from ulauncher.api.shared.item.ResultItem import ResultItem
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction
from ulauncher.search.apps.AppQueryDb import AppQueryDb


class ExtensionKeywordResultItem(ResultItem):

    def __init__(self, *args, **kw):
        super(ExtensionKeywordResultItem, self).__init__(*args, **kw)
        self._app_queries = AppQueryDb.get_instance()

    def selected_by_default(self, query):
        """
        :param ~ulauncher.search.Query.Query query:
        """
        return self._app_queries.find(query) == self.get_name()

    def on_enter(self, query):
        """
        :param ~ulauncher.search.Query.Query query: query
        """
        if query:
            self._app_queries.put(query, self.get_name())
            self._app_queries.commit()

        return SetUserQueryAction('%s ' % self.get_keyword())
