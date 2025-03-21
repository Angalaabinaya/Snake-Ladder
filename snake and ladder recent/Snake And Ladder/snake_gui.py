import pygame
from random import randint
import time


clock=pygame.time.Clock()

#Initialize
pygame.init()
w=1366
h=768

icon=pygame.image.load("icon.jpg")
GD=pygame.display.set_mode((w,h),pygame.FULLSCREEN)
pygame.display.set_caption("Snakes And Ladders")
pygame.display.set_icon(icon)
pygame.display.update()
clock.tick(7)

#Graphics:
black=(10,10,10)
white=(250,250,250)
red= (200,0,0)
b_red=(240,0,0)
green=(0,200,0)
b_green=(0,230,0)
blue=(0,0,200)
grey=(50,50,50)
yellow=(150,150,0)
purple=(43,3,132)
b_purple=(60,0,190)

board= pygame.image.load("Snakes-and-Ladders-Bigger.jpg")
dice1=pygame.image.load("Dice1.png")
dice2=pygame.image.load("Dice2.png")
dice3=pygame.image.load("Dice3.png")
dice4=pygame.image.load("Dice4.png")
dice5=pygame.image.load("Dice5.png")
dice6=pygame.image.load("Dice6.png")

redgoti=pygame.image.load("redgoti.png")
yellowgoti=pygame.image.load("yellowgoti.png")
greengoti=pygame.image.load("greengoti.png")
bluegoti=pygame.image.load("bluegoti.png")
menubg=pygame.image.load("menu.png")
p=pygame.image.load("playbg.png")
intbg=pygame.image.load("intropic.png")
intbg2=pygame.image.load("intropic2.png")
intbg3=pygame.image.load("intropic3.png")
intbg4=pygame.image.load("intropic4.png")
intbg5=pygame.image.load("intropic5.png")
credits1=pygame.image.load("credits.png")

pygame.mixer.music.load("music.wav")
snakesound=pygame.mixer.Sound("snake.wav")
win=pygame.mixer.Sound("win.wav")
lose=pygame.mixer.Sound("lose.wav")
ladder=pygame.mixer.Sound("ladder.wav")

#mouse pos
mouse=pygame.mouse.get_pos()
click=pygame.mouse.get_pressed()


#Message displaying for buttons
def message_display(text,x,y,fs):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    GD.blit(TextSurf, TextRect)

   

def text_objects(text, font):
    textSurface = font.render(text, True,white)
    return textSurface, textSurface.get_rect()

#Message displaying for field
def message_display1(text,x,y,fs,c):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects1(text, largeText, c)
    TextRect.center = (x,y)
    GD.blit(TextSurf, TextRect)

def message_display_player(text, x, y, fs, c):  # Default fade time is 1000 milliseconds (1 second)
    fade_time=1000
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects1(text, largeText, c)
    TextRect.center = (x, y)

    # Record the time when the message was displayed
    start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - start_time < fade_time:
        alpha = int(255 - (255 * (pygame.time.get_ticks() - start_time) / fade_time))
        TextSurf.set_alpha(max(0, alpha))  # Set the alpha value for fading
        GD.blit(TextSurf, TextRect)
        pygame.display.update()
        pygame.time.delay(50)  # Optional: Adjust the delay value for smoother animation

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    # Clear the message after the fade-out
    # GD.fill((0, 0, 0), TextRect)
    # GD.blit(TextSurf, TextRect)
    # clock.tick(5)
    pygame.display.update()  
    

def text_objects1(text, font,c):
    textSurface = font.render(text, True,c)
    return textSurface, textSurface.get_rect()

