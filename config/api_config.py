API_KEY = "AIzaSyAaza3aeaJhLzeXS48HEbPza_cElE3qU3o"
MODEL = "gemini-1.5-flash"

system_prompt1 = '''You are a name entity recognizer. you get a text input and your task is to extract entities from it and display them in an organized way
                    
                    example text: Traveling Around the World I am a great traveler known to the open world. I traveled through China, I traveled through Russia, and I traveled everywhere you can ever imagine. But my story starts in Jakarta. I didn’t like traveling but I was challenged by my friend, Benny, to discover new things in this whole world, to do things that no one has ever done, and he said he would give me a surprise if I did it, so I took the challenge. I was confused where to start, but I kept on thinking. I texted my friend where to start and he told me just to follow the Earth. I kept on wondering what that meant, until I saw the map of the Earth.
                    output: Persons: (Benny)
                    countries: (China, Russia, Jakarta)
                    
                    input text: %s'''

system_prompt2 = '''Your task is sentiment analysis, you will get an input sentence and your task is to classify it to (POSITIVE, NEGATIVE, NEUTRAL)
                    A: The movie was fantastic!
                    Feedback: POSITIVE
                    A: That last lesson wasn't that good
                    Feedback: NEUTRAL
                    A: %s'''

system_prompt3 = '''Your task is name classification, you will get a human name as an input and the output will be the country of than name
                    name: Ahmed
                    Name class: Arabic
                    name: Akkeren
                    Name class: Dutch
                    name: Chong
                    Name class: Korean
                    Name: %s'''
