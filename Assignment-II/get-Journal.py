import from byllm { Model }
import from dotenv { load_dotenv }
import os;


glob llm = Model(model_name="gemini/gemini-2.0-flash", 
api_key=os.getenv("GEMINI_API_KEY"), 
verbose=False);

enum Journal {
    CHEMISTRY = 'Chemistry', 
    PHYSICS = 'Physics',
    GEOGRAPHY = 'Geography',
    ENGINEERING = 'Engineering',
    BIOLOGY = 'Biology',
    COMPUTER_SCIENCE = 'Computer Science'
}

def get_Journal(name: str) -> Journal by llm();

with entry {
}