import tkinter as tk
import requests as req
import json

root = tk.Tk()
# root.overrideredirect(True)
root.title('Info From API 2')
root.geometry('450x450')
root.config(bg = 'mistyrose1')

def getInfo(loc):
    request = req.get(f'https://restcountries.com/v2/capital/{ loc }')
    jsonOut = json.loads(request.content)

    try:
        desc = 'Name: ' + jsonOut[0]['name']
        desc += '\nRegion: ' + jsonOut[0]['region']
        desc += '\nLanguage: ' + jsonOut[0]['languages'][0]['name']
        desc += '\nPopulation: ' + str(jsonOut[0]['population'])
        desc += '\nArea: ' + str(jsonOut[0]['area'])
        lblDesc['text'] = desc
    except(KeyError):
        lblDesc['text'] = 'Invalid Location'

entLoc = tk.Entry()
entLoc.place(relx = 0.5, rely = 0.4, anchor = tk.CENTER)
btnInfo = tk.Button(root, bg = 'salmon', text = 'Get Info', command = lambda: getInfo(entLoc.get()))
btnInfo.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
lblDesc = tk.Label(root, bg = 'light blue', text = '')
lblDesc.place(relx = 0.5, rely = 0.65, anchor = tk.CENTER)

root.mainloop()