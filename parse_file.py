def parse() -> dict:
    data = {}
    with open(filename) as f:
        content = f.readlines()
        # TODO parse each line

    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return data
