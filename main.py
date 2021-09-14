from psychopy import visual, event, core, gui  # import some libraries from PsychoPy

#create a window
gui = gui.Dlg()
gui.addField("Subject_ID")
gui.show()
mywin = visual.Window([1600,1200], monitor="testMonitor", units="pix", color=[1,1,1])
text = visual.TextStim(win=mywin, text="Welcome, Press any key when you spot a shape of square or triagle. press any key to continue",rgb=[-1,-1,-1])
text.draw()
mywin.flip()
event.waitKeys()
clock = core.Clock()

response_times = []

for i in range(1,8):
    current = clock.getTime()
    while clock.getTime() < 3.0+current:
        img = visual.ImageStim(win=mywin,
                            image='Dataset/'+str(i)+".jpg",
                            units='pix',
                            size=[800,800]
                            )
        img.draw()
        mywin.flip()
        if(event.waitKeys(3)):
            response_times.append(clock.getTime()-current)

            break
        response_times.append(clock.getTime() - current)

mywin.close()

print("****************************************************************************************************************************************************************************************************************************************************************************************")
print("Results of ",gui.data[0])
print(response_times)




