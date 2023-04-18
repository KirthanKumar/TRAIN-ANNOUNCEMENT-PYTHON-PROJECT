# Creating Indian Railways Announcement System Using Python Programming

# Internet connection required to run program
import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

 
def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=True)
    myobj.save(filename)


def textToSpeechs(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=True)
    myobj.save(filename)

# this function return pydub audio segments
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateSkeleton():
    # put your audio file here for extraction
    audio = AudioSegment.from_mp3('railway.mp3')
    # 1- Generate kripiya dheyan dijiye
    start = 88000 #milli seconds
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 is from city

    # 3 - Generate se chalker
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4 is via

    # 5 se raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 is to city

    # 7 ko janne wali gaadi sankhiya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8  train number and name

    # 9 kuchi samay me platform sankhiya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10 platform number

    # 11 par aa rahi he
    start = 109000
    finish = 112150
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")

    # # ENGLISH ANNOUNCEMENTS
    # 1 - Generate may i have your attension please train number
    start = 112000
    finish = 116200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_english.mp3", format="mp3")

    # 2 - train number and train name
    # 3 - from
    start = 122600
    finish = 123480
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_english.mp3", format="mp3")

    # 4 - from station
    # 5 - to
    start = 123900
    finish = 124600
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_english.mp3", format="mp3")

    # 6 - to station
    # 7 - via
    start = 127600
    finish = 128480
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_english.mp3", format="mp3")

    # 8 - via station
    # 9 - is arriving shortly on platform number
    start = 128900
    finish = 132750
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_english.mp3", format="mp3")

    # 10 - platform
    #11 - end
    start = 133400
    finish = 134500
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_english.mp3", format="mp3")


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate from-city
        textToSpeech(item['from'], '2_hindi.mp3')

        # 4 - Generate via-city
        textToSpeech(item['via'], '4_hindi.mp3')

        # 6 - Generate to-city
        textToSpeech(item['to'], '6_hindi.mp3')

        # 8 - Generate train no and name
        textToSpeech(item['train_no'] + " " +
                     item['train_name'], '8_hindi.mp3')

        # 10 - Generate platform number
        textToSpeech(item['platform'], '10_hindi.mp3')
    # audios = [f"{i}_hindienglish.mp3" for i in range(1,12)]      ## for only (hindi announcement 137-140)

    # announcement = mergeAudios(audios)
    # announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format="mp3")

    # # english
    # for index, item in df.iterrows():
        # 2 - Generate train no and name
        textToSpeechs(item['train_no'] + " " +
                      item['train_name'], '2_english.mp3')

        # 4 - Generate from-city
        textToSpeechs(item['from'], '4_english.mp3')

        # 6 - Generate to-city
        textToSpeechs(item['to'], '6_english.mp3')

        # 8 - Generate via-city
        textToSpeechs(item['via'], '8_english.mp3')

        # 10 - Generate platform number
        textToSpeechs(item['platform'], '10_english.mp3')
        
        audios_hindi = [f"{i}_hindi.mp3" for i in range(1, 12)]
        audios_english = [f"{i}_english.mp3" for i in range(1, 12)]

        hindi_announcement = mergeAudios(audios_hindi)
        english_announcement = mergeAudios(audios_english)
    
        hindi_announcement.export(
            f"h_announcement_{item['train_no']}_{index+1}.mp3", format="mp3")
        
        english_announcement.export(
            f"e_announcement_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton..")
    generateSkeleton()
    print("Now Generating Announcemenets")
    # Enter your Excel file path here
    generateAnnouncement("announce_train.xlsx")
    print("Announcement file has been successfully created in your folder")
