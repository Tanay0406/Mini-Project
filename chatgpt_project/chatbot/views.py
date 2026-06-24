from django.shortcuts import render

chat_history = []

def home(request):

    global chat_history
    if request.method == "GET" and "clear" in request.GET:
       chat_history.clear()
    
    if request.method == "POST":

        user_message = request.POST.get("message", "")
        message = user_message.lower()

        chatbot = {
            "hello": "Hello! Welcome to ChatGPT in Django.",
            "hi": "Hi! How can I help you?",
            "how are you": "I'm doing great. Thank you!",
            "what is your name": "My name is Django ChatBot.",
            "who created you": "I was created using Python and Django.",
            "what is django": "Django is a powerful Python web framework.",
            "what is python": "Python is a powerful programming language.",
            "what is html": "HTML is used to create web pages.",
            "what is css": "CSS is used to design web pages.",
            "what is javascript": "JavaScript adds interactivity to websites.",
            "what is ai": "AI stands for Artificial Intelligence.",
            "what is machine learning": "Machine Learning is a branch of AI.",
            "what is chatgpt": "ChatGPT is an AI chatbot developed by OpenAI.",
            "thank you": "You're welcome!",
            "bye": "Goodbye! Have a nice day."
        }

        response = chatbot.get(message, "Sorry, I don't understand.")

        chat_history.append({
            "user": user_message,
            "bot": response
        })

    return render(request, "index.html", {
        "chat_history": chat_history
    })