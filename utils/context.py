class AgentContext:

    def __init__(self):

        self.user_query = ""

        self.intent = {}

        self.full_schema = {}

        self.selected_schema = {}

        self.generated_sql = ""

        self.validated_sql = ""

        self.results = None

        self.analysis = ""

        self.logs = []