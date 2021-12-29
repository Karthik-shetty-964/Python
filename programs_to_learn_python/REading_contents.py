# This function is used to read the given content

from win32com.client import Dispatch
speak =Dispatch("SAPI.SpVoice")
speak.Speak("Udith malla ponku mana  ")