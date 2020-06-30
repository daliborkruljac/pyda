import wolframalpha


app_id = "JYWLGA-Y35QPQWEGK"
client = wolframalpha.Client(app_id)

question = input("Question: ")
res = client.query(question)
answer = next(res.results).text
print (answer)
