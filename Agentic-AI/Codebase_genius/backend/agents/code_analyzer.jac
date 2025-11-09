node CodeAnalyzer {
    has repo_path: str = "";
    has file_tree: str = "";
    has functions: list = [];
    has classes: list = [];
    has relationships: list = [];

    def analyze_code() {
        self.extract_functions();
        self.extract_classes();
    }

    def extract_functions() {
        self.functions = [];
    }

    def extract_classes() {
        self.classes = [];
    }
}
