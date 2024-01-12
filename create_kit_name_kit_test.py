import data
import sender_stand_request

# Long variables for the tests
symbol511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
symbol512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"


# Getting an updated kit_body for the tests
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body


# Positive assertion
def positive_assertion(name):
    kit_body_positive = get_kit_body(name)
    kit_response_positive = sender_stand_request.post_new_client_kit(kit_body_positive)
    assert kit_response_positive.json()["name"] == name
    assert kit_response_positive.status_code == 201


# Negative assertion with a name-field in a kit_body
def negative_assertion(name):
    kit_body_negative = get_kit_body(name)
    kit_response_negative = sender_stand_request.post_new_client_kit(kit_body_negative)
    assert kit_response_negative.status_code == 400


# Negative assertion without a name-field in a kit_body
def negative_assertion_no_name(kit_body):
    kit_response_negative_no_name = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response_negative_no_name.status_code == 400


# Positive tests
# Name-field in a kit_body consists of one symbol
def test_create_kit_1_symbol_in_name_get_success_response():
    positive_assertion("a")


# Name-field in a kit_body consists of 511 symbols
def test_create_kit_511_symbols_in_name_get_success_response():
    positive_assertion(symbol511)


# Name-field in a kit_body contains an english letter
def test_create_kit_english_letters_in_name_get_success_response():
    positive_assertion("QWErty")


# Name-field in a kit_body contains a russian letter
def test_create_kit_russian_letters_in_name_get_success_response():
    positive_assertion("Мария")


# Name-field in a kit_body contains a special symbol
def test_create_kit_has_special_symbols_in_name_get_success_response():
    positive_assertion("\"№%@\",")


# Name-field in a kit_body contains a space symbol
def test_create_kit_has_space_in_name_get_success_response():
    positive_assertion("Человек и КО")
