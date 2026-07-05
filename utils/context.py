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

        # Retry-related fields
        self.execution_error = ""
        self.retry_count = 0
        self.max_retries = 1