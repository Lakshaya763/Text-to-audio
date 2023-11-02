# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 

# The text that you want to convert to audio 
mytext = ''' शब्द के कई मतलब होते हैं: वाक्य, सज़ा, दंड, मुजरिम ठहराना, सज़ा का हुक्म देना| वाक्य 
शब्दों का ऐसा समूह जिसमें किसी बात का भाव पूरी तरह से स्पष्ट हो
लिखते समय वाक्य की शुरुआत बड़े अक्षर से होती है और अंत में फ़ुल स्टॉप, प्रश्नवाचक चिह्न, या विस्मयादिबोधक चिह्न होता है
वाक्य में दो मुख्य भाग होते हैं: उद्देश्य (Subject) और विधेय (Predicate)
सज़ा दंड, कारावास, मृत्यु-दण्ड, आजीवन कारावास| 
मुजरिम ठहराना 
अपराधी ठहराना, शिकार बनाना, सज़ा देना, बता देना, तजवीज़ सुनाना, दंडाज्ञा देना, सज़ा का हुक्म देना, फ़ैसला सुनाना| 
'''

# Language in which you want to convert 
language = 'hi'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("welcome.mp3") 

# Playing the converted file 
os.system("start welcome.mp3") 
print("completed")