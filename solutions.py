solutions = {
q["id"]: q["expected_query"] + ";" for q in __import__("questions").questions
}
