wl = {}
fr = {}

mfwl = ['Very Low','Low','Below Danger','Danger','Above Danger']
mffr = ['Very Slow','Slow','Normal','Fast','Very Fast']

mfov = {'Fully Closed':[0,0,5],'25% Opened':[0,25,50],'50% Opened':[40,50,60],'75% Opened':[50,70,90],'Fully Opened':[70,100,100]}

wl_range = [[0,0,5],[0,5,10],[5,10,15],[10,15,20],[15,20,20]]
fr_range = [[0,0,25000],[0,25000,50000],[25000,50000,75000],[50000,75000,100000],[75000,100000,100000]]


for i in range(5):
	wl[mfwl[i]] = wl_range[i]
	fr[mffr[i]] = fr_range[i]
