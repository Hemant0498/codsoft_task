def simple_chatbot(user_input):

    user_input = user_input.lower()


    rules = {
        'hello': 'Hi there! How can I help you?',
        'how are you': 'I am Fine, but thanks for asking!',
        'what is your name': 'I am a sbot. You can call me Spt.',
        'bye': 'Goodbye! Have a great day!'

    }


    for pattern, response in rules.items():
        if pattern in user_input:
            return response

    return 'I don\'t understand. Can you please rephrase or ask something else?'


while True:
    user_input = input('Your question: ')
    if user_input.lower() == 'bye':
        print('Goodbye! Have a great day!')
        break
    response = simple_chatbot(user_input)
    print('Response:', response)
