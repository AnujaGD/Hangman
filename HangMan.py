#!/usr/bin/env python
# coding: utf-8

# In[1]
import pandas as pd


# In[2]:


import random


# In[3]:


path = "D:/python projects/movies_metadata/movies_metadata.csv"


# In[4]:


df = pd.read_csv(path)


# In[ ]:





# In[5]:


df = df.drop(['Unnamed: 0'],axis=1)
df= df.drop(['Unnamed: 1','Unnamed: 2','Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13'],axis=1)


# In[6]:


df.head()


# In[7]:


df.isna().sum()


# In[8]:


df = df.drop(['TITLE_2'],axis=1)


# In[9]:


df.head()


# In[10]:


df.isna().sum()


# In[11]:


df = df.dropna()


# In[12]:


df.isna().sum()


# In[13]:


df.head()


# In[14]:


df.shape


# In[17]:


#print(count)


# In[19]:


df = df.drop(df[df.HINT_1==df.HINT_2].index)


# In[20]:


df.shape


# In[28]:


def displayHint1(x):
    print(df.iloc[x,2])


# In[29]:


def displayHint2(x):
    print(df.iloc[x,1])


# In[30]:


def showAnswer(x):
    return(df.iloc[x,0])


# In[32]:


def correctAns(currentPoints):
    currentPoints = currentPoints+10
    return currentPoints


# In[33]:


def getRandomMovie():
    x = random.randint(0,20368)
    return x


# In[34]:


def checkIfAlreadyDone(x):
    return already_done.__contains__(x)


# In[51]:


def startNewLevel():
    global hints
    hints=0
    temp = getRandomMovie()
    if(checkIfAlreadyDone(temp)):
        startgame()
    else:
        already_done.append(temp)
    movie = df.iloc[temp,0]
    length = movie.__len__()
    print('-----------------------------------------------------------------------------------------')
    print("Movie name has following letters")
    print()
    print(''.join(random.sample(movie.lower(),length)))
    print('-----------------------------------------------------------------------------------------')
    
    repeat(temp)


# In[52]:


def guess():
    print('-----------------------------------------------------------------------------------------')
    print('Enter your guess')
    print('-----------------------------------------------------------------------------------------')
    g = input()
    return g


# In[53]:


def repeat(temp):
    global hints
    global currentPoints
    isHintorGuess = guess()
    if(isHintorGuess.upper()=='EXIT'):
        print('-----------------------------------------------------------------------------------------')
        print('Thank you for playing')
        print('-----------------------------------------------------------------------------------------')
    else:
        if(isHintorGuess=='HINT' or isHintorGuess=='hint'):
            if(hints==0):
                displayHint1(temp)
                hints=hints+1
                repeat(temp)
            elif(hints==1):
                displayHint2(temp)
                hints = hints+1
                repeat(temp)
            elif(hints==2):
                hints = 0
                print('-----------------------------------------------------------------------------------------')
                print('You have used all your hints.')
                print('Type ANSWER to know the answer or type your next guess')
                print('-----------------------------------------------------------------------------------------')
                repeat(temp)
        elif(isHintorGuess=='ANSWER' or isHintorGuess=='answer'):
            print(showAnswer(temp))
            print('-----------------------------------------------------------------------------------------')
            print('Do you wanna play more?')
            con = input()
            print('-----------------------------------------------------------------------------------------')
            if(con.lower()=='yes'):
                startNewLevel()
            else:
                print('-----------------------------------------------------------------------------------------')
                print('You score : '+ str(currentPoints)+" ")
                print('Thank you for playing')
                print('-----------------------------------------------------------------------------------------')
        else:
            isRight = checkAnswer(isHintorGuess,temp)
            if(isRight):
                currentPoints = correctAns(currentPoints)
                print('-----------------------------------------------------------------------------------------')
                print('You guessed right!')
                print('Your points are '+str(currentPoints))
                print('-----------------------------------------------------------------------------------------')
                startNewLevel()
            else:
                print('-----------------------------------------------------------------------------------------')
                print('You guessed wrong')
                print('-----------------------------------------------------------------------------------------')
                repeat(temp)


# In[54]:


def checkAnswer(isHintorGuess,temp):
    if(isHintorGuess.lower()==str(showAnswer(temp)).lower()  or str(showAnswer(temp)).__contains__(isHintorGuess)):
        return True
    else:
        return False


# In[58]:


currentPoints=0
hints=0
already_done=[]
print('Welcome! \n Type \'hint\' for hint or \'answer\' for answer or \'exit\' to exit the game') 
startNewLevel()


# In[ ]:




