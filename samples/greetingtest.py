import time
currentTime = int(time.strftime('%H:%M').split(':')[0])   
greetingItem=''

if currentTime < 12 :
     greetingItem='Good morning'
elif currentTime > 12 :
     greetingItem='Good afternoon'
else :
     greetingItem='Good evening'

print(greetingItem)
