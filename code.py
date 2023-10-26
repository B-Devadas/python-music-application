from tkinter import *
import pandas as pd
def show():
    note = ent1.get()
    notes = set(note)
    maj_notes = []
    min_notes = []
    maj_scale = {'A':"A B C# D E F# G# A",'A#':"A# C D D# F G A A#",'B':"B C# D# E F# G# A# B",
             'C':"C D E F G A B C",'C#':"C# D# F F# G# A# C C#",'D':"D E F# G A B C# D",
             'D#':"D# F G G# A# C D D#",'E':"E F# G# A B C# D# E",'F':"F G A A# C D E F",
             'F#':"F# G# A# B C# D# F F#",'G':"G A B C D E F# G",'G#':"G# A# C C# D# F G G#"}
    min_scale = {'A':"A B C D E F G A",'A#':"A# C C# D#F F# G# A#",'B':"B C# D E F# G A B",
             'C':"C D D# F G G# A# C",'C#':"C# D# E F# G# A B C#",'D':"D E F G A A# C D",
             'D#':"D# F F# G# A# B C# D#",'E':"E F# G A B C D E",'F':"F G G# A#  C C# D# F",
             'F#':"F# G# A B C# D E F#",'G':"G A A# C D D# F G",'G#':"G# A# B C# D# E F# G#"}
    notations=['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    index = []
    ind = [i for i in range(16)]
    count = 0
    file = pd.read_csv('details.csv')
    data = pd.DataFrame(file)
#open all major scales and count all the notes in set
    for i in range(12):
        count =0
        counts = []
        x = data.loc[i][1]
        for j in notes:
            if(j.upper() in x):
                count +=1
                counts.append(count)
        min_notes.append(sum(counts))
    x = max(min_notes)
    for i in range(len(min_notes)):
        if(min_notes[i] == x):
            index.append(i)
    print("we can play the same notes in these major scales")
    for i in index:
        print(notations[i])       
    #open all minor scales and count all the notes in set
    index = []
    for i in range(12):
        count =0
        counts = []
        x = data.loc[i][2]
        for j in notes:
            if(j.upper() in x):
                count +=1
                counts.append(count)
        maj_notes.append(sum(counts))
    x = max(maj_notes)
    for i in range(len(maj_notes)):
        if(maj_notes[i] == x):
            index.append(i)
    print("we can play the same notes in these minor scales")
    for i in index:
        print(notations[i])
    print("chords for this melody is ")
    chord = str(min_scale['A'])
    chords = chord.split(" ")
    print(chords)
    print(chords[0],chords[2],chords[4]) 
    ans.configure(text = notes)
root = Tk()
root.geometry("400x400")
title = Label(root,text = "APPLICATION FOR EAR TRAINING",bg="green",fg='blue',font=('Algerian',15))
lab1 = Label(root,text= "Enter the notes of the song")
but1 = Button(root,text = "Start",bg="pink",command = show)
ent1 = Entry(root)
ans = Label(root,text="before change")
title.pack()
lab1.pack()
ent1.pack()
but1.pack()
ans.pack()
root.mainloop()
