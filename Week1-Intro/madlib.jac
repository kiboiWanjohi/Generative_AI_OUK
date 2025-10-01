import from byllm.llm { Model }

glob llm = Model(model_name="gemini/gemini-2.0-flash", verbose=False);

enum PartsOfSpeech {
    ADJECTIVE = "Adjective";
    VERB = "Verb";
    NOUN = "Noun";
}

def generate_madlib(adj: str, verb: str, noun: str) -> str by llm();

walker MadlibGame {
    has adjective: str;
    has verb: str;
    has noun: str;

    can start with `root entry;
    can play with turn entry;
}

node turn {
    has madlib_result: str;
}

with entry {
    root spawn MadlibGame("happy", "runs", "dog");
}