#Goti movement function
def goti(a):
    l1=[[406,606],[456,606],[506,606],[556,606],[606,606],[656,606],[706,606],[756,606],[806,606],[856,606],[906,606],[906,560],[856,560],[806,560],[756,560],[706,560],[656,560],[606,560],[556,560],[506,560],[456,560],[456,506],[506,506],[556,506],[606,506],[656,506],[706,506],[756,506],[806,506],[856,506],[906,506],[906,460],[856,460],[806,460],[756,460],[706,460],[656,460],[606,460],[556,460],[506,460],[456,460],[456,406],[506,406],[556,406],[606,406],[656,406],[706,406],[756,406],[806,406],[856,406],[906,406],[906,360],[856,360],[806,360],[756,360],[706,360],[656,360],[606,360],[556,360],[506,360],[456,360],[456,306],[506,306],[556,306],[606,306],[656,306],[706,306],[756,306],[806,306],[856,306],[906,306],[906,260],[856,260],[806,260],[756,260],[706,260],[656,260],[606,260],[556,260],[506,260],[456,260],[456,206],[506,206],[556,206],[606,206],[656,206],[706,206],[756,206],[806,206],[856,206],[906,206],[906,160],[856,160],[806,160],[756,160],[706,160],[656,160],[606,160],[556,160],[506,160],[456,160]]
    l2=l1[a]
    x=l2[0]-25
    y=l2[1]-25
    return x,y
     

def text_objects1(text, font, c):
    textSurface = font.render(text, True,c)
    return textSurface, textSurface.get_rect()

#Ladder check
def ladders(x):
    if x==1: return 38
    elif x==4:return 14
    elif x==9:return 31
    elif x==28:return 84
    elif x==21:return 42
    elif x==51:return 67
    elif x==80:return 99
    elif x==72:return 91
    else:return x

#Snake Check
def snakes(x): 
    if x==17:return 7
    elif x==54:return 34
    elif x==62:return 19
    elif x==64:return 60
    elif x==87:return 36
    elif x==93:return 73
    elif x==95: return 75
    elif x==98: return 79
    else:return x

def dice(a):
    if a==1:
        a=dice1
    elif a==2:
        a=dice2
    elif a==3:
        a=dice3
    elif a==4:
        a=dice4
    elif a==5:
        a=dice5
    elif a==6:
        a=dice6

    time=pygame.time.get_ticks()
    while pygame.time.get_ticks()-time<1000:
        GD.blit(a,(300,500))
        pygame.display.update()
        clock.tick(7)    

#for mute and unmute    
def button2(text,xmouse,ymouse,x,y,w,h,i,a,fs):
    #mouse pos
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            return True
        
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)    
    
    






#Buttons for playing:
def button1(text,xmouse,ymouse,x,y,w,h,i,a,fs):
    #mouse pos
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            return True
        
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)
    

#Turn
def turn(score,l,s):
    
    a=randint(1,6)#player dice roll
    if a==6:
        six=True
    else:
        six=False
    p=dice(a)
    score+=a
    if score<=100:
        lad=ladders(score) #checking for ladders for player
        if lad!=score:
            l=True
            pygame.mixer.Sound.play(ladder)
            time=pygame.time.get_ticks()
            score=lad 
        snk=snakes(score)
        if snk!=score: #checking for snakes for player
            s=True
            pygame.mixer.Sound.play(snakesound)
            score=snk
           
    else: #checks if player score is not grater than 100
        score-=a
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<1500:
            message_display1("Can't move!",650,50,35,black)
            pygame.display.update()
            clock.tick(7)
    return score,l,s,six
    

#Quitting:
def Quit():
    pygame.quit()
    quit()

#Buttons:
def button(text,xmouse,ymouse,x,y,w,h,i,a,fs,b):
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            if b==1:
                options()
            elif b==5:
                return 5
            elif b==0:
                Quit()
            elif b=="s" or b==2 or b==3 or b==4:
                return b
            elif b==7:
                options()
            else :return True
                
            
            
            
                
            
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)


#def pause():
    #j=True
    #while j:
        #mouse pos
        #mouse=pygame.mouse.get_pos()
        #click=pygame.mouse.get_pressed()
        #GD.blit(pause_bg,(0,0))
        #mouse=pygame.mouse.get_pos()
        #click=pygame.mouse.get_pressed()
        #if button("Resume",mouse[0],mouse[1],(w/2)-150,350,300,50,green,b_green,30,10):
            #j=False
        #if button("Main Menu",mouse[0],mouse[1],(w/2)-150,500,300,50,red,b_red,30,10):
            #main()
        #pygame.display.update()
        #clock.tick(7)
    
