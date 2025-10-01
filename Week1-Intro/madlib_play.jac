impl MadlibGame.start {
    if not [root --> (`?turn)] {
        next = root ++> turn();
    } else {
        next = [root --> (`?turn)];
    }
    visit next;
}

impl MadlibGame.play {
    result = generate_madlib(self.adjective, self.verb, self.noun);
    here.madlib_result = result;
    print(result);

    disengage;
}
