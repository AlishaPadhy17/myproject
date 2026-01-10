# I have created this page -Alisha
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
import os

def templates_info(request):
    return HttpResponse("<h1> Hi i am Alisha </h1> ")

def text(request):
    file_path = os.path.join(settings.BASE_DIR,"myproject","Django.txt")

    with open(file_path,'r') as  file:
        content = file.read()

    return HttpResponse(content,content_type='text/html')

def navigators(request):
    navigation='''<h1><p style="text-align:center;">NAVIGATION BAR</p></h1><br>
    <a href="https://www.facebook.com/" >FACEBOOK</a><br>
    <a href="https://www.instagram.com/" > INSTAGRAM</a><br>
    <a href="https://x.com/?lang=en-id" >TWITTER</a><br>
    <a href="https://web.whatsapp.com/"> WHATSAPP</a><br>
    <a href="https://www.moneycontrol.com/" >MONEY CONTROL</a> '''

    return HttpResponse(navigation)

def index(request):
    #param= {'name':'Alisha','place':'Bangalore'}
    return render(request,"index.html")

def removePunction(request):
    djtext = request.POST.get('text', '')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    punctuations = '''!@#$%^&*,./":[]{}();'''

    analyzed_text = djtext
    purpose = []

    # 1️⃣ Remove punctuation
    if removepunc == "on":
        temp = ""
        for char in analyzed_text:
            if char not in punctuations:
                temp += char
        analyzed_text = temp
        purpose.append("Removed Punctuations")

    # 2️⃣ Convert to uppercase
    if fullcaps == "on":
        analyzed_text = analyzed_text.upper()
        purpose.append("Converted to Uppercase")

    # 3️⃣ Remove extra spaces
    if extraspaceremover == "on":
        analyzed_text = ""
        for index,char in enumerate(djtext): 
            if not(djtext[index]==" " and djtext[index+1]==" "): 
                analyzed_text=analyzed_text+char
        purpose.append("Removed Extra Spaces")

    # 4️⃣ Character count
    if charcount == "on":
        count = len(analyzed_text)
        analyzed_text = f"{analyzed_text}\n\nCharacter Count: {count}"
        purpose.append("Character Count")

    # ❌ No checkbox selected
    if not purpose:
        return HttpResponse("Please select at least one operation")

    params = {
        'purpose': ", ".join(purpose),
        'analyzedtext': analyzed_text
    }

    return render(request, "analyze.html", params)


    