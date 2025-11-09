node DocGenie {
    has repo_url: str = "";
    has file_tree: str = "";
    has readme: str = "";
    has functions: list = [];
    has classes: list = [];
    has markdown_doc: str = "";
    has diagrams: str = "";

    def generate_documentation() {
        self.generate_markdown();
    }

    def generate_markdown() {
        self.markdown_doc = "# Documentation\n\nGenerated from " + self.repo_url;
    }
}
