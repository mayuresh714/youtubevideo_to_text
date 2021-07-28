from youtube_transcript_api import YouTubeTranscriptApi
from google_trans_new import google_translator
from deep_translator import GoogleTranslator



class transcribe:
  def __init__(self):
      pass

  def hinglish(self,sent, dest="mr"):### src means lang code of sender and dest means lang code for receivers...
      to_translate =  sent
      translated = GoogleTranslator(source='auto', target= dest).translate(to_translate)
      return translated

  def fetch_id(self,url = 'https://youtu.be/kuFpDqFWSQA'):
      return url[-11:]
      
  def video_to_text(self,id = 'kuFpDqFWSQA' ):
      #transcript_list = YouTubeTranscriptApi.list_transcripts(id)
      #print(transcript_list)
      #return YouTubeTranscriptApi.get_transcripts(id, languages=['en'])
      return  YouTubeTranscriptApi.get_transcript(id)

  def dict_to_string(self,s):
      sam = ''
      for i in s:
        sam += i['text']+" "
      return sam

  def para_translate(self,data,dest):
    s = ""
    sent = data.split('.')
    #print(sent)
    for i in sent:
        s += obj.hinglish(i,dest)
    return s

  def sms_reply(self,link,lang = 'en'):
      id  = self.fetch_id(link)
      dictform = self.video_to_text(id)
      #return dictform
      text = self.dict_to_string(dictform)
      #return self.para_translate(text,dest = lang)
      return text


 