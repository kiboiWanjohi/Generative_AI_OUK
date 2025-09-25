import from byllm { Model }

glob llm = Model(model_name="gemini/gemini-2.0-flash");

enum Journal {
    CHEMISTRY = 'Chemistry', 
    PHYSICS = 'Physics',
    GEOGRAPHY = 'Geography',
    ENGINEERING = 'Engineering',
    BIOLOGY = 'Biology'
}

def get_Journal(name: str) -> Journal by llm();



with entry {
    name = "Study of cellular respiration";
    result = get_Journal(name);
    print(f"{result.value} Journal better for publishing {name}");
}
    