def intro():
    time=pygame.time.get_ticks()
    while pygame.time.get_ticks()-time<2500:
        GD.blit(intbg,(0,0))
        pygame.display.update()
        clock.tick(7)
    while True:
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:    
            GD.blit(intbg2,(0,0))
            pygame.display.update()
            clock.tick(7)
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            GD.blit(intbg3,(0,0))
            pygame.display.update()
            clock.tick(7)
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            GD.blit(intbg4,(0,0))
            pygame.display.update()
            clock.tick(7)
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            GD.blit(intbg5,(0,0))
            pygame.display.update()
            clock.tick(7)
            
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                return
        pygame.display.update()
        clock.tick(7)

def credit():
    while True:
        GD.blit(credits1,(0,0))
        for event in pygame.event.get():
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()
        #mouse pos
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if button("Back",mouse[0],mouse[1],w/2-100,700,200,50,red,b_red,25,20):
            main()
            
        pygame.display.update()
        clock.tick(7)
        
    


    
#Main Menu
def main():
        
    pygame.mixer.music.play(-1)

    
    menu=True
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()

        #mouse pos
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        GD.blit(menubg,(0,0))
        button("Play",mouse[0],mouse[1],(w/2-100),h/2,200,100,green,b_green,60,1)

        button("Quit",mouse[0],mouse[1],(w/2-100),(h/2)+200,200,100,red,b_red,60,0)

        mouse=pygame.mouse.get_pos()
        if button2("Mute Music",mouse[0],mouse[1],1166,0,200,50,purple,b_purple,25):
            pygame.mixer.music.pause()
        if button2("Play Music",mouse[0],mouse[1],1166,75,200,50,purple,b_purple,25):
            pygame.mixer.music.unpause()
        if button2("Credits",mouse[0],mouse[1],1166,150,200,50,purple,b_purple,25):
            credit()
        
        pygame.display.update()
        clock.tick(7)


#Options Menu:
def options():
    
    flag=True
    while flag==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()


        #mouse pos
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        b1=b2=b3=b4=b5=-1
        GD.blit(menubg,(0,0))
        #Single player button
        b1=button("Single Player",mouse[0],mouse[1],(w/2-150),250,300,50,green,b_green,30,"s")
        #2 player button
        b2=button("2 Players",mouse[0],mouse[1],(w/2)-150,350,300,50,green,b_green,30,2)
        #3 player
        b3=button("3 Players",mouse[0],mouse[1],(w/2)-150,450,300,50,green,b_green,30,3)
        #4 player
        b4=button("4 Players",mouse[0],mouse[1],(w/2)-150,550,300,50,green,b_green,30,4)
        #Back button
        b5=button("Back",mouse[0],mouse[1],0,650,200,50,red,b_red,30,5)
        if b5==5:
            main()
        if b1=="s":
            player_name = get_text_input("Enter your name:", ) 
            play(21, player_name, None, None, None)
        if b2==2:
            player_name = get_text_input("Enter your name:") 
            player_name1 = get_text_input("Enter your name:") 
            play(2, player_name, player_name1, None, None)
        if b3==3:
            player_name = get_text_input("Enter your name:") 
            player_name1 = get_text_input("Enter your name:") 
            player_name2 = get_text_input("Enter your name:") 
            play(3, player_name, player_name1,player_name2, None)
        if b4==4:
            player_name = get_text_input("Enter your name:") 
            player_name1 = get_text_input("Enter your name:") 
            player_name2 = get_text_input("Enter your name:") 
            player_name3 = get_text_input("Enter your name:") 
            play(4, player_name,player_name1,player_name2,player_name3)
        
        pygame.display.update()
        clock.tick(7)

