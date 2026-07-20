from app.rag.rag_chain import answer_question

metrics = """
Revenue : ₹2,500,000
Profit : -₹120,000
Orders : 580
"""

question = "Why is my profit decreasing?"

response = answer_question(metrics, question)

print(response)
