def judge(question: str, expects: str, answer: str, results) -> bool:
    if not answer or not expects:
        return False

    has_expected = expects.lower() in answer.lower()
    not_refused = "don't have enough information" not in answer.lower()

    return has_expected and not_refused