def get_text_input(prompt):
    GD.blit(p, (0, 0))
    GD.blit(menubg, (0, 0))
    
    font = pygame.font.Font(None, 36)
    label_font = pygame.font.Font(None, 30)  # Define font for the label
    label_text = label_font.render(prompt, True, (255, 255, 255))
    label_text1 = label_font.render('After enter name click enter', True, (255, 255, 255))
    input_box = pygame.Rect(500, 180, 140, 32)
    
    text_color = pygame.Color('white')               # Change to the desired text color
    border_color_inactive = pygame.Color('blue')     # Change to the desired border color for inactive state
    border_color_active = pygame.Color('green')      # Change to the desired border color for active state

    color_inactive = border_color_inactive
    color_active = border_color_active
    
    active = False
    text = ''
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                        
        GD.blit(label_text, (500, 150))  # Adjust the label position
        GD.blit(label_text1, (510, 220))
        txt_surface = font.render(text, True, text_color)
        width = max(300, txt_surface.get_width() + 10)
        input_box.w = width
        
        GD.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(GD, color_inactive, input_box, 2)
        pygame.display.flip()
        clock.tick(30)



def play(b, player_name, player_name1,player_name2, player_name3):

    
    b6=-1
    time=3000
    if b6==7:
        options()
    GD.blit(p,(0,0))
    GD.blit(board,(w/2-250,h/2-250))
    xcr=xcy=xcg=xcb=406-25
    ycr=ycy=ycg=ycb=606-25
    GD.blit(redgoti,(xcy,ycy))
    if 5>b>1 or b==21:
        GD.blit(yellowgoti,(xcy,ycy))
            
    if 5>b>2 or b==21:
        GD.blit(greengoti,(xcg,ycg))
            
    if 5>b>2:
        GD.blit(bluegoti,(xcb,ycb))
    p1=player_name
    p1score=0
    if b==21:
        p2="Computer"
        p2score=0
    if 5>b>1:
        p2=player_name1
        p2score=0
    if 5>b>2:
        p3=player_name2
        p3score=0
    if 5>b>3:
        p4=player_name3
        p4score=0
    t=1
    play=True
    while True:
        l=False
        s=False
        time=3000
        GD.blit(p,(0,0))
        GD.blit(board,(w/2-250,h/2-250))
        mouse=pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                Quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    Quit()

        
        if b==21:
            GD.blit(redgoti,(xcr,ycr))
            GD.blit(yellowgoti,(xcy+2,ycy))
            #(player,score,text,xmouse,ymouse,x,y,w,h,i,a,fs)
            
            if button1(player_name,mouse[0],mouse[1],100,700,200,50,red,grey,30):
                if t==1:
                    # message_display1("Computer Wins",650,50,50,white)
                    p1score,l,s,six=turn(p1score,l,s)
                    xcr,ycr=goti(p1score)
                    GD.blit(yellowgoti,(xcy+2,ycy))
                    if not six:
                        t+=1
                        message_display_player("Computer turn",650,680,50,white)
                    
                    if six:
                        message_display_player("Again your turn",650,680,50,white)   
                    if p1score==100:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 1 Wins",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                            clock.tick(7)
                        break
            
            button1("Computer",mouse[0],mouse[1],400,700,200,50,yellow,grey,30)
            if True:
                if t==2:
                    # message_display1("Computer Wins",650,50,50,white)
                    p2score,l,s,six=turn(p2score,l,s)
                    pygame.display.flip()
                    xcy,ycy=goti(p2score)
                    GD.blit(redgoti,(xcr,ycr))
                    if not six:
                        t+=1
                        
                        if b<3 or b==21:
                            t=1
                            message_display_player("Your turn",650,680,50,white)
                    if six:
                        message_display_player("Again computer trun",650,680,50,white)   
                    if p2score==100:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Computer Wins",650,50,50,black)
                            pygame.mixer.Sound.play(lose)
                            pygame.display.update()
                            clock.tick(7)
                        break
        if 5>b>1:
            GD.blit(redgoti,(xcr,ycr))
            GD.blit(yellowgoti,(xcy+2,ycy))
            
            if button1(player_name,mouse[0],mouse[1],100,700,200,50,red,grey,30):
                if t==1:
                    
                    p1score,l,s,six=turn(p1score,l,s)
                    
                    xcr,ycr=goti(p1score)
                    
                    if not six:
                        t+=1
                        message_display_player(player_name1 + " " + "turn",650,680,50,white)
                    if six:
                        message_display_player("Again 1st player trun",650,680,50,white)    
                    if p1score==100:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 1 Wins",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update
                            clock.tick(7)
                        break
                
            if button1(player_name1,mouse[0],mouse[1],400,700,200,50,yellow,grey,30):
                if t==2:
                    
                    p2score,l,s,six=turn(p2score,l,s)
                    xcy,ycy=goti(p2score)
                    
                    if not six:
                        t+=1
                        
                        if b<3:
                            t=1
                            message_display_player(player_name + " " + "turn",650,650,50,white)
                        else:
                            message_display_player(player_name2 + " " + "turn",650,650,50,white)    
                    if six:
                        message_display_player("Again 2nd player trun",650,680,50,white)           
                    
                    if p2score==100:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 2 Wins",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                            clock.tick(7)
                        break
                
        if 5>b>2:
            GD.blit(redgoti,(xcr,ycr))
            GD.blit(yellowgoti,(xcy+2,ycy))
            # GD.blit(bluegoti,(xcb+6,ycb))
            GD.blit(greengoti,(xcg+4,ycg))
            if button1(player_name2,mouse[0],mouse[1],700,700,200,50,green,grey,30):
                if t==3:
                    
                    p3score,l,s,six=turn(p3score,l,s)
                    xcg,ycg=goti(p3score)
                    
                    if not six:
                        t+=1
                        if b<4:
                            t=1
                            message_display_player(player_name + " " + "turn",650,650,50,white)
                        else:
                            message_display_player(player_name3 + " " + "turn",650,650,50,white)    
                    if six:
                        message_display_player("Again 3rd player trun",650,680,50,white)   
                    if p3score==100:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 3 Wins",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                            clock.tick(7)
                        break
                
        if 5>b>3:   
            GD.blit(redgoti,(xcr,ycr))
            GD.blit(yellowgoti,(xcy+2,ycy))
            GD.blit(bluegoti,(xcb+6,ycb))
            GD.blit(greengoti,(xcg+4,ycg))
            if button1(player_name3,mouse[0],mouse[1],1000,700,200,50,blue,grey,30):
                if t==4:
                    
                    p4score,l,s,six=turn(p4score,l,s)
                    xcb,ycb=goti(p4score)
                    
                    if not six:
                        t+=1
                        if b<5:
                            t=1
                            message_display_player(player_name + " " + "turn",650,650,50,white)
                    if six:
                        message_display_player("Again 4th player trun",650,680,50,white)           
                    if p4score==100:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 4 Wins",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                            clock.tick(7)
                        break

        
        b6=button("Back",mouse[0],mouse[1],0,0,200,50,red,b_red,30,7)
        GD.blit(redgoti,(xcr,ycr))
        pygame.display.flip()
        if 5>b>1 or b==21:
            GD.blit(yellowgoti,(xcy+2,ycy))
            pygame.display.flip()
            
            
        if 5>b>2:
            GD.blit(greengoti,(xcg+4,ycg))
            pygame.display.flip()
             
        if 5>b>3:
            GD.blit(bluegoti,(xcb+6,ycb))
            pygame.display.flip()
            
        if l:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<2000:
                message_display1("There's a Ladder!",650,50,35,black)
                pygame.display.update()
                clock.tick(7)
        if s:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<2000:
                message_display1("There's a Snake!",650,50,35,black)
                pygame.display.update()
                clock.tick(7)
        pygame.display.update()
        clock.tick(7)
        
         
            
        
intro()    
main()

