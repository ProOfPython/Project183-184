import tkinter as tk
import requests as req
import json

root = tk.Tk()
# root.overrideredirect(True)
root.title('Info From API 3')
root.geometry('700x350')
root.config(bg = 'mistyrose1')

def getInfo(key, amount):
    request = req.get(f'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey={ key }')
    jsonOut = json.loads(request.content)

    try:
        lblDesc['text'] = ''
        for i in range(amount):
            lblDesc['text'] += 'Title ' + str(i + 1) + ': ' + jsonOut['articles'][i]['title'] + '\n'
            lblDesc['text'] += 'Description: ' + jsonOut['articles'][i]['description'] + '\n'
    except(KeyError):
        lblDesc['text'] = 'Invalid Key'

btnInfo = tk.Button(
    root, 
    bg = 'salmon', 
    text = 'Get Info', 
    command = lambda: getInfo('b10267cc8674415db7167f6741d30a81', 3)
)
btnInfo.place(relx = 0.5, rely = 0.1, anchor = tk.CENTER)
lblDesc = tk.Label(root, bg = 'light blue', text = '')
lblDesc.place(relx = 0.5, rely = 0.2, anchor = tk.N)

root.mainloop()