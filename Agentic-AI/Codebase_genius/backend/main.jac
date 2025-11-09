import from byllm.llm { Model }
import from dotenv { load_dotenv }
import os;
import json;
include utils;
include agents.repo_mapper;
include agents.code_analyzer;
include agents.doc_genie;

walker code_genius {
    has repo_url: str = "";
    
    obj __specs__ {
        static has auth: bool = False;
    }
    
    can execute with `root entry {
        repo_mapper = RepoMapper(repo_url=self.repo_url);
        repo_mapper.map_repo();
        
        code_analyzer = CodeAnalyzer(repo_path=repo_mapper.repo_path, file_tree=repo_mapper.file_tree);
        code_analyzer.analyze_code();
        
        doc_genie = DocGenie(repo_url=self.repo_url, file_tree=repo_mapper.file_tree, readme=repo_mapper.readme, functions=code_analyzer.functions, classes=code_analyzer.classes);
        doc_genie.generate_documentation();
        
        readme_sum = self.summarize_readme(repo_mapper.readme);
        
        report {
            "status": "Documentation generated",
            "url": self.repo_url,
            "file_tree": repo_mapper.file_tree,
            "readme_summary": readme_sum,
            "markdown_doc": doc_genie.markdown_doc
        };
    }
    
    def summarize_readme(readme: str) -> str {
        lines = readme.split("\n");
        summary = "";
        for i in range(min(3, len(lines))) {
            summary = summary + lines[i] + " ";
        }
        return summary if summary else "No summary available";
    }
}

with entry {
    load_dotenv();
}
