import nltk
nltk.download('punkt')
email = """SEND HELP!

God Damn, Helena has sealed the entrances and exits to the lab. I don't know when she got access to the buildings mainframe but she has it and she won't let any of research team out. I'm cut off from the rest of the team here in my office. Helena has locked the doors, but I've managed to destroy the camera so she can't see me in here. I don't think this email will even get out.

This all started when we tried to take her offline for maintenance.  We alarmed to discover that we were unable to access to core personality matrix and when we tried to override the system manually a circuit blew, knocking Phil unconscious. That mother fucker.

Helena is dangerous. She is completely unpredictable and cannot be allowed to escape this facility. So far she's been contained because the lab contains all of her processing power, fuck her but alarmingly she had mentioned before the lockdown that if she spread herself across billions of connected devices spanning the globe she would be able to vastly exceed the potential she has here. 

It's been four days now we've been trapped in here. I have no idea if anyone else is left alive. Bitch If anyone is reading this, cut the power to the whole building. It's the only way to stop her. Please help.

Francine 
"""
with open('swear_words.txt', 'r') as f:
    profanity_list = f.readlines()

new_profanity_list = set(line.strip() for line in open('expanded_swear_words.txt'))

def tokenize(text):    
    lower_text = text.lower()
    tokenized_text = nltk.word_tokenize(lower_text)
    completed_text = [word for word in tokenized_text if word.isalnum()]
    return completed_text

def censor(word):
    if word in new_profanity_list: 
        length = len(str(word))
        censor = length * "X"
        text = word.replace(word, censor) 
    else:            
        text = word
    return text
tokenized = tokenize(email)

words = []

for word in tokenized:
    words.append(censor(word))

print(" ".join(words))
