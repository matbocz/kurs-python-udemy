import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)


def translate(word):
    word = word.lower()
    cursor = con.cursor()

    cursor.execute(
        "SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
    result = cursor.fetchall()
    if len(result) > 0:
        return result
    cursor.execute(
        "SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word.title())
    result = cursor.fetchall()
    if len(result) > 0:
        return result
    cursor.execute(
        "SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word.upper())
    result = cursor.fetchall()
    if len(result) > 0:
        return result

    cursor.execute("SELECT Expression, Definition FROM Dictionary")
    result = cursor.fetchall()
    if len(get_close_matches(word, [x[0] for x in result])) > 0:
        best_match = get_close_matches(word, [x[0] for x in result])[0]
        response = input(
            "Did you mean %s instead?\nEnter Y if yes, or N if no: " % best_match)
        if response == "Y":
            cursor.execute(
                "SELECT Definition FROM Dictionary WHERE Expression = '%s'" % best_match)
            return cursor.fetchall()
        elif response == "N":
            return "The word doesn't exist."
        else:
            return "We didn't understand your entry."
    return "The word doesn't exist."


word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item[0])
else:
    print(output)
